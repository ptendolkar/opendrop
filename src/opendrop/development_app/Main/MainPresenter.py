from typing import Any
from opendrop.development_app.about.AboutView import AboutView
from opendrop.development_app.camera_sample.CameraView import CameraView
from opendrop.development_app.iviews.IMainView import IMainView
from opendrop.mvp import handles
from opendrop.mvp.Presenter import Presenter
from gi.repository import Gtk


class MainPresenter(Presenter[Any, IMainView]):
    @handles('on_about_button_clicked')
    def handle_about_button_clicked(self):
        self.view.show_about_dialog()

    @handles('on_help_button_clicked')
    def handle_help_button_clicked(self):
        print("help button clicked")

    @handles('on_settings_button_clicked')
    def handle_settings_button_clicked(self):
        print("settings button clicked")

    @handles('on_contact_button_clicked')
    def handle_contact_button_clicked(self):
        print("Contact button clicked")

    @handles('on_pendant_button_clicked')
    def handle_pendant_button_clicked(self):
        dialog = PopUp(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("You clicked OKAY")
        elif response == Gtk.ResponseType.CANCEL:
            print("You clicked CANCEL")
        dialog.destroy()

    @handles('on_camera_button_clicked')
    def handle_camera_button_clicked(self):
        self.view.close(next_view=CameraView)



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