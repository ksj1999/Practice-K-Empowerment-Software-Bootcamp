# class

class Pokemon:
    def __init__(self, name, owner, skills):
        self.name = name
        self.owner = owner
        self.skills = skills.split('/')

        print(f"포켓몬 {name} 생산됨")

    def info(self):
        print(f"{self.owner}의 포켓몬은 {self.name}입니다")
        for skill in self.skills:
            print(skill)


p1 = Pokemon('피카츄', '한지우', '50만 볼트/100만 볼트/번개')
p2 = Pokemon('꼬부기', '오바람', '고속스핀/거품/몸통박치기/하이드로펌프')


p2.info()
p1.info()
# print(p2, skills)
# print(p1, p2)




# class Pokemon:
#     def __init__(self):  #객체 생성 시 동작
#         print("포켓몬 객체 생선됨")
#
#
# p1 = Pokemon()
# p2 = Pokemon()
# print(p1, p2)