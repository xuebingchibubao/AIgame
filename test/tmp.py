import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QScrollArea, QSizePolicy, QTextEdit, QPushButton)
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt, QTimer

class BubbleLabel(QLabel):
    """支持自动换行和气泡背景的 Label"""
    def __init__(self, text="", is_bot=True):
        super().__init__(text)
        self.setWordWrap(True)
        self.setFont(QFont("Arial", 12))
        self.setContentsMargins(10, 10, 10, 10)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        if is_bot:
            self.setStyleSheet("background-color: #cce5ff; border-radius: 10px; padding: 8px;")
        else:
            self.setStyleSheet("background-color: #e2e2e2; border-radius: 10px; padding: 8px;")
        self.adjustSize()

class ScrollablePanel(QWidget):
    """滚动容器的通用面板"""
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)

    def add_widget(self, widget):
        self.layout.addWidget(widget)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("多智能体剧情游戏")
        self.setFixedSize(1200, 800)
        self.setup_ui()

    def setup_ui(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)

        # 左侧剧情区域（2/3）
        self.story_area = ScrollablePanel()
        self.story_scroll = QScrollArea()
        self.story_scroll.setWidgetResizable(True)
        self.story_scroll.setWidget(self.story_area)
        self.story_scroll.setStyleSheet("background-color: white;")

        # 右侧聊天区域（1/3）
        self.chat_area = ScrollablePanel()
        self.chat_scroll = QScrollArea()
        self.chat_scroll.setWidgetResizable(True)
        self.chat_scroll.setWidget(self.chat_area)
        self.chat_scroll.setStyleSheet("background-color: white;")

        # 聊天输入框与按钮
        self.input_box = QTextEdit()
        self.input_box.setFixedHeight(50)
        self.send_button = QPushButton("发送")
        self.send_button.clicked.connect(self.send_message)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_box)
        input_layout.addWidget(self.send_button)

        right_panel = QVBoxLayout()
        right_panel.addWidget(self.chat_scroll)
        right_panel.addLayout(input_layout)

        # 添加到主界面布局
        main_layout.addWidget(self.story_scroll, 2)
        main_layout.addLayout(right_panel, 1)

        self.setCentralWidget(main_widget)

        # 示例数据：自动添加剧情内容
        self.add_story("欢迎来到多智能体剧情世界。")
        self.add_story("NPC 小明：我今天发现了一个秘密。")

        # 模拟 Bot 回复
        QTimer.singleShot(1000, lambda: self.stream_bot_reply("你好，欢迎来到这个世界！"))

    def add_story(self, text):
        label = QLabel(text)
        label.setWordWrap(True)
        label.setFont(QFont("Arial", 12))
        label.setStyleSheet("padding: 8px;")
        self.story_area.add_widget(label)

    def send_message(self):
        user_text = self.input_box.toPlainText().strip()
        if not user_text:
            return
        self.input_box.clear()
        user_bubble = BubbleLabel(user_text, is_bot=False)
        self.chat_area.add_widget(user_bubble)

        # 模拟 Bot 回复
        QTimer.singleShot(500, lambda: self.stream_bot_reply("这是一个流式输出的例子。每次一段，像打字机一样出现。"))

    def stream_bot_reply(self, full_text):
        """模拟逐字输出 bot 回复"""
        bubble = BubbleLabel("", is_bot=True)
        self.chat_area.add_widget(bubble)
        self.bot_text = full_text
        self.current_index = 0

        def append_next_char():
            if self.current_index < len(self.bot_text):
                bubble.setText(bubble.text() + self.bot_text[self.current_index])
                bubble.adjustSize()
                self.current_index += 1
                QTimer.singleShot(30, append_next_char)

        append_next_char()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
