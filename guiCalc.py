
from tkinter import *

INPUT_DIGIT_MAX_LEN = 5

operandsList = ['0', '0']   # Список операндов
operandIndex = 0            # Индекс операнда, с которым мы работаем в данный момент
currentOperation = ''       # Знак операции, которая выполнится при нажатии '='

#------------------------------------------------------------------------------------
def addDigit(digit):
  global operandsList
  operand = operandsList[operandIndex]

  # Производим ввод числа не длиннее чем INPUT_DIGIT_MAX_LEN
  if len(operand) < INPUT_DIGIT_MAX_LEN:
    if operand == '0':
      operand = str(digit)
    else:
      operand += str(digit)
    
    outLabel.configure(text=operand)     # Обновляем лейбл вывода
    operandsList[operandIndex] = operand # Возвращаем измененное значение операнда в список операндов

#------------------------------------------------------------------------------------
def rmLastDigit():
  global operandsList
  operand = operandsList[operandIndex]

  operand = operand[0:-1] # Берём срез строки до предпоследнего элемента

  # Проверка, остались ли цифры в строке
  if len(operand) == 0:
    operand = '0'

  outLabel.configure(text=operand) # Обновляем лейбл вывода
  operandsList[operandIndex] = operand # Возвращаем измененное значение операнда в список операндов

#-- Событие при нажатии клавиши с операцией -------------------------------------------------------
def operation(sign):
  global operandIndex
  global currentOperation

  buttonsCollorReset()

  if sign == '+':
    currentOperation = sign
    btnAdd.configure(bg="grey")
  if sign == '-':
    currentOperation = sign
    btnSub.configure(bg="grey")
  if sign == '*':
    currentOperation = sign
    btnMul.configure(bg="grey")
  if sign == '/':
    currentOperation = sign
    btnDiv.configure(bg="grey")

  if operandIndex == 0:
    operandIndex += 1

#-- Событие при нажатии клавиши "=" ---------------------------------------------------------------
def equalRes():
  global operandsList
  global operandIndex
  global currentOperation

  buttonsCollorReset()

  if operandIndex != 0:
    if currentOperation == '+':
      operandsList[0] = str(int(operandsList[0]) + int(operandsList[1]))
    elif currentOperation == '-':
      operandsList[0] = str(int(operandsList[0]) - int(operandsList[1]))
    elif currentOperation == '*':
      operandsList[0] = str(int(operandsList[0]) * int(operandsList[1]))
    elif currentOperation =='/':
      operandsList[0] = str(int(operandsList[0]) / int(operandsList[1]))

    operandsList[1] = 0
    outLabel.configure(text=operandsList[0]) # Обновляем лейбл вывода

def allClear():
  global operandsList
  global operandIndex

  operandsList = ['0', '0']
  operandIndex = 0

  outLabel.configure(text='0')
  buttonsCollorReset()

def buttonsCollorReset():
  btnAdd.configure(bg="white")
  btnSub.configure(bg="white")
  btnMul.configure(bg="white")
  btnDiv.configure(bg="white")

# Главное окно
mainWin = Tk()
mainWin.title("My calc")

# Поле вывода результата
outLabel = Label(mainWin, text='0', font=("Arial Bold", 50))
outLabel.grid(column=0, row=0, columnspan=3)

# Кнопки с цифрами
buttonFontParam = ("Arial Bold", 15)
# === 1 =========================================
btn1 = Button(mainWin, text='1', font=buttonFontParam, command=lambda: addDigit(1))
btn1.grid(column=0, row=1)
# === 2 =========================================
btn2 = Button(mainWin, text='2', font=buttonFontParam, command=lambda: addDigit(2))
btn2.grid(column=1, row=1)
# === 3 =========================================
btn3 = Button(mainWin, text='3', font=buttonFontParam, command=lambda: addDigit(3))
btn3.grid(column=2, row=1)
# === 4 =========================================
btn4 = Button(mainWin, text='4', font=buttonFontParam, command=lambda: addDigit(4))
btn4.grid(column=0, row=2)
# === 5 =========================================
btn5 = Button(mainWin, text='5', font=buttonFontParam, command=lambda: addDigit(5))
btn5.grid(column=1, row=2)
# === 6 =========================================
btn6 = Button(mainWin, text='6', font=buttonFontParam, command=lambda: addDigit(6))
btn6.grid(column=2, row=2)
# === 7 =========================================
btn7 = Button(mainWin, text='7', font=buttonFontParam, command=lambda: addDigit(7))
btn7.grid(column=0, row=3)
# === 8 =========================================
btn8 = Button(mainWin, text='8', font=buttonFontParam, command=lambda: addDigit(8))
btn8.grid(column=1, row=3)
# === 9 =========================================
btn9 = Button(mainWin, text='9', font=buttonFontParam, command=lambda: addDigit(9))
btn9.grid(column=2, row=3)
# === 0 =========================================
btn0 = Button(mainWin, text='0', font=buttonFontParam, command=lambda: addDigit(0))
btn0.grid(column=0, row=4)

# Кнопки с операциями
btnRm = Button(mainWin, text='<', font=buttonFontParam, command=rmLastDigit)
btnRm.grid(column=1, row=4)
# === '+' =========================================
btnAdd = Button(mainWin, text='+', font=buttonFontParam, command=lambda: operation('+'))
btnAdd.grid(column=2, row=4)

# === '-' =========================================
btnSub = Button(mainWin, text='-', font=buttonFontParam, command=lambda: operation('-'))
btnSub.grid(column=3, row=4)

# === '*' =========================================
btnMul = Button(mainWin, text='*', font=buttonFontParam, command=lambda: operation('*'))
btnMul.grid(column=4, row=4)

# === '/' =========================================
btnDiv = Button(mainWin, text='/', font=buttonFontParam, command=lambda: operation('/'))
btnDiv.grid(column=5, row=4)

# === '=' =========================================
btnEqv = Button(mainWin, text='=', font=buttonFontParam, command=equalRes)
btnEqv.grid(column=6, row=4)

# === 'c' =========================================
btnClr = Button(mainWin, text='C', font=buttonFontParam, command=allClear)
btnClr.grid(column=7, row=4)

mainWin.mainloop()