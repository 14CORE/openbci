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

LEVELS_TIMEOUT = 180

LEVELS = { '1': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,0,1,0,1,0,1],
                 [1,1,0,4,0,0,0,0,0,1],
                 [1,0,0,1,0,0,1,0,0,1],
                 [1,3,1,2,0,0,0,0,0,1],
                 [1,0,0,1,0,0,0,0,1,1],
                 [1,1,0,0,1,1,0,0,0,1],
                 [1,0,0,0,0,0,0,1,0,1],
                 [1,0,1,0,0,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

           '2': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,0,0,1,0,0,1],
                 [1,0,0,0,2,0,0,2,1,1],
                 [1,0,1,0,0,0,0,0,0,1],
                 [1,0,0,0,3,0,0,1,0,1],
                 [1,0,0,0,1,0,0,0,0,1],
                 [1,2,0,0,0,0,0,2,0,1],
                 [1,0,0,0,0,0,1,0,0,1],
                 [1,0,1,4,1,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
           '3': [[1,1,1,1,1,1,1,1,1,1],
                 [1,2,0,0,1,0,0,0,2,1],
                 [1,1,0,0,0,0,0,0,1,1],
                 [1,2,0,3,0,0,0,0,1,1],
                 [1,1,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,1,2,1,1],
                 [1,1,0,0,0,0,1,1,1,1],
                 [1,2,0,0,0,0,0,4,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
           '4': [[1,1,1,1,1,1,1,1,1,1],
                 [1,2,0,0,1,0,0,2,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,1,0,4,0,1],
                 [1,1,0,0,0,1,2,0,1,1],
                 [1,2,0,0,3,0,0,0,1,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,1,0,0,0,1,0,1],
                 [1,0,0,2,1,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
           '5': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,1,0,4,0,1],
                 [1,0,0,0,0,0,0,0,2,1],
                 [1,0,0,1,1,0,0,0,0,1],
                 [1,0,0,0,0,0,1,0,0,1],
                 [1,0,1,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,2,0,0,1],
                 [1,1,0,0,3,0,0,0,1,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
           '6': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,2,2,0,0,1,2,1],
                 [1,0,3,0,0,0,0,0,1,1],
                 [1,0,1,0,0,1,0,0,0,1],
                 [1,0,4,0,0,0,0,0,0,1],
                 [1,0,0,2,0,0,0,1,0,1],
                 [1,1,0,0,0,1,0,0,2,1],
                 [1,1,2,1,0,0,0,1,0,1],
                 [1,1,0,0,0,1,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
           '7': [[1,1,1,1,1,1,1,1,1,1],
                 [1,2,1,0,0,3,1,2,0,1],
                 [1,0,0,0,0,0,1,0,0,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,0,0,0,1,1,0,0,0,1],
                 [1,0,0,0,0,0,1,0,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,2,0,0,0,0,0,4,0,1],
                 [1,0,0,1,0,0,1,1,1,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
           '8': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,0,2,2,2,2,1],
                 [1,3,0,0,0,0,1,1,1,1],
                 [1,0,1,0,0,0,0,2,2,1],
                 [1,0,1,0,0,0,0,1,1,1],
                 [1,0,1,2,0,0,0,0,0,1],
                 [1,0,2,4,0,0,0,0,0,1],
                 [1,0,0,0,0,1,0,0,0,1],
                 [1,1,0,0,0,0,0,1,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
           '9': [[1,1,1,1,1,1,1,1,1,1],
                 [1,1,1,0,0,0,4,0,1,1],
                 [1,1,0,0,2,1,0,0,1,1],
                 [1,1,0,0,1,0,0,0,1,1],
                 [1,1,0,0,3,1,0,0,1,1],
                 [1,1,0,0,0,0,0,1,1,1],
                 [1,1,0,0,1,2,0,0,1,1],
                 [1,1,0,0,1,0,0,0,1,1],
                 [1,1,0,0,0,0,0,0,1,1],
                 [1,1,1,1,1,1,1,1,1,1]], 

            
          '10': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,0,1,0,2,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,1,0,0,0,3,1,0,0,1],
                 [1,0,0,0,1,1,0,0,0,1],
                 [1,0,0,0,1,1,0,0,0,1],
                 [1,0,0,0,0,0,4,0,0,1],
                 [1,2,1,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,1,1,1,1,1,1,1,1,1]],
             
          '11': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,0,1,0,0,0,1],
                 [1,0,0,1,0,0,1,4,0,1],
                 [1,0,1,1,0,0,1,0,2,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,0,0,1,0,0,1,0,0,1],
                 [1,0,3,1,0,0,1,1,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,0,1,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
          '12': [[1,1,1,1,1,1,1,1,1,1],
                 [1,1,2,0,0,0,1,2,0,1],
                 [1,1,1,0,0,2,1,0,0,1],
                 [1,1,0,0,0,0,0,0,0,1],
                 [1,1,0,3,0,0,1,0,0,1],
                 [1,0,0,0,1,0,2,0,0,1],
                 [1,0,0,1,0,0,0,0,2,1],
                 [1,0,0,0,0,0,0,4,0,1],
                 [1,0,1,0,0,0,1,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
          '13': [[1,1,1,1,1,1,1,1,1,1],
                 [1,2,2,2,0,0,0,0,1,1],
                 [1,0,1,0,0,2,0,0,0,1],
                 [1,0,0,0,0,0,4,0,0,1],
                 [1,0,0,1,0,0,0,0,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,1,0,3,0,0,1,0,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,1,1,1,0,0,1,2,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
          '14': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,2,0,0,0,0,1,1],
                 [1,1,0,4,0,0,0,0,0,1],
                 [1,0,0,0,0,1,0,0,0,1],
                 [1,1,0,0,0,0,1,0,0,1],
                 [1,1,1,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,1,0,0,1],
                 [1,0,3,0,0,0,0,0,0,1],
                 [1,0,2,1,1,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '15':  [[1,1,1,1,1,1,1,1,1,1],
                 [1,1,1,1,0,1,1,1,1,1],
                 [1,1,1,0,0,0,0,1,1,1],
                 [1,1,0,3,0,0,0,0,1,1],
                 [1,2,0,0,1,4,0,0,0,1],
                 [1,0,0,0,2,0,0,0,2,1],
                 [1,1,0,0,0,0,0,0,1,1],
                 [1,1,1,0,0,0,1,2,1,1],
                 [1,1,1,1,0,0,1,1,1,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
          '16': [[1,1,1,1,1,1,1,1,1,1],
                 [1,3,0,0,0,0,0,1,1,1],
                 [1,0,1,1,1,1,0,0,1,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,1,1,1,2,1,0,0,0,1],
                 [1,4,0,0,0,0,0,0,1,1],
                 [1,2,0,0,0,0,0,1,1,1],
                 [1,0,0,0,0,0,1,1,1,1],
                 [1,0,0,0,0,1,1,1,1,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
          '17': [[1,1,1,1,1,1,1,1,1,1],
                 [1,3,0,0,0,0,1,2,0,1],
                 [1,0,0,0,1,0,0,0,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,1,0,0,0,0,1,0,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,1,0,0,0,0,2,1],
                 [1,0,0,0,0,1,4,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
          '18': [[1,1,1,1,1,1,1,1,1,1],
                 [1,1,1,1,2,0,0,0,2,1],
                 [1,0,0,0,0,0,0,0,4,1],
                 [1,0,0,1,1,0,1,0,0,1],
                 [1,0,0,1,0,3,0,0,1,1],
                 [1,0,0,0,0,0,1,0,0,1],
                 [1,2,0,0,0,0,0,1,0,1],
                 [1,1,0,0,0,0,0,0,0,1],
                 [1,1,0,0,2,1,2,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]], 
            
          '19': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,3,0,1,0,0,0,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,1,0,0,1],
                 [1,0,1,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,0,0,1,0,0,0,0,2,1],
                 [1,1,2,0,0,1,0,4,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
          '20': [[1,1,1,1,1,1,1,1,1,1],
                 [1,1,3,0,1,1,1,0,0,1],
                 [1,4,0,0,0,2,1,0,2,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,1,0,1,0,2,1,0,1,1],
                 [1,0,0,0,0,1,1,0,1,1],
                 [1,0,1,0,1,1,0,0,2,1],
                 [1,0,0,0,0,1,0,1,1,1],
                 [1,2,1,0,0,0,0,1,1,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
          '21': [[1,1,1,1,1,1,1,1,1,1],
                 [1,1,4,0,1,1,1,0,0,1],
                 [1,3,0,0,0,0,1,0,2,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,1,0,0,0,0,1,0,1,1],
                 [1,0,0,2,0,1,1,0,1,1],
                 [1,0,1,0,1,1,0,0,2,1],
                 [1,0,0,0,0,1,0,1,1,1],
                 [1,2,1,0,0,0,0,1,1,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
          '22': [[1,1,1,1,1,1,1,1,1,1],
                 [1,1,1,1,1,1,1,1,1,1],
                 [1,1,0,0,0,0,0,3,1,1],
                 [1,1,0,1,1,1,1,0,1,1],
                 [1,1,0,0,0,0,1,0,1,1],
                 [1,1,1,1,1,0,1,0,1,1],
                 [1,2,2,2,1,0,2,0,1,1],
                 [1,2,2,2,1,0,1,1,1,1],
                 [1,2,2,2,1,4,1,2,1,1],
                 [1,1,1,1,1,1,1,1,1,1]],
                            
          '23': [[1,1,1,1,1,1,1,1,1,1],
                 [1,2,0,0,0,1,0,0,2,1],
                 [1,2,0,0,0,0,0,0,1,1],
                 [1,2,0,1,0,0,0,0,2,1],
                 [1,2,3,1,0,0,1,0,2,1],
                 [1,2,0,1,0,0,1,0,2,1],
                 [1,2,0,0,0,0,1,0,2,1],
                 [1,4,0,0,0,0,0,0,2,1],
                 [1,2,0,0,1,0,0,2,2,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
          '24': [[1,1,1,1,1,1,1,1,1,1],
                 [1,1,0,0,0,0,0,0,1,1],
                 [1,0,0,0,0,1,1,0,0,1],
                 [1,1,0,2,0,2,1,1,0,1],
                 [1,0,0,0,3,0,1,1,0,1],
                 [1,0,0,4,0,0,0,2,0,1],
                 [1,0,0,2,0,0,0,1,0,1],
                 [1,0,1,0,1,0,0,0,0,1],
                 [1,0,0,0,0,0,1,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
          '25':  [[1,1,1,1,1,1,1,1,1,1],
                 [1,2,0,0,0,0,0,0,0,1],
                 [1,0,0,4,0,0,0,0,1,1],
                 [1,1,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,1,0,0,3,1],
                 [1,0,2,0,0,0,0,2,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,0,1,0,0,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]], 

            
          '26': [[1,1,1,1,1,1,1,1,1,1],
                 [1,1,1,1,1,1,1,1,1,1],
                 [1,1,3,0,0,1,0,0,1,1],
                 [1,1,0,0,0,0,2,0,1,1],
                 [1,1,0,2,0,0,0,0,1,1],
                 [1,1,0,0,0,0,1,0,1,1],
                 [1,1,0,0,1,0,0,4,1,1],
                 [1,1,0,0,0,1,0,0,1,1],
                 [1,1,1,1,1,1,1,1,1,1],
                 [1,1,1,1,1,1,1,1,1,1]], 
            
          '27': [[1,1,1,1,1,1,1,1,1,1],
                 [1,1,2,0,0,0,0,0,0,1],
                 [1,0,0,0,0,1,2,0,0,1],
                 [1,0,1,0,0,0,0,0,0,1],
                 [1,0,2,0,2,0,2,0,0,1],
                 [1,3,0,0,0,0,1,0,0,1],
                 [1,0,0,0,0,0,0,4,0,1],
                 [1,0,0,1,2,0,0,2,0,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '28': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,1,2,0,0,0,0,1],
                 [1,0,0,0,0,0,1,1,0,1],
                 [1,0,1,1,0,1,0,0,0,1],
                 [1,0,0,0,0,2,0,0,0,1],
                 [1,2,1,0,0,0,0,2,0,1],
                 [1,0,1,3,0,0,0,1,0,1],
                 [1,0,1,1,1,0,1,1,0,1],
                 [1,4,0,0,0,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]], 

          '29': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,1,4,2,2,2,3,0,1],
                 [1,0,0,0,2,1,0,0,0,1],
                 [1,1,0,0,0,0,0,0,0,1],
                 [1,0,0,0,1,0,0,0,0,1],
                 [1,0,0,2,1,0,0,0,0,1],
                 [1,0,1,0,0,0,2,0,1,1],
                 [1,0,0,2,0,1,0,0,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '30': [[1,1,1,1,1,1,1,1,1,1],
                 [1,1,1,1,0,0,1,1,1,1],
                 [1,1,1,0,0,0,0,1,1,1],
                 [1,1,0,0,0,0,0,0,1,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,4,0,0,0,0,0,1,1,1],
                 [1,1,1,0,0,0,1,1,1,1],
                 [1,1,1,1,3,1,1,1,1,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '31': [[1,1,1,1,1,1,1,1,1,1],
                 [1,2,0,0,1,1,0,0,2,1],
                 [1,0,0,1,0,0,0,1,1,1],
                 [1,1,0,0,0,0,0,1,2,1],
                 [1,0,0,0,3,0,0,0,0,1],
                 [1,1,0,0,0,4,0,0,0,1],
                 [1,0,1,0,0,0,0,0,0,1],
                 [1,0,1,0,0,0,0,0,0,1],
                 [1,0,0,0,0,1,1,1,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],


          '32': [[1,1,1,1,1,1,1,1,1,1],
                 [1,4,0,0,0,2,0,0,1,1],
                 [1,0,0,1,0,0,1,0,0,1],
                 [1,2,0,0,0,1,0,0,0,1],
                 [1,1,1,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,0,1,0,0,0,3,0,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,1,0,0,0,0,1,1,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '33': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,1,0,0,1,0,1],
                 [1,1,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,1,0,0,3,0,0,0,0,1],
                 [1,2,0,0,1,0,0,0,0,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,0,1,4,0,1,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '34': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,0,1,0,0,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,3,0,0,1,0,2,0,0,1],
                 [1,0,1,0,0,0,0,4,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,1,0,0,1,1],
                 [1,0,0,1,1,2,0,0,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '35':  [[1,1,1,1,1,1,1,1,1,1],
                 [1,1,0,0,1,1,0,0,0,1],
                 [1,0,0,0,0,0,0,2,2,1],
                 [1,0,3,0,0,0,0,0,0,1],
                 [1,0,0,0,1,0,0,0,0,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,1,0,2,0,0,0,0,2,1],
                 [1,4,0,0,0,0,0,0,0,1],
                 [1,2,0,0,1,1,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

     
          '36': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,1,0,0,1,0,0,1],
                 [1,0,1,0,0,0,1,1,0,1],
                 [1,4,0,0,0,0,0,0,1,1],
                 [1,2,0,3,1,0,1,0,0,1],
                 [1,0,0,0,0,0,2,0,0,1],
                 [1,1,2,0,0,0,0,0,0,1],
                 [1,0,0,1,2,0,0,0,0,1],
                 [1,0,0,0,0,0,1,2,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
          '37': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,2,0,0,0,0,0,1,1],
                 [1,0,0,4,0,0,0,0,0,1],
                 [1,1,0,1,1,0,1,2,0,1],
                 [1,0,0,0,1,0,0,1,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,1,0,0,0,0,1,1],
                 [1,3,0,0,0,0,1,0,0,1],
                 [1,1,0,0,0,0,0,0,2,1],
                 [1,1,1,1,1,1,1,1,1,1]], 
            
          '38': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,1,1,0,0,0,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,0,1,2,0,0,0,0,0,1],
                 [1,0,0,0,0,4,0,0,0,1],
                 [1,0,0,0,3,0,0,0,0,1],
                 [1,1,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,0,1,0,1],
                 [1,0,0,0,0,1,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]], 
            
          '39': [[1,1,1,1,1,1,1,1,1,1],
                 [1,2,1,0,0,0,0,0,0,1],
                 [1,0,0,0,1,0,0,0,0,1],
                 [1,0,0,0,0,1,0,0,0,1],
                 [1,0,0,0,3,0,0,1,0,1],
                 [1,0,0,0,0,0,0,4,0,1],
                 [1,0,0,0,0,0,0,0,2,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,0,1,1,0,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '40': [[1,1,1,1,1,1,1,1,1,1],
                 [1,1,0,1,4,0,0,2,0,1],
                 [1,2,0,0,0,0,0,0,0,1],
                 [1,3,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,1,0,0,0,1],
                 [1,0,1,0,0,0,0,0,0,1],
                 [1,0,0,1,0,0,0,0,0,1],
                 [1,0,0,0,0,0,0,1,0,1],
                 [1,0,0,0,1,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '41': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,2,1,0,0,0,0,0,1],
                 [1,0,0,0,0,0,0,1,0,1],
                 [1,0,0,0,2,0,0,1,0,1],
                 [1,0,0,0,0,2,0,0,0,1],
                 [1,1,0,0,0,0,0,0,0,1],
                 [1,2,0,3,0,0,1,1,0,1],
                 [1,0,0,2,0,0,0,0,0,1],
                 [1,0,0,4,0,2,1,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '42': [[1,1,1,1,1,1,1,1,1,1],
                 [1,1,0,1,0,1,1,0,0,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,0,0,1,0,0,0,0,2,1],
                 [1,0,0,0,4,0,0,0,0,1],
                 [1,2,0,0,0,3,0,0,0,1],
                 [1,0,0,0,0,0,0,1,0,1],
                 [1,1,0,0,0,0,2,0,0,1],
                 [1,0,0,0,1,1,1,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '43': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,1,0,0,0,0,1],
                 [1,0,0,1,0,0,1,0,0,1],
                 [1,0,0,0,0,0,0,4,0,1],
                 [1,0,0,0,0,0,0,2,0,1],
                 [1,0,0,0,3,0,0,0,1,1],
                 [1,0,1,0,0,0,0,0,0,1],
                 [1,0,0,0,0,1,0,0,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '44': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,0,1,0,0,4,1],
                 [1,0,0,0,0,0,0,0,2,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,1,0,0,0,0,1,0,1],
                 [1,0,0,0,1,0,0,0,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,3,0,0,0,0,1,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],
            
          '45':  [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,0,1,0,0,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,0,1,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,3,2,4,0,0,0,1],
                 [1,0,0,0,0,2,1,0,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,1,1,0,0,0,2,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '46': [[1,1,1,1,1,1,1,1,1,1],
                 [1,1,0,0,0,0,0,1,0,1],
                 [1,0,0,0,0,1,0,0,0,1],
                 [1,0,0,0,0,0,0,0,4,1],
                 [1,3,0,0,2,2,2,0,0,1],
                 [1,0,0,1,0,0,0,0,0,1],
                 [1,0,2,0,0,0,0,1,0,1],
                 [1,0,0,0,0,2,0,0,0,1],
                 [1,0,0,0,1,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '47': [[1,1,1,1,1,1,1,1,1,1],
                 [1,2,2,4,2,2,2,2,2,1],
                 [1,1,1,0,0,0,1,0,2,1],
                 [1,0,0,0,0,1,0,0,2,1],
                 [1,3,0,0,0,0,0,1,2,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,2,0,0,1,0,2,0,2,1],
                 [1,2,1,0,0,0,0,0,2,1],
                 [1,2,2,2,2,2,2,1,2,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '48': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,0,0,1,0,4,1],
                 [1,0,0,0,0,0,0,0,2,1],
                 [1,0,0,0,1,0,0,0,0,1],
                 [1,0,0,1,0,0,0,0,1,1],
                 [1,0,1,0,0,0,0,1,0,1],
                 [1,1,0,0,0,1,0,0,0,1],
                 [1,0,0,0,1,0,0,0,0,1],
                 [1,3,0,1,0,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '49': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,1,4,0,2,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,1,0,0,1],
                 [1,0,1,0,0,0,0,0,0,1],
                 [1,0,0,0,3,0,0,0,0,1],
                 [1,0,0,0,0,0,0,1,0,1],
                 [1,0,0,0,1,0,0,0,0,1],
                 [1,2,1,0,0,0,1,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '50': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,2,1,0,0,0,0,0,1],
                 [1,0,0,0,0,0,0,3,0,1],
                 [1,0,4,1,0,1,0,0,0,1],
                 [1,0,0,1,0,0,0,1,0,1],
                 [1,0,0,1,0,0,0,0,1,1],
                 [1,2,0,1,1,2,0,0,2,1],
                 [1,1,0,0,0,0,0,0,0,1],
                 [1,0,0,1,2,0,0,1,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '51': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,0,1,1,1,1,0,0,2,1],
                 [1,0,1,3,0,1,1,0,0,1],
                 [1,0,1,1,0,1,0,0,4,1],
                 [1,0,0,0,0,1,0,0,2,1],
                 [1,0,1,1,1,1,0,0,0,1],
                 [1,0,0,0,0,2,0,0,0,1],
                 [1,0,0,0,0,0,0,1,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '52': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,2,0,0,0,0,0,0,1],
                 [1,1,2,0,1,1,0,0,0,1],
                 [1,0,0,0,1,1,2,0,0,1],
                 [1,0,1,1,1,1,1,1,0,1],
                 [1,0,1,1,1,1,1,1,0,1],
                 [1,0,2,0,1,1,4,0,0,1],
                 [1,0,0,0,1,1,0,2,1,1],
                 [1,3,0,0,0,0,0,2,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '53': [[1,1,1,1,1,1,1,1,1,1],
                 [1,2,1,0,0,0,0,1,2,1],
                 [1,0,1,0,0,3,0,0,1,1],
                 [1,0,0,1,0,0,0,0,1,1],
                 [1,0,1,0,0,0,0,1,0,1],
                 [1,0,4,0,0,0,0,0,1,1],
                 [1,0,0,1,0,0,0,0,1,1],
                 [1,0,2,0,1,0,0,1,0,1],
                 [1,0,0,0,0,0,0,2,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '54': [[1,1,1,1,1,1,1,1,1,1],
                 [1,3,0,0,0,0,0,0,0,1],
                 [1,0,1,0,0,2,0,0,0,1],
                 [1,0,0,0,0,0,0,1,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,4,0,0,0,0,0,1],
                 [1,0,0,0,0,0,1,0,0,1],
                 [1,1,0,0,0,0,2,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '55':  [[1,1,1,1,1,1,1,1,1,1],
                 [1,2,1,1,1,0,0,0,0,1],
                 [1,0,0,0,0,0,1,1,0,1],
                 [1,0,1,0,1,0,1,1,1,1],
                 [1,0,1,3,1,0,1,0,0,1],
                 [1,0,0,1,0,0,0,0,1,1],
                 [1,1,1,4,1,1,1,0,1,1],
                 [1,1,1,0,1,1,1,0,1,1],
                 [1,1,1,0,0,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '56': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,1,0,0,1,0,0,1],
                 [1,0,1,4,0,0,0,0,0,1],
                 [1,2,0,0,0,0,0,1,0,1],
                 [1,1,0,0,0,0,0,0,2,1],
                 [1,0,0,0,0,0,0,0,1,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,3,0,0,0,1,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '57': [[1,1,1,1,1,1,1,1,1,1],
                 [1,2,1,2,1,2,1,2,1,1],
                 [1,3,0,0,1,0,0,0,0,1],
                 [1,0,1,0,0,0,0,1,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,0,0,0,1],
                 [1,0,0,0,0,0,0,4,0,1],
                 [1,0,0,0,0,1,0,0,1,1],
                 [1,1,2,1,2,1,2,1,2,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '58': [[1,1,1,1,1,1,1,1,1,1],
                 [1,0,0,0,0,0,0,1,0,1],
                 [1,0,2,1,0,0,0,2,0,1],
                 [1,0,0,3,0,0,0,0,0,1],
                 [1,1,0,0,0,0,0,0,0,1],
                 [1,0,0,1,0,0,0,0,1,1],
                 [1,0,0,4,0,1,0,0,0,1],
                 [1,0,2,0,0,0,1,2,0,1],
                 [1,0,1,0,0,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '59': [[1,1,1,1,1,1,1,1,1,1],
                 [1,3,0,0,0,0,0,1,2,1],
                 [1,2,2,2,2,2,0,2,0,1],
                 [1,2,4,2,2,2,0,2,0,1],
                 [1,2,0,2,0,0,0,0,0,1],
                 [1,2,0,2,2,2,1,2,0,1],
                 [1,2,0,1,0,0,0,0,0,1],
                 [1,2,0,2,0,2,2,2,1,1],
                 [1,1,0,0,0,0,0,0,2,1],
                 [1,1,1,1,1,1,1,1,1,1]],

          '60': [[1,1,1,1,1,1,1,1,1,1],
                 [1,1,0,0,1,1,0,0,0,1],
                 [1,2,0,3,1,0,0,1,0,1],
                 [1,0,0,0,0,0,1,1,0,1],
                 [1,0,1,0,0,1,1,0,0,1],
                 [1,0,0,1,1,1,0,0,1,1],
                 [1,1,0,2,1,0,0,1,1,1],
                 [1,2,0,0,4,0,1,1,1,1],
                 [1,2,1,2,1,1,1,1,1,1],
                 [1,1,1,1,1,1,1,1,1,1]]
                 }
LEVELS_IN_ORDER={ '1':LEVELS['3'], 
                  '2':LEVELS['7'],  
                  '3':LEVELS['4'],  
                  '4':LEVELS['22'],  
                  '5':LEVELS['11'],  
                  '6':LEVELS['26'],  
                  '7':LEVELS['6'],  
                  '8':LEVELS['20'],  
                  '9':LEVELS['14'],  
                  '10':LEVELS['21'],  
                  '11':LEVELS['52'],  
                  '12':LEVELS['9'],  
                  '13':LEVELS['55'],  
                  '14':LEVELS['12'],  
                  '15':LEVELS['17'],  
                  '16':LEVELS['23'],  
                  '17':LEVELS['28'],  
                  '18':LEVELS['59'],  
                  '19':LEVELS['8'],  
                  '20':LEVELS['16'],   
                  '21':LEVELS['15'],   
                  '22':LEVELS['5'],   
                  '23':LEVELS['10'],   
                  '24':LEVELS['19'],   
                  '25':LEVELS['51'],   
                  '26':LEVELS['29'],   
                  '27':LEVELS['60'],   
                  '28':LEVELS['32'],   
                  '29':LEVELS['36'],   
                  '30':LEVELS['44'],   
                  '31':LEVELS['49'],   
                  '32':LEVELS['45'],   
                  '33':LEVELS['30'],   
                  '34':LEVELS['53'],   
                  '35':LEVELS['1'],   
                  '36':LEVELS['46'],   
                  '37':LEVELS['35'],   
                  '38':LEVELS['40'],   
                  '39':LEVELS['37'],   
                  '40':LEVELS['33'],   
                  '41':LEVELS['13'],   
                  '42':LEVELS['57'],   
                  '43':LEVELS['43'],   
                  '44':LEVELS['56'],   
                  '45':LEVELS['58'],   
                  '46':LEVELS['25'],   
                  '47':LEVELS['50'],   
                  '48':LEVELS['2']}