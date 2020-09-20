from pathlib import Path

from mainwindow import Ui_MainWindow
from Qt.QtWidgets import QApplication, QMainWindow, QLabel, QShortcut
from Qt.QtGui import QMovie, QKeySequence


class MultiGifView(QMainWindow, Ui_MainWindow):
    """A program for viewing .gif files"""

    def __init__(self, filenames):
        super().__init__(None)
        self.setupUi(self)

        # extra keyboard shortcuts
        quit_shortcut = QShortcut(QKeySequence("Q"), self)
        quit_shortcut.activated.connect(QApplication.instance().quit)
        quit_shortcut = QShortcut(QKeySequence("Ctrl+Q"), self)
        quit_shortcut.activated.connect(QApplication.instance().quit)
        quit_shortcut = QShortcut(QKeySequence("Ctrl+X"), self)
        quit_shortcut.activated.connect(QApplication.instance().quit)
        quit_shortcut = QShortcut(QKeySequence("Ctrl+W"), self)
        quit_shortcut.activated.connect(QApplication.instance().quit)
        next_shortcut = QShortcut(QKeySequence("left"), self)
        next_shortcut.activated.connect(self.previous_action)
        next_shortcut = QShortcut(QKeySequence("right"), self)
        next_shortcut.activated.connect(self.next_action)

        def set_clicked(widget, function):
            widget.clicked.connect(function)
            if hasattr(function, "__doc__"):
                widget.setToolTip(function.__doc__.strip())

        set_clicked(self.play_button, self.play_action)
        set_clicked(self.previous_button, self.previous_action)
        set_clicked(self.next_button, self.next_action)

        filepath = Path(filenames[0])
        self.movie = QMovie(str(filepath))
        self.movie.setCacheMode(QMovie.CacheAll)
        self.gif_widget.setMovie(self.movie)
        self.movie.jumpToFrame(0)

        self.extra_movies = []
        self.extra_gif_widgets = []
        for i, arg in enumerate(filenames[1:]):
            gif_widget = QLabel(self.centralwidget)
            gif_widget.setText("")
            gif_widget.setObjectName(f"gif_widget{i + 1}")

            filepath = Path(arg)
            movie = QMovie(str(filepath))
            movie.setCacheMode(QMovie.CacheAll)
            gif_widget.setMovie(movie)
            movie.jumpToFrame(0)

            if i % 2 == 0:
                # add to right column (filenames[0] was in left column)
                position = self.right_column.count() - 1
                self.right_column.insertWidget(position, gif_widget)
            else:
                # add to left column
                position = self.left_column.count() - 1
                self.left_column.insertWidget(position, gif_widget)

            self.extra_movies.append(movie)
            self.extra_gif_widgets.append(gif_widget)

        # want the longest-running gif to be the one that's directly controlled, so that
        # it can play all the way to the end, not have to stop when self.movie reaches
        # its last frame
        for i, movie in enumerate(self.extra_movies):
            if movie.frameCount() > self.movie.frameCount():
                self.extra_movies[i] = self.movie
                self.movie = movie

        # Create actions so extra movies follow self.movie
        self.movie.frameChanged.connect(self.change_frames)

    def play_action(self):
        """Play the gif"""
        if self.movie.state() == QMovie.Running:
            self.movie.setPaused(True)
        elif self.movie.state() == QMovie.Paused:
            self.movie.setPaused(False)
        else:
            self.movie.start()

    def previous_action(self):
        """Back one frame"""
        self.movie.jumpToFrame(
            (self.movie.currentFrameNumber() - 1) % self.movie.frameCount()
        )

    def next_action(self):
        """Forward one frame"""
        self.movie.jumpToNextFrame()

    def change_frames(self, new_frame):
        """Change all the frames in step"""
        for movie in self.extra_movies:
            movie.jumpToFrame(new_frame)
