from typing import Any
from opendrop.development_app.about.AboutView import AboutView
from opendrop.development_app.camera_sample.CameraView import CameraView
from opendrop.development_app.iviews.IMainView import IMainView
from opendrop.development_app.help.HelpView import HelpView
from opendrop.mvp import handles
from opendrop.mvp.Presenter import Presenter
from opendrop.development_app.Main.MainView import MainView
from gi.repository import Gtk
import cv2

class MainPresenter(Presenter[Any, IMainView]):
    @handles('on_about_button_clicked')
    def handle_about_button_clicked(self):
        print("Open about dialog")
        self.view.show_about_dialog()

    @handles('on_help_button_clicked')
    def handle_help_button_clicked(self):
        print("Open help window")
        self.view.close(next_view=HelpView)

    @handles('on_settings_button_clicked')
    def handle_settings_button_clicked(self):
        print("settings button clicked")

    @handles('on_contact_button_clicked')
    def handle_contact_button_clicked(self):
        print("Contact button clicked")

    @handles('on_pendant_button_clicked')
    def handle_pendant_button_clicked(self):
        try:
            dialog = PopUp(self)
            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                print("You clicked OKAY")
            elif response == Gtk.ResponseType.CANCEL:
                print("You clicked CANCEL")
            dialog.destroy()
        except:
            print("Error in MainPresenter (on_pendant_button_clicked)")

    @handles('on_camera_button_clicked')
    def handle_camera_button_clicked(self):
        try:
            cap = cv2.VideoCapture(0)
            while (True):
                # Capture frame-by-frame
                ret, frame = cap.read()
                # Our operations on the frame come here
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                # Display the resulting frame
                cv2.imshow('frame', gray)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            # When everything done, release the capture
            cap.release()
            cv2.destroyAllWindows()
            self.view.close(next_view=CameraView)
        except:
            print("Error in MainPresenter (on_camera_button_clicked)")


class PopUp(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self,"Pop-up Title", parent, Gtk.DialogFlags.MODAL, (
            "Custom cancel text", Gtk.ResponseType.CANCEL,
            Gtk.STOCK_OK, Gtk.ResponseType.OK
        ))
        self.set_default_size(100,100)

        area = self.get_content_area()
        area.add(Gtk.Label("This is a pop up"))
        self.show_all()