from gi.repository import Gtk, GdkPixbuf
from opendrop.development_app.bases.GtkView import GtkView
from opendrop.development_app.iviews.ICameraView import ICameraView
import cv2

class CameraView(GtkView, ICameraView):
    def setup(self) -> None:
        self.window.set_border_width(10)
        self.window.set_default_size(500, 500)



        self.window.show_all()