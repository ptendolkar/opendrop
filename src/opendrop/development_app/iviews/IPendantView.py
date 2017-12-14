from abc import abstractmethod

from opendrop.mvp.IView import IView

from opendrop.development_app.bases.IMaximizable import IMaximizable


class IPendantView(IView, IMaximizable):
    @abstractmethod
    def on_contact_button_clicked(self):
        pass