
import tkinter as tk
import tkinter.ttk as ttk

def btnClick():
  print(txtField.get())

# Создаём объект окна приложения
win = tk.Tk()

# Настраиваем окно
win.title("My first GUI application")
win.geometry('300x200')

# Создаём объект текстовой строки
lbl = tk.Label(win, text='Hello world')
lbl.grid(column=0, row=0, columnspan=10)

# Создаём объект, хранящий состояние чекбокса
testVar = tk.BooleanVar()
testVar.set(True)

# Создаём объект чекбокса
chk = tk.Checkbutton(win, text="Select", var=testVar)
chk.grid(column=0, row=2)

# Создаём объект, хранящий состояние переключателя
testVar = tk.IntVar()

# Создаём объекты переключателя
rbtn1 = tk.Radiobutton(win, text="Radiobutton 1", value=1, variable=testVar)
rbtn2 = tk.Radiobutton(win, text="Radiobutton 2", value=2, variable=testVar)
rbtn3 = tk.Radiobutton(win, text="Radiobutton 3", value=3, variable=testVar)
rbtn1.grid(column=0, row=3)
rbtn2.grid(column=1, row=3)
rbtn3.grid(column=2, row=3)

# Создаём объект выпадающего списка
comBox = ttk.Combobox(win)
comBox['value'] = ['Test 1', 'Test 2', 'Test 3', 'Test 4', 'Test 5', 'Test 6']
comBox.current(0)
comBox.grid(column=0, row=4)

# Создаём объект, хранящий содержимое текстового поля
textFieldData = tk.StringVar()
textFieldData.set('Test')

# Создаём объект текстового поля
txtField = tk.Entry(win, width=10, textvariable=textFieldData)
txtField.grid(column=0, row=5)

# Создаём объекты кнопки
btn = tk.Button(win, text="Press", command=btnClick)
btn.grid(column=0, row=6)

win.mainloop()
