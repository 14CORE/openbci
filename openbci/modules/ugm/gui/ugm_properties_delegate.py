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
"""Delegate for UGM properties list view - creates editors for different
properties"""

from PyQt4 import QtCore, QtGui

class UGMPropertiesDelegate(QtGui.QItemDelegate):
    """Delegate for UGM properties list view - creates editors for different
    properties"""
    
    def createEditor(self, parent, option, index):
        """Creates editor for given item, depending on its type"""
        l_item = self.getItem(index)
        l_type = l_item.type
        l_typeParameters = l_item.typeParameters
        
        # TODO: Currently thins are depended on enumerated editors, so only those
        # changes are effective immediately. Ultimately, it should be checked,
        # whether something depends on given thing
        if l_type == 'int':
            editor = QtGui.QSpinBox(parent)
            editor.setSingleStep(1)
            editor.setMaximum(1000)
            #self.connect(editor, QtCore.SIGNAL('valueChanged(int)'), self.editorValueChanged)
        elif l_type == 'float':
            editor = QtGui.QDoubleSpinBox(parent)
            editor.setSingleStep(0.05)
            editor.setMaximum(1000)   
            #self.connect(editor, QtCore.SIGNAL('valueChanged(double)'), self.editorValueChanged)
        elif l_type == 'string':
            editor = QtGui.QLineEdit(parent)
            #self.connect(editor, QtCore.SIGNAL('textChanged(QString)'), self.editorValueChanged)
        elif l_type == 'enumerated':
            editor = QtGui.QComboBox(parent)
            for i_value in l_typeParameters['values']:
                editor.addItem(i_value)
            self.connect(editor, QtCore.SIGNAL('currentIndexChanged(int)'), self.editorValueChanged)
        else:
            editor = None
        
        return editor
    
    def setEditorData(self, editor, index):
        """Sets data for editor of given item"""
        l_value = index.model().data(index, QtCore.Qt.EditRole)
        l_item = self.getItem(index)
        l_type = l_item.type
        
        if l_type == 'int' or l_type == 'float':
            editor.setValue(l_value)
        elif l_type == 'string':
            editor.setText(QtCore.QString(str(l_value)))
        elif l_type == 'enumerated':
            editor.setCurrentIndex(editor.findText(l_value))
    
    def setModelData(self, p_editor, model, index):
        """Saves data entered into editor of given item, into the model"""
        l_item = self.getItem(index)
        l_type = l_item.type
        
        if l_type == 'int' or l_type == 'float':
            p_editor.interpretText()
            l_value = p_editor.value()
        elif l_type == 'string':
            l_value = str(p_editor.text())
        elif l_type == 'enumerated':
            l_value = str(p_editor.currentText())
        else:
            return
        
        model.setData(index, l_value, QtCore.Qt.EditRole)
    
    def editorValueChanged(self):
        """Emits signal to commit data of current editor to model.
        Because some fields are dependent on others we want to do it as soon
        as value changes"""
        self.emit(QtCore.SIGNAL('commitData(QWidget *)'), self.sender())
    
    def updateEditorGeometry(self, editor, option, index):
        """Sets editors geometry to rect"""
        editor.setGeometry(option.rect)
    
    def getItem(self, index):
        """Returns item, that is pointed by given QModelIndex."""
        if index.isValid():
            item = index.internalPointer()
            if item:
                return item
        # Index is invalid - that happens for top level element
        return self.rootItem
