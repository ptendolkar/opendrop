from gi.repository import Gtk

from opendrop.development_app.bases.GtkView import GtkView
from opendrop.development_app.iviews.IMainView import IMainView


class MainView(GtkView, IMainView):
    def setup(self) -> None:
        # -- Build the UI --
        grid = Gtk.Grid(margin=10, column_spacing=10, row_spacing=10)
        self.window.add(grid)

        # Logo
        logo = Gtk.Image()
        logo.set_from_file("../resources/images/logo.png")

        # Generic Buttons
        about_button = Gtk.Button("About")
        help_button = Gtk.Button("Help")
        camera_button = Gtk.Button("Camera Test")
        setting_button = Gtk.Button("Settings")

        # Pendant Button
        pendant_box = Gtk.VBox()
        pendant_title = Gtk.Label("Pendant Drop")
        pendant_image = Gtk.Image()
        pendant_image.set_from_file("../resources/images/pendant.png")
        pendant_button = Gtk.Button()
        pendant_box.add(pendant_title)
        pendant_box.add(pendant_image)
        pendant_button.add(pendant_box)


        # Contact Button
        contact_box = Gtk.VBox()
        contact_title = Gtk.Label("Contact Angle")
        contact_image = Gtk.Image()
        contact_image.set_from_file("../resources/images/contact.png")
        contact_button = Gtk.Button()
        contact_box.add(contact_title)
        contact_box.add(contact_image)
        contact_button.add(contact_box)

        # Headers
        measurement_title = Gtk.Label("Measurements:")
        camera_title = Gtk.Label("Select Camera Type: ")


        # Boxes
        measurement_box = Gtk.VBox()
        measurement_grid = Gtk.Grid()
        measurement_grid.attach(measurement_title, 0, 0, 1, 1)
        measurement_grid.attach_next_to(pendant_button, measurement_title, Gtk.PositionType.BOTTOM, 1, 1)
        measurement_grid.attach_next_to(contact_button, pendant_button, Gtk.PositionType.BOTTOM, 1, 1)
        measurement_box.add(measurement_grid)

        camera_options_box = Gtk.VBox()
        camera_options_box.add(camera_title)

        # Camera selector (Stack switcher)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        camera_options_box.add(box)

        main_area = Gtk.Stack()
        main_area.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        main_area.set_transition_duration(2000)

        flea3 = Gtk.Label("")
        main_area.add_titled(flea3, "flea3", "Flea3")

        usb = Gtk.Label("")
        main_area.add_titled(usb, "usb", "USB")

        local_image = Gtk.Label("")
        main_area.add_titled(local_image, "local_image", "Local Image")

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(main_area)

        box.pack_start(stack_switcher, True, True, 0)
        box.pack_start(main_area, True, True, 0)


        # Events
        about_button.event_name = "on_about_button_clicked"
        help_button.event_name = "on_help_button_clicked"
        setting_button.event_name = "on_settings_button_clicked"
        pendant_button.event_name = "on_pendant_button_clicked"
        contact_button.event_name = "on_contact_button_clicked"
        camera_button.event_name = "on_camera_button_clicked"

        # -- Attach events --
        for button in (about_button,
                       setting_button,
                       help_button,
                       pendant_button,
                       contact_button,
                       camera_button):
            button.connect('clicked', self.on_buttonx_clicked)


        # UI setup
        grid.attach(logo, 0, 0, 1, 1)
        grid.attach_next_to(about_button, logo, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(help_button, about_button, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(measurement_box, logo, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(camera_options_box, measurement_box, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(setting_button, help_button, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(camera_button, setting_button, Gtk.PositionType.BOTTOM, 1, 1)
        self.window.show_all()



    # Fires event
    def on_buttonx_clicked(self, button: Gtk.Button) -> None:
        self.fire(button.event_name)
