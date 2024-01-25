# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 14:06:08 2024

@author: Darya Milenina

"""


from model import StableDiffusionGenerator
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QSpacerItem, QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QSizePolicy
from PyQt5.QtGui import QPixmap
import sys

class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.original_pixmap = None
        self.setMinimumSize(600, 600)
        
class MainWindow(QWidget):
    def __init__(self):      
        super().__init__()
        self.image_generator = StableDiffusionGenerator()

        self.prompt_label = QLabel('Prompt:')       
        self.prompt_edit = QLineEdit()
        self.negative_prompt_label = QLabel('Negative prompt:')           
        self.negative_prompt_edit = QLineEdit()
        self.result_label = ImageLabel()

        self.generate_button = QPushButton('Generate')        
        self.generate_button.clicked.connect(self.generate)
        self.spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        layout = QVBoxLayout() 
        
        layout.addWidget(self.prompt_label)
        layout.addWidget(self.prompt_edit)   
        layout.addWidget(self.negative_prompt_label)
        layout.addWidget(self.negative_prompt_edit)  
        layout.addWidget(self.generate_button)
        layout.addWidget(self.result_label)
        layout.addItem(self.spacer)
        self.setLayout(layout)
                
    def generate(self):     
        prompt = self.prompt_edit.text()
        negative_prompt = self.negative_prompt_edit.text()
        image_path = self.image_generator.generate_image(prompt, negative_prompt)
        pixmap = QPixmap(image_path)
        self.result_label.setPixmap(pixmap)

if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()   
    window.show()
    sys.exit(app.exec_())