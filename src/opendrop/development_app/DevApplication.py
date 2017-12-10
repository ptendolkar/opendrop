from opendrop.development_app.about.AboutView import AboutView
from opendrop.development_app.DevModel import DevModel
from opendrop.development_app.Main.MainPresenter import MainPresenter
from opendrop.development_app.Main.MainView import MainView
from opendrop.development_app.bases.GtkApplication import GtkApplication


class DevApplication(GtkApplication):
    APPLICATION_ID = 'org.example.development_app'

    MODEL = DevModel
    VIEWS = [MainView, AboutView]
    PRESENTERS = [MainPresenter]

    ENTRY_VIEW = MainView