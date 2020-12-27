import random
import threading
import time
import sys


# класс Поток, который будет параллельно гравной пргорамме генерировать монстров
class monster_generator(threading.Thread):
    def __init__(self, max_len, interval, arr, flag):
        threading.Thread.__init__(self)
        self.daemon = True
        self.interval = interval
        self.list = arr
        self.max_number_of_monsters = max_len
        self.flag = flag

    def run(self):
        while len(self.list) < self.max_number_of_monsters:
            obj = Monster()
            self.list.append(obj)
            time.sleep(self.interval)
        self.flag = 0

# Класс Игрока, который отвечает за подсчет очков во время игры
class Player:
    def __init__(self, PlayerName="Unknown"):
        self._name = PlayerName
        self._point = 0

    def killMonster(self, obj):
        self._point += obj.exp

    def getPoint(self):
        print(self._point, " очков у вас")

    def __repr__(self):
        return "{} nickname".format(self._name)

# Класс NPC , у каждого свои обязанности
class Warrior:
    def __init__(self):
        self.power = random.randint(1, 20)
        self.health = 30
        self.armor = 6

    def hit(self, obj):
        obj.health -= (self.power - obj.armor) if obj.armor < self.power else 0
        if self.power - obj.armor > 0:
            print("your warrior hit the monster!")
        else:
            print("Monster too strong!")
        self.power += 2

    def __repr__(self):
        return "class warrior: health = {} , power = {} , armor = {}".format(self.health, self.power, self.armor)


class Healer:
    def __init__(self):
        self.power = 2
        self.health = 10
        self.armor = 1

    def healing(self, obj):
        obj.health += self.power
        print("Your healer heal your npc")

    def __repr__(self):
        return "class healer: health = {} , power = {} , armor = {}".format(self.health, self.power, self.armor)


class Archer:
    def __init__(self):
        self.power = 5
        self.armor = 10
        self.health = 11

    def hit(self, obj):
        obj.health -= (self.power - obj.armor) if obj.armor < self.power else 0
        if self.power - obj.armor > 0:
            print("Your archer hit the monster!")
        else:
            print("Monster too strong!")

    def __repr__(self):
        return "class archer: health = {} , power = {} , armor = {}".format(self.health, self.power, self.armor)

# Класс монстер, рандомно определяется лвл, который влияет на характеристики монстра
class Monster:
    def __init__(self):
        self.level = random.randint(1, 3)
        self.power = 7 * self.level
        self.health = 30 * self.level
        self.armor = 2 * self.level
        self.reward = 25 * self.level
        self.exp = 100 * self.level ** 2

    def hit(self, obj):
        obj.health -= (self.power - obj.armor) if obj.armor < self.power else 0
        if self.power - obj.armor > 0:
            print("Monster hit your npc")
        else:
            print("Monster couldn't hit your npc")

    def __repr__(self):
        return "Monster: health = {} , power = {} , armor = {}".format(self.health, self.power, self.armor)


def main():
    print("Добро пожаловать в Генератор битвы!")

    NamePlayer = input("Input your nickname: ")
    gamer = Player(NamePlayer)

    print("Суть игры: в начале игрок набирает себе команду по собственному усмотрению(количество NPC в отряде)")
    print("Далее игроку требуется победить монстров, если монстров станет более числа W, указанного игроком, "
          "то игрок проиграл", sep=" ")
    print("Если же все монстры побеждены игра оканчивается и соответственно игрок выиграл!")

    W = int(input("Введите крайнее число монстров: "))
    T = int(input("Периодичность генерации монстров: "))

    monster_stack = []# Список с монстрами

    flag = 1

    your_army = []# Ваша армия

    number_of_warriors = int(input("Введите количество воинов: "))
    number_of_archers = int(input("Введите количество лучников: "))
    number_of_healer = int(input("Введите количество хиллеров: "))
    # Заполняем массив армией
    for i in range(number_of_warriors):
        npc = Warrior()
        your_army.append(npc)

    for i in range(number_of_archers):
        npc = Archer()
        your_army.append(npc)

    for i in range(number_of_healer):
        npc = Healer()
        your_army.append(npc)
    # Создание и запуск потока генерации монстра
    Thread = monster_generator(W, T, monster_stack, flag)

    Thread.start()
    while flag and len(your_army) != 0 and len(monster_stack) < W:
        print(
            "Выберите команду:",
            "1 - выбрать вашего бойца и совершить действие",
            "2 - вывести список своих бойцов",
            "3 - узнать характеристики монстров",
            "4 - выход из программы", sep="\n"
        )

        choice = int(input("Your choice: "))

        if choice == 1:
            for i in your_army:
                print(i)
            print("Выберите бойца, вводя в консоль его номер: ")
            n = int(input("Номер бойца: ")) - 1
            classname = your_army[n].__class__.__name__
            if classname == 'Warrior' or 'Archer':
                print("Выберите цель для атаки, написав соответствующий номер монстра: ")
                for j in monster_stack:
                    print(j)
                atack_num = int(input("Номер монстра: ")) - 1
                your_army[n].hit(monster_stack[atack_num])
                if monster_stack[atack_num].health <= 0:
                    print("You kill monster!")
                    gamer.killMonster(monster_stack[atack_num])
                    monster_stack.pop(atack_num)
                    if len(monster_stack) == 0:
                        flag = 0
                else:
                    monster_stack[atack_num].hit(your_army[n])
                    if your_army[n].health <= 0:
                        print("Your npc was die!")
                        your_army.pop(n)
            elif classname == 'Healer':
                print("Выберите цель, которую требуется исцелить: ")
                for k in your_army:
                    print(k)
                g = int(input("Номер npc для хилла: "))
                your_army[n].hit(your_army[g])
        elif choice == 2:
            for _ in your_army:
                print(_)

        elif choice == 3:
            for _ in monster_stack:
                print(_)

        elif choice == 4:
            print("До свидания!")
            sys.exit()

        else:
            print("Неверная команда!")

    gamer.getPoint()
    if flag == 1 and len(your_army) == 0:
        print("Ваша армия умерла...")
    elif len(monster_stack) > 0:
        print("Вы проиграли, монстров стало слишком много!")
    elif len(your_army) > 0:
        print("Вы убили всех монстров!Поздравляем!")


main()

