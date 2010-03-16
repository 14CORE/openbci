#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# OpenBCI - framework for Brain-Computer Interfaces based on EEG signal
# Project was initiated by Magdalena Michalska and Krzysztof Kulewski
# as part of their MSc theses at the University of Warsaw.
# Copyright (C) 2008-2009 Krzysztof Kulewski and Magdalena Michalska
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author:
#     Mateusz Kruszyński <mateusz.kruszynski@gmail.com>


from multiplexer.multiplexer_constants import peers, types
from multiplexer.clients import BaseMultiplexerServer

import signalml_save_manager
import sys
import settings, variables_pb2
import data_storage_logging
LOGGER = data_storage_logging.get_logger("signal_saver")

class SignalSaver(BaseMultiplexerServer):
    def __init__(self, addresses):
        super(SignalSaver, self).__init__(addresses=addresses, 
                                          type=peers.SIGNAL_SAVER)
        self._session_is_active = False
        self._save_manager = None

    def handle_message(self, mxmsg):
        """Handle messages:
        * amplifier_signal_message - raw data from mx.
        If session is active convey data to save_manager.
        * signal_saver_control_message - start or finish saving session
        depending on data received."""
        if mxmsg.type == types.AMPLIFIER_SIGNAL_MESSAGE and \
                self._session_is_active:
            l_vec = variables_pb2.SampleVector()
            l_vec.ParseFromString(mxmsg.message)
	    for i_sample in l_vec.samples:
                self._save_manager.data_received(i_sample.value)

        elif mxmsg.type == types.SIGNAL_SAVER_CONTROL_MESSAGE:
            LOGGER.info("Signal saver got signal_saver_control_message: "+\
                            mxmsg.message)
            if mxmsg.message == 'finish_saving':
                self.finish_saving_session()
            elif mxmsg.message == 'start_saving':
                self.start_saving_session()
                
    def start_saving_session(self):
        if self._session_is_active:
            LOGGER.error("Attempting to start saving signal to file while not closing previously opened file!")
            return 
        self._session_is_active = True
        l_signal_params = {}
        l_freq = int(self.conn.query(message = "SamplingRate", 
                                     type = types.DICT_GET_REQUEST_MESSAGE, 
                                     timeout = 1).message)
        l_ch_nums = self.conn.query(message = "AmplifierChannelsToRecord", 
                                    type = types.DICT_GET_REQUEST_MESSAGE, 
                                    timeout = 1).message.strip().split(' ')
        l_ch_names = self.conn.query(message = "ChannelsNames", 
                                     type = types.DICT_GET_REQUEST_MESSAGE, 
                                     timeout = 1).message.strip().split(';')
        l_ch_gains = self.conn.query(message = "Gain", 
                                     type = types.DICT_GET_REQUEST_MESSAGE, 
                                     timeout = 1).message.strip().split(' ')
        l_ch_offsets = self.conn.query(message = "Offset", 
                                       type = types.DICT_GET_REQUEST_MESSAGE, 
                                       timeout = 1).message.strip().split(' ')
        l_f_name =  self.conn.query(message = "SaveFileName", 
                                    type = types.DICT_GET_REQUEST_MESSAGE, 
                                    timeout = 1).message
        l_f_path = self.conn.query(message = "SaveFilePath", 
                                   type = types.DICT_GET_REQUEST_MESSAGE, 
                                   timeout = 1).message

        l_signal_params['number_of_channels'] = len(l_ch_nums)
        l_signal_params['sampling_frequency'] = l_freq
        l_signal_params['channels_numbers'] = l_ch_nums
        l_signal_params['channels_names'] = l_ch_names
        l_signal_params['channels_gains'] = l_ch_gains
        l_signal_params['channels_offsets'] = l_ch_offsets

        l_log = "Start saving to file "+l_f_path+l_f_name+" with values:\n"
        for i_key, i_value in l_signal_params.iteritems():
            l_log = ''.join([l_log, i_key, " : ", str(i_value), "\n"])
        LOGGER.info(l_log)

        self._save_manager = signalml_save_manager.SignalmlSaveManager(
           l_f_name, l_f_path, l_signal_params)

    def finish_saving_session(self):
        if not self._session_is_active:
            LOGGER.error("Attempting to stop saving signal to file while no file being opened!")
            return
        l_files = self._save_manager.finish_saving()
        self._session_is_active = False
        LOGGER.info("Saved files: \n"+l_files[0]+"\n"+l_files[1])
        return l_files

if __name__ == "__main__":
    SignalSaver(settings.MULTIPLEXER_ADDRESSES).loop()


        
