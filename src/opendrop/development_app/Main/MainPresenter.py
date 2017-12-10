from typing import Any

from opendrop.development_app.about.AboutView import AboutView
from opendrop.development_app.camera_sample.CameraView import CameraView
from opendrop.development_app.iviews.IMainView import IMainView
from opendrop.mvp import handles
from opendrop.mvp.Presenter import Presenter


class MainPresenter(Presenter[Any, IMainView]):
    @handles('on_about_button_clicked')
    def handle_about_button_clicked(self):
        self.view.close(next_view=AboutView)

    @handles('on_help_button_clicked')
    def handle_help_button_clicked(self):
        pass

    @handles('on_settings_button_clicked')
    def handle_settings_button_clicked(self):
        pass

    @handles('on_contact_button_clicked')
    def handle_contact_button_clicked(self):
        pass

    @handles('on_pendant_button_clicked')
    def handle_pendant_button_clicked(self):
        pass

    @handles('on_camera_button_clicked')
    def handle_camera_button_clicked(self):
        self.view.close(next_view=CameraView)