class newClass:
    def __init__(self, name):
        self.name = name
        print("초기화")

    def t1(self):
        print("test1" + self.name)

    def t2(self):
        print("test2" + self.name)


a = newClass("김만재")
a.t1()
a.t2()
