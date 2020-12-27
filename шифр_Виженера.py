import tkinter
from tkinter import *
#Алфавит python в chr и ord не имеет буквы ё поэтому она как с обычным алфавитом эта программа работать не будет но она шифрует Виженером с питоновским русским алфавитом
def main():
   l=0 # число для создания списка букв в длину кодируемой строки из букв ключевого слова
   o=[] # список из букв кодированной строки
   u=[] # список из букв ключевого слова которая имеет длину кодируемой строки
   b=a.get() # значение кодируемой строки
   p=c.get() # значение ключевого слова
   s = [char for char in b] # список из букв кодируемой строки
   k= [char for char in p] # список из букв ключевого слова
   for i in range(len(s)): # создание списка из букв ключевого слова во с размером длины кодируемой сроки
       u.append(k[l])
       l=l+1
       if l == len(k):
           l=0
   for i in range(len(s)): # сама кодировка
       if 1072<=ord(s[i])<=1103: # отбор: от 1072 до 1103 значения букв а-я
           t = ord(s[i])
           if t+ord(u[i])-2142>32: # вычисляем сумму номеров букв если меньше 32(количество букв в алфавите)-складываем с 1072,если больше 32 - складываем 1072 с суммой разности с алфавита и суммой нумерации
               o.append(chr(1072+t+ord(u[i])-2142-32))
           else:
               o.append(chr(1072 + t + ord(u[i]) - 2142))
       elif 1040<=ord(s[i])<=1071:
           t = ord(s[i]) + 32
           if t + ord(u[i]) - 2142 > 64:
               o.append(chr(1072 - t - ord(u[i]) + 2142+32)-32)
           else:
               o.append(chr(1072 + t + ord(u[i]) - 2142-32))
       else:
           o.append(s[i]) # и добавляем в новый массив
   return a.set(''.join(map(str, o))) # выводим кодированный массив в строку

window = Tk()
window.title("Шифр Виженера")
window.geometry('270x200')
a =StringVar()
c = StringVar()
lab = Label(text="Введите слово:")
lab.place(x=12,y=0)
pole = Entry(window,width=40 ,textvariable=a)
pole.place(x=15,y=20)
lab1 = Label(text="Введите ключ:")
lab1.place(x=12,y=40)
pole1 = Entry(window,width=40 ,textvariable=c)
pole1.place(x=15,y=60)
knopka = tkinter.Button(window, text = "Зашифровать",command = main)
knopka.place(x=85,y=90)
window.mainloop()
