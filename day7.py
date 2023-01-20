# class

class Pokemon:
    def __init__(self, owner, skills):
        self.owner = owner
        self.skills = skills.split('/')

        print(f"포켓몬 생성:", end=' ')

    def info(self):
        print(f"{self.owner}의 포켓몬이 사용 가능한 스킬은")
        for i in range(len(self.skills)):
            print(f'{i+1} : {self.skills[i]}')
        # for skill in self.skills:
        #     print(f'{skill}')

    def attack(self, idx):
        print(f'{self.skills[idx]}공격 시전!')


class Pikachu(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "피카츄"
        print(f"{self.name}")

    def attack(self, idx):  # override
        print(f'{self.owner}의 {self.name}이 {self.skills[idx]}공격(번개) 시전!')


class Gobugi(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "꼬부기"
        print(f"{self.name}")

    def attack(self, idx):
        print(f'{self.owner}의 {self.name}이 {self.skills[idx]}공격(물) 시전!')

    def swim(self):
        print(f'{self.name}가 수영을 합니다')


class Pairi(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)
        self.name = "파이리"
        print(f"{self.name}")

    def attack(self, idx):
        print(f'{self.owner}의 {self.name}이 {self.skills[idx]}공격(물) 시전!')

    def swim(self):
        print(f'{self.name}가 수영을 합니다')


while True:
    menu = input('1) 포켓몬 생성 2) 프로그램 종료 : ')
    if menu == '2':
        print('프로그램을 종료합니다')
        break
    elif menu == '1':
        pokemon = input('1) 피카츄  2) 꼬부기  3) 파이리: ')
    if pokemon == '1':
        n = input('플레이어 이름 입력 : ')
        s = input('사용하능한 기술 입력(/로 구분하여 입력)')
        p = Pikachu(n, s)
    elif pokemon == '2':
        n = input('플레이어 이름 입력 : ')
        s = input('사용하능한 기술 입력(/로 구분하여 입력)')
        p = Gobugi(n, s)
    elif pokemon == '3':
        n = input('플레이어 이름 입력 : ')
        s = input('사용하능한 기술 입력(/로 구분하여 입력)')
        p = Pairi(n, s)
    else:
        print("메뉴에서 골라주세요")
    p.info()
    attack_menu = input('공격 번호 입력')
    p.attack(int(attack_menu)-1)

else:
    print('메뉴에서 골라주세요')