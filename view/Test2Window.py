import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableView, QPushButton, QHBoxLayout, QFileDialog
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PIL import Image
import os

class MyApplication(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Создаем модель данных для QTableView
        self.model = QStandardItemModel(0, 3)
        self.model.setHorizontalHeaderLabels(["Название", "Разрешение", "Вес"])

        # Создаем QTableView
        self.table_view = QTableView()
        self.table_view.setModel(self.model)

        # Создаем три кнопки
        btn_view_result = QPushButton('Просмотреть результат', self)
        btn_detection = QPushButton('Детекция', self)
        btn_exit = QPushButton('Выход', self)

        # Подключаем обработчики событий для кнопок
        btn_view_result.clicked.connect(self.view_result)
        btn_detection.clicked.connect(self.detect)
        btn_exit.clicked.connect(self.exit_app)

        # Создаем горизонтальный макет для кнопок
        button_layout = QHBoxLayout()
        button_layout.addWidget(btn_view_result)
        button_layout.addWidget(btn_detection)
        button_layout.addWidget(btn_exit)

        # Создаем вертикальный макет для основного окна
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table_view)
        main_layout.addLayout(button_layout)

        # Устанавливаем макет в основное окно
        self.setLayout(main_layout)

        # Устанавливаем размеры окна
        self.setFixedSize(1200, 700)
        self.setWindowTitle('Приложение с QTableView')

        # Отображаем окно
        self.show()

    def view_result(self):
        # Открываем диалог выбора папки
        folder_path = QFileDialog.getExistingDirectory(self, 'Выберите папку с изображениями')

        # Если пользователь выбрал папку, обновляем таблицу
        if folder_path:
            self.update_table(folder_path)

    def update_table(self, folder_path):
        # Очищаем таблицу
        self.model.removeRows(0, self.model.rowCount())

        # Получаем список файлов в выбранной папке
        files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

        # Заполняем таблицу информацией о каждом изображении
        for file in files:
            file_path = os.path.join(folder_path, file)
            image = Image.open(file_path)
            width, height = image.size
            size_in_bytes = os.path.getsize(file_path)
            size_in_mbytes = float(size_in_bytes / 1048576)


            # Добавляем данные в таблицу
            row_position = self.model.rowCount()
            self.model.insertRow(row_position)
            self.model.setItem(row_position, 0, QStandardItem(file))
            self.model.setItem(row_position, 1, QStandardItem(f"{width}x{height}"))
            self.model.setItem(row_position, 2, QStandardItem(f"{round(size_in_mbytes, 1)} Mbytes"))

    def detect(self):
        print('Кнопка "Детекция" нажата!')

    def exit_app(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApplication()
    sys.exit(app.exec())
