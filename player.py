class Player:
    def __init__(self, money, name):
        self.money = money
        self.name = name

players = {f"player_{i}": Player(money=1000, name=f"player{i}") for i in range(1, 4)}

print(players)