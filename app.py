import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QCloseEvent, QScreen
from PySide6.QtWidgets import QMainWindow, QMessageBox, QApplication, QWidget, QHBoxLayout, QVBoxLayout

from view.ModeSelector import ModeSelector
from view.RecordView import RecordView
from view.PlaybackView import PlaybackView
from model.AudioModel import AudioModel

class Main(QWidget):

    def __init__(self):
        super().__init__()

        self.current_mode = 0       # 0 = Record mode, 1 = Playback mode

        self.mode_selector = ModeSelector(app_controller=self)

        self.record_view = RecordView(app_controller=self)

        self.playback_view = PlaybackView(app_controller=self)

        self.audio_model = AudioModel()

        layout = QVBoxLayout()
        layout.addWidget(self.mode_selector, alignment=Qt.AlignCenter)
        layout.addWidget(self.record_view)
        self.setLayout(layout)

    def switch_mode(self, mode):

        # Remove the widget containing the view of the old mode
        layout = self.layout()
        w = layout.takeAt(layout.count() - 1).widget()
        layout.removeWidget(w)
        w.deleteLater()

        if self.current_mode != mode:
            #Add PlaybackInterface widget to the layout
            if mode == 1:
                self.current_mode = 1
                self.playback_view = PlaybackView(app_controller=self)
                layout.addWidget(self.playback_view)
                self.setLayout(layout)

            #Add RecordInterface widget to the layout
            elif mode == 0:
                self.current_mode = 0
                self.record_view = RecordView(app_controller=self)
                layout.addWidget(self.record_view)
                self.setLayout(layout)

    # Slots for record view
    def on_record_button_clicked(self):
        pass

    def on_audio_input_select_box_changed(self):
        pass

    def on_save_recording_button_clicked(self):
        pass

    # Slots for playback view
    def on_select_recording_button_clicked(self):
        pass

    def on_slider_changed(self):
        pass

    def on_play_pause_button_clicked(self):
        pass

    def on_seek_forward_button_clicked(self):
        pass

    def on_seek_backward_button_clicked(self):
        pass



class MainWindow(QMainWindow):
    def __init__(self, width, height):
        super().__init__()

        self.resize(width/2, height/2)

        self.setWindowTitle("Speech_to_Text")

        main = Main()

        self.setCentralWidget(main)

    def closeEvent(self, ev: QCloseEvent):
        # closing the last (and only) window ends the application
        if QMessageBox.question(self, "Please confirm...",
                                "Do you really want to close the application?",
                                QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            ev.setAccepted(True)
        else:
            ev.setAccepted(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    screen = app.primaryScreen()
    screen_resolution = QScreen.geometry(screen)
    screen_width = screen_resolution.width()
    screen_height = screen_resolution.height()

    main_window = MainWindow(screen_width, screen_height)
    main_window.show()
    sys.exit(app.exec())