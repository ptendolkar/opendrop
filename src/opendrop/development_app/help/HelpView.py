from gi.repository import Gtk

from opendrop.development_app.bases.GtkView import GtkView
from opendrop.development_app.iviews.IHelpView import IHelpView


class HelpView(GtkView, IHelpView):
    def setup(self) -> None:
        # -- Build the UI --
        grid = Gtk.Grid(margin=10, column_spacing=10, row_spacing=10)
        self.window.set_default_size(500, 500)
        self.window.add(grid)

        # Title
        help_title = Gtk.Label()
        help_title.set_markup("<u><big>Help</big></u>")

        # Basic instructions
        instructions = Gtk.Label()
        instructions.set_markup(
            "select either pendant drop or contact angle. "
        )
        instructions.set_line_wrap(True)


        grid.attach(help_title, 0, 0, 1, 1)
        grid.attach_next_to(instructions, help_title, Gtk.PositionType.BOTTOM, 1, 1)
        self.window.show_all()
        # Create info box
