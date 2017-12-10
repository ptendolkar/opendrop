
from opendrop.development_app.iviews import ICameraView
from opendrop.mvp.Presenter import Presenter
from opendrop.development_app import DevModel

class CameraPresenter(Presenter[DevModel, ICameraView]):
    def setup(self) -> None:
        pass
