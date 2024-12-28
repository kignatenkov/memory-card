from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle
from random import randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Итальянский'))
question_list.append(Question('Какого цвета нет на флаге России?', 'Зелённый', 'Красный', 'Белый', 'Синий'))
question_list.append(Question('Национальная хижина якутов?', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
question_list.append(Question('В каком году основали Санкт-Петербург?', '1703', '1652', '1340', '1847'))
question_list.append(Question('Столица Чехии?', 'Прага', 'Стокгольм', 'Берлин', 'Венеция'))
question_list.append(Question('В каком году придумали баскетбол?','1891', '1790', '1935', '1659'))
question_list.append(Question('Столица Нидерландов?', 'Амстердам', 'Рим', 'Париж', 'Старсбург'))

app = QApplication([])
main_win = QWidget()
button = QPushButton('Ответить')
main_win.setWindowTitle('Memory Card')
question_main = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('Варианты ответов')
main_win.total = -1
main_win.score = 0
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
layout_ans1.addWidget(button)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
Result = QLabel('прав ты или нет?')
Correct = QLabel('ответ будет тут')

layout_res = QVBoxLayout()
layout_res.addWidget(Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(Correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question_main, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)

AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(button, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def test():
    if 'Ответить' == button.text():
        show_result()
    else:
        show_question()

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question_main.setText(q.question)
    Correct.setText(q.right_answer)
    show_question()   

def show_correct(res):
    Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

def next_question():
    main_win.total += 1
    if main_win.total != 0:
        print('Статистика\n -Всего вопросов:',main_win.total,'\n -Правильных ответов:',main_win.score,'\n Рейтинг:', main_win.score/main_win.total*100)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

main_win.setLayout(layout_card)
button.clicked.connect(click_OK)
main_win.cur_question = -1
next_question()
main_win.show()
app.exec_()








