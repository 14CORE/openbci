
from PyQt4 import QtGui, QtCore
import ugm_config_manager

class UgmStimulusFactory(object):
    #TODO - create a cool list with factories for every stimulus
    def createStimulus(self, p_parent, p_stim_config):
        l_stim = p_stim_config['stimulus_type']
        if l_stim == 'rectangle':
            return UgmRectStimulus(p_parent, p_stim_config)
        elif l_stim == 'cross':
            return UgmCrossStimulus(p_parent, p_stim_config)
        elif l_stim == 'image':
            return UgmImageStimulus(p_parent, p_stim_config)
        elif l_stim == 'text':
            return UgmTextStimulus(p_parent, p_stim_config)
        elif l_stim == 'diode':
            return UgmDiodeStimulus(p_parent, p_stim_config)

class UgmStimulus(QtGui.QWidget):
    def __init__(self, p_parent, p_config_dict):
        QtGui.QWidget.__init__(self, p_parent)
        self._ugm_id = p_config_dict['id']
        self._update_geometry_from_config(p_config_dict)

        l_stims_factory = UgmStimulusFactory()
        for i_stim_config in p_config_dict['stimuluses']:
            l_stims_factory.createStimulus(self, i_stim_config)


    def update_geometry(self):
        """Called from resize event."""
        l_config = self.get_config_manager().get_config_for(self._ugm_id)
        self._update_geometry_from_config(l_config)
        for i in self.children():
            i.update_geometry()
    def _update_geometry_from_config(self, p_config):
        self._set_config(self.parent(), p_config)
        # Below I must call the method every time, as we need to
        # refresh stimuli after refreshing UgmField
        self.setGeometry(self.position_x, self.position_y,
                         self.position_x + self.width,
                         self.position_y + self.height)
#        self.setGeometry(0, 0, self.parent().width, self.parent().height)
        self.update()

    def get_config_manager(self):
        return self.parent().get_config_manager()

class UgmImageStimulus(UgmStimulus, ugm_config_manager.UgmRectConfig):
    # TODO - teraz podaje sie width i height, na tej podstawie liczy sie position ... pewnie na razie width i height powinny sie brac z obrazka i juz ...
    def _set_config(self, p_parent, p_config_dict):
        #TODO - set default config values
        self._image_path = p_config_dict['image_path']
        self._image = QtGui.QImage(QtCore.QString(self._image_path))
        # By now we get image`s size from the image
        p_config_dict['width_type'] = 'absolute'
        p_config_dict['height_type'] = 'absolute'
        p_config_dict['width'] = self._image.size().width()
        p_config_dict['height'] = self._image.size().height()
        self._set_rect_config(p_parent, p_config_dict)

    def paintEvent(self, event):
        paint = QtGui.QPainter()
        paint.begin(self)
        paint.drawImage(0, 0, self._image)
        paint.end()
        
class UgmTextStimulus(UgmStimulus, ugm_config_manager.UgmRectConfig):
    def _set_config(self, p_parent, p_config_dict):
        self._font = QtGui.QFont()
        self._font.setFamily(p_config_dict['font_family'])
        self._font.setPointSize(p_config_dict['font_size'])
        self._color = p_config_dict['font_color']
        self._message = p_config_dict['message']

        l_font_metrics = QtGui.QFontMetrics(self._font)
        p_config_dict['width_type'] = 'absolute'
        p_config_dict['height_type'] = 'absolute'
        p_config_dict['width'] = l_font_metrics.width(self._message)
        p_config_dict['height'] = p_config_dict['font_size']#l_font_metrics.height() #TODO - na pewno tak?
        self._set_rect_config(p_parent, p_config_dict)
        
    def paintEvent(self, event):
        paint = QtGui.QPainter()
        paint.begin(self)
        l_color = QtGui.QColor(0, 0, 0)
        l_color.setNamedColor(self._color)
    	paint.setPen(l_color)
        paint.setFont(self._font)
        paint.drawText(0, self.height, self._message)
        paint.end()
    #TODO
    pass
class UgmRectStimulus(UgmStimulus, ugm_config_manager.UgmRectConfig):
    def _set_config(self, p_parent, p_config_dict):
        #TODO - set default config values
        self._set_rect_config(p_parent, p_config_dict)

    def paintEvent(self, event):
        paint = QtGui.QPainter()
        paint.begin(self)
        l_bg_color = QtGui.QColor(0, 0, 0)
        l_bg_color.setNamedColor(self.color)
        paint.setBrush(l_bg_color)
        
        paint.drawRect(0, 0, self.width, self.height)
        paint.end()

"""import virtual_diode_stimulus
class UgmDiodeStimulus(UgmStimulus, ugm_config_manager.UgmRectConfig):
    def _set_config(self, p_parent, p_config_dict):
        #TODO - set default config values
        self._set_rect_config(p_parent, p_config_dict)
        self.freq = p_config_dict['freq']

    def paintEvent(self, event):
        l_geom = self._get_absolute_geometry()
        virtual_diode_stimulus.show_diode_in_thread(self._ugm_id, l_geom, self.width, self.height, self.freq)

    def _get_absolute_geometry(self):
        l_parent = self.parent()
        l_geom = [self.geometry().x(), self.geometry().y()]
        while l_parent:
            l_new_geom = l_parent.geometry()
            l_geom[0] = l_geom[0] + l_new_geom.x()
            l_geom[1] = l_geom[1] + l_new_geom.y()
            l_parent = l_parent.parent()
        return l_geom"""
            
            
    
