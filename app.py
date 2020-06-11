import sys
from PyQt5.QtWidgets import QApplication

from howl.controller import Manager
from howl.view import WindowManager


# Client
def main():
    # QApplication instance
    howl = QApplication(sys.argv)

    # Show main window
    view = WindowManager()
    view.show()

    # Set view in the controller
    Manager(view=view, application=howl)

    # Main loop
    sys.exit(howl.exec())


if __name__ == '__main__':
    main()