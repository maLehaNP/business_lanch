from PyQt6.QtWidgets import QWidget, QApplication, QMessageBox, QAbstractButton
import sys
from ui_main import Ui_Form


class Widget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pos_k = 0
        self.checklist = []
        self.cb_1.clicked.connect(self.positions)
        self.cb_2.clicked.connect(self.positions)
        self.cb_3.clicked.connect(self.positions)
        self.cb_4.clicked.connect(self.positions)
        self.cb_5.clicked.connect(self.positions)
        self.rb_11.toggled.connect(self.buttons)
        self.rb_12.toggled.connect(self.buttons)
        self.rb_21.toggled.connect(self.buttons)
        self.rb_22.toggled.connect(self.buttons)
        self.rb_31.toggled.connect(self.buttons)
        self.rb_32.toggled.connect(self.buttons)
        self.rb_41.toggled.connect(self.buttons)
        self.rb_42.toggled.connect(self.buttons)
        self.rb_51.toggled.connect(self.buttons)
        self.rb_52.toggled.connect(self.buttons)
        self.checkout.clicked.connect(self.confirm_check)

    def buttons(self):
        if self.sender().isChecked() == True:
            self.checklist.append(self.sender().text())
            self.enable_check()
        else:
            self.checklist.remove(self.sender().text())
            self.enable_check()

    def positions(self):
        if self.sender().isChecked() == True:
            self.pos_k += 1
        else:
            # нужно чтобы снимались радио-кнопки при убирании галки
            self.pos_k -= 1
        self.enable_check()

    def enable_check(self):
        if self.pos_k >= 2 and len(self.checklist) >= 2:
            self.checkout.setEnabled(1)
        else:
            self.checkout.setDisabled(1)

    def confirm_check(self):
        order = ''
        for i in range(len(self.checklist)):
            order += f"{i + 1}) {self.checklist[i]}\n"
        confirm = QMessageBox.question(self, 'Подтверждение заказа', f"Ваш заказ:\n{order}")
        if confirm == QMessageBox.StandardButton.Yes:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec())
