import random

class Robot:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense_mode = False
        self.consecutive_attacks = 0

    def attack_enemy(self, enemy):
        self.consecutive_attacks += 1
        damage_percent = 40  # Attack always reduces enemy HP by 40%
        damage = int(enemy.hp * (damage_percent / 100))
        enemy.hp -= damage
        print(f"{self.name} menyerang {enemy.name} dan memberikan {damage} damage! HP {enemy.name} menjadi {enemy.hp}")

        if self.consecutive_attacks == 3:
            hp_gain = int(damage * 0.2)  # Gain 20% of damage dealt as HP on third attack
            self.hp += hp_gain
            print(f"{self.name} telah menyerang 3 kali berturut-turut dan mendapatkan tambahan {hp_gain} HP! HP sekarang: {self.hp}")

    def defend(self):
        self.defense_mode = True
        self.hp -= int(self.hp * 0.2)  # Reduce HP by 20%
        print(f"{self.name} bersiap bertahan! HP berkurang 20% menjadi {self.hp}")
        self.consecutive_attacks = 0  # Reset consecutive attack count

    def give_up(self, enemy):
        print(f"{self.name} menyerah! {enemy.name} menang!")
        enemy.hp += self.hp  # Transfer remaining HP to the winner
        print(f"{enemy.name} menerima tambahan {self.hp} HP! HP sekarang: {enemy.hp}")
        self.hp = 0

    def is_defeated(self):
        return self.hp <= 0

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.round = 1

    def play_turn(self, robot, enemy):
        print(f"\n{robot.name} [HP: {robot.hp} | ATK: {robot.attack}]")
        print("1. Attack     2. Defense     3. Giveup")
        choice = input(f"{robot.name}, pilih aksi: ")
        
        if choice == "1":
            robot.attack_enemy(enemy)
        elif choice == "2":
            robot.defend()
        elif choice == "3":
            robot.give_up(enemy)
            return False
        return True

    def start(self):
        print("\n=== Pertarungan Robot Dimulai! ===")
        print(f"{self.robot1.name} [HP: {self.robot1.hp} | ATK: {self.robot1.attack}]")
        print(f"{self.robot2.name} [HP: {self.robot2.hp} | ATK: {self.robot2.attack}]")
        
        while not (self.robot1.is_defeated() or self.robot2.is_defeated()):
            print(f"\nRound-{self.round} ============================")
            
            if not self.play_turn(self.robot1, self.robot2):
                return
            if not self.play_turn(self.robot2, self.robot1):
                return

            if self.robot2.is_defeated():
                print(f"{self.robot2.name} kalah! {self.robot1.name} menang!")
                break
            if self.robot1.is_defeated():
                print(f"{self.robot1.name} kalah! {self.robot2.name} menang!")
                break

            self.round += 1

# Contoh permainan
robot1 = Robot("Atreus", 500, 10)
robot2 = Robot("Daedalus", 750, 8)

game = Game(robot1, robot2)
game.start()