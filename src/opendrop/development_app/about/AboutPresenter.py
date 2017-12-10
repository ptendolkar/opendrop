from opendrop.development_app import DevModel
from opendrop.development_app.iviews import IAboutView
from opendrop.mvp.Presenter import Presenter


class AboutPresenter(Presenter[DevModel, IAboutView]):
    def setup(self) -> None:
        pass
