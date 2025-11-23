import sys

from PySide6.QtMultimedia import QMediaDevices
from PySide6.QtWidgets import QWidget, QLabel, QComboBox, QPushButton, QHBoxLayout, QVBoxLayout, QApplication, \
    QMainWindow


class RecordView(QWidget):
    def __init__(self, app_controller=None):
        super().__init__()

        self.app_controller = app_controller

        self.select_audio_input_label = QLabel("Select audio input device:")

        self.audio_input_select_box = QComboBox()
        devices = QMediaDevices.audioInputs()
        for device in devices:
            self.audio_input_select_box.addItem(device.description())
        self.audio_input_select_box.currentIndexChanged.connect(self.on_audio_input_select_box_changed)

        self.record_button = QPushButton("Start recording")
        self.record_button.clicked.connect(self.on_record_button_clicked)

        self.ai_summarize_button = QPushButton("Summarize with AI")

        self.bottom_buttons = QWidget()
        bottom_button_layout = QHBoxLayout()
        bottom_button_layout.addWidget(self.record_button, stretch=0)
        bottom_button_layout.addWidget(self.ai_summarize_button, stretch=0)
        self.bottom_buttons.setLayout(bottom_button_layout)

        self.save_button = QPushButton("Save recording")

        layout = QVBoxLayout()
        layout.addWidget(self.select_audio_input_label, stretch=0)
        layout.addWidget(self.audio_input_select_box, stretch=2)
        layout.addWidget(self.bottom_buttons, stretch=0)
        layout.addWidget(self.save_button, stretch=0)
        layout.setSpacing(10)
        self.setLayout(layout)

    def on_record_button_clicked(self):
        self.app_controller.on_record_button_clicked()

    def on_audio_input_select_box_changed(self):
        print(self.audio_input_select_box.currentText())



if __name__ == "__main__":
    app = QApplication(sys.argv)

    record_view = RecordView()

    main_window = QMainWindow()
    main_window.setCentralWidget(record_view)
    main_window.show()

    app.exec()