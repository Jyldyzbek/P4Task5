class Solider:
    def __init__(self, bullet):
        self.bullet = bullet


class Gans:
    def __init__(self):
        self.ak_47 = 29
    
class Act_of_shooting(Solider, Gans):

    def __init__(self, bullet):
        Solider.__init__(self, bullet)
        Gans.__init__(self)

    def harakiri(self):
        if self.bullet >= 29:
            self.bullet -= self.ak_47
            print('Пьу-пьу')
            # print(self.bullet)
        elif 0 < self.bullet <= 29:
            self.bullet -= self.bullet
            # print(self.bullet)
            print('Пьу-пьу')
            print('Мало пули капитааан!')
            print('Пьу-пьу')
            self.harakiri()
        else:
            print('Патронов нету капитан по ходу нам хана !!!')
        if self.bullet:
            self.harakiri()

    def pov(self):
        if self.bullet:
            Act_of_shooting(n)

n = int(input('Дай пули капитан там война: '))
Var = Act_of_shooting(n)
Var.harakiri()