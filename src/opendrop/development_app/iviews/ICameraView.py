from abc import abstractmethod

from opendrop.mvp.IView import IView

from opendrop.development_app.bases.IMaximizable import IMaximizable


class ICameraView(IView, IMaximizable):
    @abstractmethod
    def show_about_dialog(self): pass