import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QMainWindow, QVBoxLayout, QFileDialog, \
    QLabel, QSlider, QHBoxLayout


class PlaybackView(QWidget):
    def __init__(self, app_controller=None):
        super().__init__()
        self.app_controller = app_controller
        
        # Select recording button
        self.select_recording_folder_button = QPushButton("Select folder of recording...")
        self.select_recording_folder_button.clicked.connect(self.select_recording_folder_button_clicked)
        
        self.recording_name = QLabel()

        self.seek_slider = QSlider(Qt.Horizontal)
        
        self.position = QLabel("Position")
        self.duration = QLabel("Duration")
        time_indicators = QWidget()
        time_indicators_layout = QHBoxLayout()
        time_indicators_layout.addWidget(self.position, alignment=Qt.AlignLeft)
        time_indicators_layout.addWidget(self.duration, alignment= Qt.AlignRight)
        time_indicators.setLayout(time_indicators_layout)

        self.play_pause_button = QPushButton()
        self.play_pause_button.clicked.connect(self.play_pause_button_clicked)

        self.seek_forward_button = QPushButton()
        self.seek_forward_button.clicked.connect(self.seek_forward_button_clicked)
        #TODO: Add seek functionality

        self.seek_backward_button = QPushButton()
        self.seek_backward_button.clicked.connect(self.seek_backward_button_clicked)
        #TODO: Add seek functionality

        playback_buttons = QWidget()
        playback_buttons_layout = QHBoxLayout()
        playback_buttons_layout.addWidget(self.seek_backward_button, alignment=Qt.AlignRight)
        playback_buttons_layout.addWidget(self.play_pause_button, alignment=Qt.AlignCenter)
        playback_buttons_layout.addWidget(self.seek_forward_button, alignment=Qt.AlignLeft)
        playback_buttons.setLayout(playback_buttons_layout)
        
        ai_summarize_button = QPushButton("Summarize with AI")
        #TODO: Add AI summarize functionality and link with button

        layout = QVBoxLayout()
        layout.addWidget(self.recording_name, alignment=Qt.AlignTop, stretch=0)
        layout.addWidget(self.select_recording_folder_button, alignment=Qt.AlignTop, stretch=0)
        layout.addWidget(self.seek_slider, alignment=Qt.AlignBottom, stretch=0)
        layout.addWidget(time_indicators, alignment=Qt.AlignCenter, stretch=0)
        layout.addWidget(playback_buttons, stretch=1)
        layout.addWidget(ai_summarize_button, stretch=1)
        layout.setSpacing(10)
        self.setLayout(layout)

    def play_pause_button_clicked(self):
        pass

    def seek_forward_button_clicked(self):
        pass

    def seek_backward_button_clicked(self):
        pass

    def select_recording_folder_button_clicked(self):
        recording_directory = QFileDialog.getExistingDirectory()
        self.recording_name.setText(recording_directory)
        return recording_directory

if __name__ == "__main__":
    app = QApplication(sys.argv)

    playback_view = PlaybackView()

    main_window = QMainWindow()
    main_window.setCentralWidget(playback_view)
    main_window.show()

    app.exec()