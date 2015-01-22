# -*- coding: utf-8 -*-
#!/usr/bin/env python
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
#     Anna Chabuda <anna.chabuda@gmail.com>
#

import os.path, thread, time, Queue

from maze_logic import MazeLogic
from maze_wii_logic import MazeWiiLogic
from tags.tagger import Tagger

from obci.exps.ventures.data import data_manager

class MazeGame(object):
    def __init__(self, user_id, sesion_duration=30*60, time_board_display=5, time_left_out=30, 
                 maze_path_display=False, tag_status=True, tag_name='', tag_dir='./'):
	self._init_queue()
        super(MazeGame, self).__init__()
        self.user_id = user_id
        self.sesion_number = data_manager.sesion_number_get(self.user_id)
        self.sesion_type = data_manager.sesion_type_get(self.user_id)
        self.sesion_duration = sesion_duration
        self.time_board_display = time_board_display
        self.time_left_out = time_left_out
        self.maze_path_display = maze_path_display
        self.tagger_init(tag_name, tag_dir, tag_status)

    def tagger_init(self, tag_name, tag_dir, tag_status):
        if tag_status:
            self.tagger = Tagger(tag_name, tag_dir, status='ON')
        else:
            self.tagger = Tagger(tag_name, tag_dir, status='OFF')

    def _get_start_info(self, user_name):
        return self.user_data_parser.get_user_trening_data(user_name)

    def run(self):
        if self.sesion_type == 'wii':
            game = MazeWiiLogic(data_manager.maze_current_level_get_last(self.user_id),
                                data_manager.wii_current_level_get_last(self.user_id),
                                self.sesion_number, 
                                self.sesion_duration, 
                                self.time_board_display, 
                                self.time_left_out, 
                                self.maze_path_display, 
                                self.tagger, 
                                self.sesion_type, 
                                self)
        else:
            game = MazeLogic(data_manager.maze_current_level_get_last(self.user_id), 
                             self.sesion_number, 
                             self.sesion_duration, 
                             self.time_board_display, 
                             self.time_left_out, 
                             self.maze_path_display, 
                             self.tagger, 
                             self.sesion_type)
        game.main()
        if self.sesion_type == 'wii':
            data_manager.wii_current_level_set(self.user_id, game.get_current_wii_level())
        data_manager.maze_current_level_set(self.user_id, game.get_current_level())

    def _init_queue(self):
        self._queue = Queue.Queue()

    def handle_message(self, msg):
        self._queue.put(msg)
    
    def get_message(self):
        if self._queue.qsize() > 5:
            print("Warning! Queue size is: "+str(self._queue.qsize()))
        try:
            return self._queue.get_nowait()
        except Queue.Empty:
            return None

def test_maze():
    a = MazeGame('1')
    thread.start_new_thread(a.run, ())
    x = 0
    while True:
        a.handle_message((2, x%100))
        x += 1
        for i in range(10000):
            i
	if x % 5 == 0:
	    for i in range(5):
		a.get_message()

def run_maze():
    a = MazeGame('1')
    a.run()
    
if __name__ == '__main__':
    run_maze()