from gi.repository import Gtk

from opendrop.development_app.bases.GtkView import GtkView
from opendrop.development_app.iviews.IAboutView import IAboutView


class AboutView(GtkView, IAboutView):
    def setup(self) -> None:
        self.window.set_default_size(500, 500)

        layout = Gtk.Grid()
        layout.set_border_width(10)

        header_box = Gtk.Box()
        header = Gtk.Label()
        header.set_markup("<u><big>About</big></u>")
        header_box.add(header)

        about_info_box = Gtk.Box()
        about_info = Gtk.Label("Information about OpenDrop can go here")
        about_info.set_line_wrap(True)
        about_info.set_justify(Gtk.Justification.FILL)
        about_info_box.add(about_info)

        layout.attach(header_box, 0, 0, 1, 1)
        layout.attach_next_to(about_info_box, header_box, Gtk.PositionType.BOTTOM, 1, 1)

        self.window.add(layout)
        self.window.show_all()

