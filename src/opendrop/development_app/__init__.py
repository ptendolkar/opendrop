import sys

import gi

gi.require_version('Gtk', '3.0')

from opendrop.development_app.DevApplication import DevApplication


def main() -> None:
    app = DevApplication()
    app.run(sys.argv)

    print("Done.")


if __name__ == "__main__":
    main()