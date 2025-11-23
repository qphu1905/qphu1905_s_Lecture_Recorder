import sys

from PySide6.QtCore import Qt, QRect, QPropertyAnimation, QEasingCurve
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QMainWindow


class ModeSelector(QWidget):
    def __init__(self, app_controller=None):
        super().__init__()
        self.app_controller = app_controller

        self.current_mode = app_controller.current_mode  #0 = Record, #1 = Playback

        self.setFixedSize(300,30)
        self.setStyleSheet("background-color: #444; border-radius: 25px;")

        option_stylesheet = """
            QPushButton {
                background-color: #444;        /* Dark grey background */
                color: white;                  /* White text */
                border: none;                  /* No border line */
                border-radius: 8px;            /* Rounded corners */
                font-weight: bold;
            }
        """

        # Labels for options
        self.record_button = QPushButton("Record", self)
        self.record_button.setFixedSize(int(self.width()/2),self.height())
        self.record_button.setStyleSheet(option_stylesheet)
        self.record_button.clicked.connect(self.record_button_clicked)

        self.playback_button = QPushButton("Playback", self)
        self.playback_button.setFixedSize(int(self.width()/2),self.height())
        self.playback_button.setStyleSheet(option_stylesheet)
        self.playback_button.clicked.connect(self.playback_button_clicked)

        layout = QHBoxLayout()
        layout.addWidget(self.record_button, alignment=Qt.AlignCenter, stretch=2)
        layout.addWidget(self.playback_button, alignment=Qt.AlignCenter, stretch=2)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setLayout(layout)

        # Sliding button
        self.slider = QLabel("", self)
        if self.current_mode:
            self.slider.setGeometry(int(self.width()/2), 0, int(self.width()/2), self.height())
        else:
            self.slider.setGeometry(0, 0, int(self.width()/2), self.height())
        self.slider.setStyleSheet("""
            QLabel {
                background-color: rgba(255, 255, 255, 50);
                color: black;
                border-radius: 10px;
                padding: 8px;
            }
        """)

    def set_current_mode(self, mode):
        self.current_mode = mode

    def record_button_clicked(self):
        if self.current_mode:
            self.current_mode = 0
            self.app_controller.switch_mode(0)
            self.animate_slider(0)

    def playback_button_clicked(self):
        if not self.current_mode:
            self.current_mode = 1
            self.app_controller.switch_mode(1)
            self.animate_slider(int(self.width()/2))

    def animate_slider(self, new_x):
        anim = QPropertyAnimation(self.slider, b"geometry")
        anim.setDuration(250)
        anim.setEasingCurve(QEasingCurve.InOutCubic)
        anim.setStartValue(self.slider.geometry())
        anim.setEndValue(QRect(new_x, 0, int(self.width()/2), self.height()))
        anim.start()
        self.anim = anim  # Keep reference so it’s not garbage-collected

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mode_selector = ModeSelector()

    main_window = QMainWindow()
    main_window.setCentralWidget(mode_selector)
    main_window.show()

    app.exec()
