from gi.repository import Gtk

from opendrop.development_app.bases.GtkView import GtkView
from opendrop.development_app.iviews.IPendantView import IPendantView


class PendantView(GtkView, IPendantView):
    def setup(self) -> None:
        self.window.set_default_size(500, 500)
        self.window.show_all()

