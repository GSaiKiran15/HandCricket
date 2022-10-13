import random
import math
import time


class MainGame:
    def __init__(self) -> None:
        pass
    no_of_overs = int(input("Overs : "))

    choice_of_toss = input("Choose Heads or Tails : ")
    batsmen = 10
    ball = 0
    balls = no_of_overs * 6
    player_score = 0
    computer_score = 0
    c_bat_or_bowl = 0
    p_bat_or_bowl = 0
    innings = 0

    def toss_is(self, choice_of_toss):
        toss_options = ['heads', 'tails']
        toss_output = toss_options[math.floor((random.randrange(2)))]
        if choice_of_toss.lower() == toss_output:
            print("You've Won the Toss!🤟")
            choice_of_play = input("Choose Bat or Bowl : ")
            if choice_of_play.lower() == 'bat':
                self.p_bat_or_bowl = 0
                self.c_bat_or_bowl = 1
            elif choice_of_play.lower() == 'bowl':
                self.p_bat_or_bowl = 1
                self.c_bat_or_bowl = 0
            print(
                f"You've chosen to {'bat' if self.p_bat_or_bowl == 0 else 'bowl'}")
        else:
            computer_play = math.floor((random.randrange(2)))
            print("You've lost the toss")
            if computer_play == 1:
                self.p_bat_or_bowl = 0
                self.c_bat_or_bowl = 1
            else:
                self.p_bat_or_bowl = 1
                self.c_bat_or_bowl = 0
            print(
                f"Opponent has chosen {'bat' if self.c_bat_or_bowl == 0 else 'bowl'}")

        return self.p_bat_or_bowl, self.c_bat_or_bowl

    def batting(self, player, player_sc, batsmen, ball, balls, no_of_overs, c_bat_or_bowl, p_bat_or_bowl, innings, computer_score, player_score):
        print(f"You're {'batting' if self.p_bat_or_bowl == 0 else 'bowling'}")
        time.sleep(1)
        print(f"It's {self.no_of_overs} overs match")
        time.sleep(1)
        print("You can only use numbers from 0 to 6")
        time.sleep(1)
        print("All the Best!")
        time.sleep(1)
        print("Start!")
        ball = 0
        if player is self.c_bat_or_bowl:
            while batsmen > 0 and ball < self.no_of_overs*6:
                print(f'{ball+1}th ball')
                computer_hit = math.floor((random.randrange(7)))
                player_hit = int(input("Ball : "))
                ball += 1
                balls -= 1
                print(
                    f"Your choice = {player_hit} and Computer's Choice = {computer_hit}")
                if player_hit == computer_hit:
                    batsmen -= 1
                else:
                    self.computer_score += computer_hit
                    computer_score = self.computer_score
        else:
            while batsmen > 0 and ball < self.no_of_overs*6:
                print(f'{ball+1}th ball')
                computer_hit = math.floor((random.randrange(7)))
                player_hit = int(input("Ball : "))
                ball += 1
                balls -= 1
                print(
                    f"Your choice = {player_hit} and Computer's Choice = {computer_hit}")
                if player_hit == computer_hit:
                    batsmen -= 1
                else:
                    self.player_score += player_hit
                    player_score = self.player_score
        if self.innings == 0:
            print("Innings Over")
            self.innings = 1
            if self.p_bat_or_bowl == 0:
                self.p_bat_or_bowl = 1
                self.bat_or_bowl()
            else:
                self.p_bat_or_bowl = 0
                self.bat_or_bowl()
        elif self.innings == 1:
            if self.computer_score == self.player_score:
                print("Match Tied")
            elif self.computer_score > self.player_score:
                print('You Lost 🥲, Better Luck Next Time❤️')
            else:
                print("You've Won the Match !✨")
            print(
                f"Your Score - {self.player_score}, Computer Score - {self.computer_score},player_score, computer_score")
            print("Game Over, Hope You Liked It 😉")
            quit()

    def bat_or_bowl(self):
        if self.p_bat_or_bowl == 0:
            self.batting(self.p_bat_or_bowl, self.player_score,
                         self.batsmen, self.ball, self.balls, self.no_of_overs, self.c_bat_or_bowl, self.p_bat_or_bowl, self.innings, self.computer_score, self.player_score)
        else:
            self.batting(self.c_bat_or_bowl, self.computer_score,
                         self.batsmen, self.ball, self.balls, self.no_of_overs, self.c_bat_or_bowl, self.p_bat_or_bowl, self.innings, self.computer_score, self.player_score)


game1 = MainGame()
game1.toss_is(game1.choice_of_toss)
game1.bat_or_bowl()
