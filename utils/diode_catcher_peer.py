#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:
#     Mateusz Kruszyński <mateusz.kruszynski@titanis.pl>

import os.path
import sys

from multiplexer.multiplexer_constants import peers, types
from obci_control.peer.configured_multiplexer_server import ConfiguredMultiplexerServer

from configs import settings, variables_pb2
from utils import tags_helper
from utils import openbci_logging as logger
LOGGER = logger.get_logger("diode_catcher_peer", 'debug')

class DiodeCatcher(ConfiguredMultiplexerServer):
    def __init__(self, addresses):
        super(DiodeCatcher, self).__init__(addresses=addresses,
                                          type=peers.DIODE_CATCHER)
        self.ready()

    def handle_message(self, mxmsg):
        if mxmsg.type == types.DIODE_MESSAGE:
            msg = variables_pb2.Diode()
            msg.ParseFromString(mxmsg.message)
            LOGGER.debug("GOT DIODE: "+repr(msg.timestamp)+" / "+str(msg.value))
            tags_helper.send_tag(self.conn, msg.timestamp, msg.timestamp, "diode",
                                 {"freqs" : msg.value})
        self.no_response()

if __name__ == "__main__":
    DiodeCatcher(settings.MULTIPLEXER_ADDRESSES).loop()

