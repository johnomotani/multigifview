#!/usr/bin/env python3

from Qt.QtWidgets import QApplication
import sys

from core import MultiGifView


def main():
    """Simple gif viewer"""
    app = QApplication(sys.argv)
    window = MultiGifView(sys.argv)
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
