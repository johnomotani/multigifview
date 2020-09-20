from pathlib import Path

from mainwindow import Ui_MainWindow
from Qt.QtWidgets import QMainWindow, QLabel
from Qt.QtGui import QMovie


class MultiGifView(QMainWindow, Ui_MainWindow):
    """A program for viewing .gif files"""

    def __init__(self, args):
        super().__init__(None)
        self.setupUi(self)

        def set_clicked(widget, function):
            widget.clicked.connect(function)
            if hasattr(function, "__doc__"):
                widget.setToolTip(function.__doc__.strip())

        set_clicked(self.play_button, self.play_action)
        set_clicked(self.previous_button, self.previous_action)
        set_clicked(self.next_button, self.next_action)

        filepath = Path(args[1])
        self.movie = QMovie(str(filepath))
        self.movie.setCacheMode(QMovie.CacheAll)
        self.gif_widget.setMovie(self.movie)
        self.movie.jumpToFrame(0)

        self.extra_movies = []
        self.extra_gif_widgets = []
        for i, arg in enumerate(args[2:]):
            gif_widget = QLabel(self.centralwidget)
            gif_widget.setText("")
            gif_widget.setObjectName(f"gif_widget{i + 1}")

            filepath = Path(arg)
            movie = QMovie(str(filepath))
            movie.setCacheMode(QMovie.CacheAll)
            gif_widget.setMovie(movie)
            movie.jumpToFrame(0)

            if i%2 == 0:
                # add to right column (arg[1] was in left column)
                position = self.right_column.count() - 1
                self.right_column.insertWidget(position, gif_widget)
            else:
                # add to left column
                position = self.left_column.count() - 1
                self.left_column.insertWidget(position, gif_widget)

            self.extra_movies.append(movie)
            self.extra_gif_widgets.append(gif_widget)

    def play_action(self):
        """Play the gif

        """
        if self.movie.state() == QMovie.Running:
            self.movie.setPaused(True)
        elif self.movie.state() == QMovie.Paused:
            self.movie.setPaused(False)
        else:
            self.movie.start()

    def previous_action(self):
        """Back one frame

        """
        self.movie.jumpToFrame(
            (self.movie.currentFrameNumber() - 1) % self.movie.frameCount()
        )

    def next_action(self):
        """Forward one frame

        """
        self.movie.jumpToNextFrame()
