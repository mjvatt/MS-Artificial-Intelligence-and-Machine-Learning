# -*- coding: utf-8 -*-
"""
Created on Mon Jun 6 11:17:52 2022

@author: mjvat
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import random
import time
import os
import sys
# import GameWindow

TITLE_MONSTER = QImage('./images/monsters/monster9.png')
monsters_location = ('./images/monsters/')
monsters_list = os.listdir(monsters_location)
IMG_FLAG = QImage('./images/flag.png')
IMG_START = QImage('./images/hero2.png')
IMG_CLOCK = QImage('./images/clock.png')

NUM_COLORS = {
    1: QColor('#f44336'),
    2: QColor('#9C27B0'),
    3: QColor('#3F51B5'),
    4: QColor('#03A9F4'),
    5: QColor('#00BCD4'),
    6: QColor('#4CAF50'),
    7: QColor('#E91E63'),
    8: QColor('#FF9800')
}

LEVELS = [
    ('Beginner', 8, 10),
    ('Intermediate', 16, 40),
    ('Expert', 30, 99)
]

PLAYER_READY = 0
PLAYER_PLAYING = 1
PLAYER_LOST = 2
PLAYER_WON = 3

PLAYER_ICONS = {
    PLAYER_READY: './images/play.png',
    PLAYER_PLAYING: './images/controller.png',
    PLAYER_LOST: "./images/game_over.png",
    PLAYER_WON: './images/win.png',
}

class paint(QWidget):
    
    expandable = pyqtSignal((int, int))
    clicked = pyqtSignal()
    eaten = pyqtSignal()
    
    
    def __init__(self, x, y, *args, **kwargs):
        
        super(paint, self).__init__(*args, **kwargs)
        
        self.setFixedSize(QSize(33,33))
        
        self.x = x
        self.y = y
        
        
    def reset(self):
        
        self.is_start = False
        self.is_monster = False
        self.adjacent_n = 0
        
        self.is_revealed = False
        self.is_flagged = False
        
        self.update()
        
        
    def paintEvent(self, event):
        
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)
        
        r = event.rect()
        
        if self.is_revealed:
            color = self.palette().color(QPalette.Background)
            outer, inner = color, color
        else:
            outer, inner = Qt.black, QColor(200, 106, 6)
        
        p.fillRect(r, QBrush(inner))
        pen = QPen(outer)
        pen.setWidth(2.5)
        p.setPen(pen)
        p.drawRect(r)
        
        if self.is_revealed:
            if self.is_start:
                p.drawPixmap(r, QPixmap(IMG_START))
            
            elif self.is_monster:
                p.drawPixmap(r, QPixmap(QImage(os.path.join(monsters_location, random.choice(monsters_list)))))
                
            elif self.adjacent_n > 0:
                pen = QPen(NUM_COLORS[self.adjacent_n])
                p.setPen(pen)
                f = p.font()
                f.setBold(True)
                p.setFont(f)
                p.drawText(r, Qt.AlignHCenter | Qt.AlignVCenter, str(self.adjacent_n))
                
        elif self.is_flagged:
            p.drawPixmap(r, QPixmap(IMG_FLAG))
            
            
    def flag(self):
        self.is_flagged = True
        self.update()

        self.clicked.emit()


    def reveal(self):
        self.is_revealed = True
        self.update()


    def click(self):
        if not self.is_revealed:
            self.reveal()
            if self.adjacent_n == 0:
                self.expandable.emit(self.x, self.y)

        self.clicked.emit()


    def mouseReleaseEvent(self, e):

        if (e.button() == Qt.RightButton and not self.is_revealed):
            self.flag()

        elif (e.button() == Qt.LeftButton):
            self.click()

            if self.is_monster:
                self.eaten.emit()         
            

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
    
        self.game_chosen = 0
        
    def start_window(self):
                
        w = QWidget()
        hb = QHBoxLayout()
        
        self.setWindowTitle('Monster Wrangler')
        
        self.welcome = QLabel()
        self.welcome.setText('What level difficulty would you like to play?')
        self.setGeometry(200,200,400,100)
        self.welcome.setAlignment(Qt.AlignTop | Qt.AlignCenter)

        f = self.welcome.font()
        f.setPointSize(16)
        f.setWeight(75)
        self.welcome.setFont(f)
        
        self.gametypes = QComboBox()
        self.gametypes.setGeometry(QtCore.QRect(140,60,160,70))
        self.gametypes.addItems(['Beginner', 'Intermediate', 'Expert'])        
        self.gametypes.setEditable(True)
        self.gametypes.lineEdit().setAlignment(Qt.AlignCenter)
        self.gametypes.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLengthWithIcon)
        
        f2 = self.gametypes.font()
        f2.setPointSize(9)
        f2.setWeight(70)
        self.gametypes.setFont(f2)

        vb = QVBoxLayout()
        vb.addWidget(self.welcome)
        vb.addWidget(self.gametypes)

        w.setLayout(vb)
        self.setCentralWidget(w)

        self.show()
        self.gametypes.activated.connect(self.activated)
        self.gametypes.currentTextChanged.connect(self.text_changed)
        self.gametypes.currentIndexChanged.connect(self.index_changed)
        self.game_chosen = self.gametypes.currentIndex()
        print(self.game_chosen)
        
        sys.exit(app.exec())

        
    def game_window(self, game_chosen):
        
        self.level_name, self.b_size, self.n_monsters = LEVELS[game_chosen] # self.game_chosen

        w = QWidget()
        hb = QHBoxLayout()
        
        self.setGeometry(200, 100, 100, 100)

        self.monsters = QLabel()
        self.monsters.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.clock = QLabel()
        self.clock.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        f = self.monsters.font()
        f.setPointSize(24)
        f.setWeight(75)
        self.monsters.setFont(f)
        self.clock.setFont(f)

        self._timer = QTimer()
        self._timer.timeout.connect(self.update_timer)
        self._timer.start(999)  # 1 second timer

        self.monsters.setText("%03d" % self.n_monsters)
        self.clock.setText("000")

        self.button = QPushButton()
        self.button.setFixedSize(QSize(80, 80))
        self.button.setIconSize(QSize(80, 80))
        self.button.setIcon(QIcon('./images/controller.png'))
        self.button.setFlat(True)

        self.button.pressed.connect(self.button_pressed)

        l = QLabel()
        l.setPixmap(QPixmap.fromImage(TITLE_MONSTER))
        l.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        hb.addWidget(l)

        hb.addWidget(self.monsters)
        hb.addWidget(self.button)
        hb.addWidget(self.clock)

        l = QLabel()
        l.setPixmap(QPixmap.fromImage(IMG_CLOCK))
        l.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        hb.addWidget(l)

        vb = QVBoxLayout()
        vb.addLayout(hb)

        self.grid = QGridLayout()
        self.grid.setSpacing(5)

        vb.addLayout(self.grid)
        w.setLayout(vb)
        self.setCentralWidget(w)

        self.init_map()
        self.update_player(PLAYER_READY)

        self.reset_map()
        self.update_player(PLAYER_READY)

        self.show()

    
    def start_game(self):
        
        self.hide()
        # sys.exit(app.exec())
        self.game_window(self.game_chosen)
    
    def activated(self, index):
       
        print("Activated index:", index)
        self.start_game()
    
    def text_changed(self, s):
        
        print("Text changed:", s)
    
    def index_changed(self, index):
       
        print("Index changed", index)
        self.game_chosen = index
        print(self.game_chosen)
        return self.game_chosen
    

    def init_map(self):

        for x in range(0, self.b_size):
            
            for y in range(0, self.b_size):
                
                w = paint(x, y)
                self.grid.addWidget(w, y, x)

                w.clicked.connect(self.trigger_start)
                w.expandable.connect(self.expand_reveal)
                w.eaten.connect(self.game_over)


    def reset_map(self):

        for x in range(0, self.b_size):
            
            for y in range(0, self.b_size):
                
                w = self.grid.itemAtPosition(y, x).widget()
                w.reset()

        # Add monsters to the positions
        positions = []
        while len(positions) < self.n_monsters:
            
            x, y = random.randint(0, self.b_size - 1), random.randint(0, self.b_size - 1)
            
            if (x, y) not in positions:
                
                w = self.grid.itemAtPosition(y, x).widget()
                w.is_monster = True
                positions.append((x, y))


        def get_adjacency_n(x, y):
            
            positions = self.get_surrounding(x, y)
            n_monsters = sum(1 if w.is_monster else 0 for w in positions)

            return n_monsters

        for x in range(0, self.b_size):
            
            for y in range(0, self.b_size):
                
                w = self.grid.itemAtPosition(y, x).widget()
                w.adjacent_n = get_adjacency_n(x, y)

        while True:
            
            x, y = random.randint(0, self.b_size - 1), random.randint(0, self.b_size - 1)
            w = self.grid.itemAtPosition(y, x).widget()

            if (x, y) not in positions:
                
                w = self.grid.itemAtPosition(y, x).widget()
                w.is_start = True

                for w in self.get_surrounding(x, y):
                    
                    if not w.is_monster:
                        w.click()
                break


    def get_surrounding(self, x, y):
        positions = []

        for xi in range(max(0, x - 1), min(x + 2, self.b_size)):
            
            for yi in range(max(0, y - 1), min(y + 2, self.b_size)):
                
                positions.append(self.grid.itemAtPosition(yi, xi).widget())

        return positions


    def button_pressed(self):
        
        if self.player == PLAYER_PLAYING:
            
            self.update_player(PLAYER_LOST)
            self.reveal_map()

        elif self.player == PLAYER_LOST:
            
            self.update_player(PLAYER_READY)
            self.reset_map()


    def reveal_map(self):
        
        for x in range(0, self.b_size):
            
            for y in range(0, self.b_size):
                
                w = self.grid.itemAtPosition(y, x).widget()
                w.reveal()


    def expand_reveal(self, x, y):
        
        for xi in range(max(0, x - 1), min(x + 2, self.b_size)):
            
            for yi in range(max(0, y - 1), min(y + 2, self.b_size)):
                
                w = self.grid.itemAtPosition(yi, xi).widget()
                
                if not w.is_monster:
                    
                    w.click()


    def trigger_start(self, *args):
        
        if self.player != PLAYER_PLAYING:
            
            self.update_player(PLAYER_PLAYING)
            self._timer_start_nsecs = int(time.time())


    def update_player(self, player):
        
        self.player = player
        self.button.setIcon(QIcon(PLAYER_ICONS[self.player]))


    def update_timer(self):
        
        if self.player == PLAYER_PLAYING:
            
            n_secs = int(time.time()) - self._timer_start_nsecs
            self.clock.setText("%03d" % n_secs)


    def game_over(self):
        
        self.reveal_map()
        self.update_player(PLAYER_LOST)


if __name__ == '__main__':
    
    app = QApplication([])
    main_window = MainWindow()
    main_window.start_window()

            
            
            
            
            
            
            
            