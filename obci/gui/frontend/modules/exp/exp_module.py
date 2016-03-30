# -*- coding: utf-8 -*-
#!/usr/bin/env python
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
#      Łukasz Polak <l.polak@gmail.com>
#
"""Module file for experiment configuration"""

#from ugm.ugm_config_manager import UgmConfigManager
from modules.exp.exp_module_dock_widget import EXPModuleDockWidget

class ExpModule(object):
    """Module file for EXP. Creates and manages its configuration GUI"""

    #name of this module, that will be shown in GUI
    name = "Konfiguracja eksperymentu"
    
    def __init__(self): 
        self.dockWidget = None
        #self.ugmConfigManager = UgmConfigManager()
    
    def buildGui(self, p_parent):
        """Return configuration GUI in form of dock widget"""
        if self.dockWidget == None:
            self.dockWidget = EXPModuleDockWidget(p_parent)
        return self.dockWidget
    
