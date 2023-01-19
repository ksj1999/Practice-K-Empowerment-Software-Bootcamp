groups = {'빅뱅' : ['GD', '태양', '탑', '대성', '승리'], '마마무' : ['문별', '솔라', '휘인', '화사']}

for group, members in groups.items():
    print(f'{group}의 멤버')
    for member in members:
        if member != "승리":
            print(member)