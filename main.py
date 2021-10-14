class C2():
    pass


class C3:
    pass


class C1(C2, C3):
    pass


# Создание и связывание класса Cl
# Присваивание name: Cl.setname
# self является либо II, либо 12
C1.x = 1
C1.y = 1
C2.x = 2
C2.z = 2
C3.z = 3
C3.w = 3


def set_name(self, who):
    self.name = who


C1.set_name = set_name
I1 = C1()
I2 = C1()
I1.set_name('kat')
I2.set_name('mike')
print(I1.name, I2.name)
print(I1.x, I2.y, I1.z, I2.w)
