import sys
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QGridLayout, QLabel, QPushButton

import randomizer


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        grid = QGridLayout()
        column_1_width = 100

        self.rom_path = self.LineEdit()
        rom_label = QLabel("ROM:")
        rom_label.setFixedWidth(column_1_width)
        grid.addWidget(rom_label, 0, 0)
        grid.addWidget(self.rom_path, 0, 1, 1, 2)

        self.output_path = self.LineEdit()
        output_label = QLabel("Output Path:")
        output_label.setFixedWidth(column_1_width)
        grid.addWidget(output_label, 1, 0)
        grid.addWidget(self.output_path, 1, 1, 1, 2)

        randomize_button = QPushButton(self)
        randomize_button.setText("Randomize")
        randomize_button.clicked.connect(self.randomize_clicked)
        grid.addWidget(randomize_button, 2, 2)

        self.setLayout(grid)
        self.setFixedSize(500, 200)
        self.setWindowTitle("Pokemon Stadium Randomizer")

    def randomize_clicked(self):
        randomizer.randomizer_func(self.rom_path.text(), self.output_path.text())

    class LineEdit(QLineEdit):
        def __init__(self):
            super().__init__()
            self.setAcceptDrops(True)

        def dragEnterEvent(self, event):
            if event.mimeData().hasUrls():
                event.accept()
            else:
                event.ignore()

        def dropEvent(self, event):
            lines = []
            for url in event.mimeData().urls():
                lines.append(url.toLocalFile())
            self.setText('\n'.join(lines))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
