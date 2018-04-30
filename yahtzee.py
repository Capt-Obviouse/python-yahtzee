#import tkinter as tk
import random
import time

#window = tk.Tk()

#window.title("Yahtzee")

#window.geometry('400x400')

#-------CLASSES---------
class Player:
    def __init__(self, name):
        self.name = name
        self.turn = 0
        self.total_score = 0
class ScoreCard:
    def __init__(self):
        # ones = 1, twos = 2, threes = 3, fours == 4, fives = 5, sixes = 6, kind3 = 7, kind 4 = 8, fullhouse = 9, smallStraight = 10, largeStraight = 11, chance = 12, yahtzee = 13
        self.slot = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 7: -1, 8: -1, 9: -1, 10: -1, 11: -1, 12: -1, 13: -1, 'top':0, 'bonus': 0, 'topTotal': 0, 'bonusYahtzeeCount': 0, 'bottomTotal': 0, 'total': 0}
        self.slot_name = {1: "Ones", 2: "Twos", 3: "Threes", 4: "Fours", 5: "Fives", 6: "Sixes", 7: "Three of a Kind", 8: "Four of a kind", 9: "Full House", 10: "Small Straight", 11: "Large Straight", 12: "Chance", 13: "Yahtzee", 'top': "Top", 'bonus': "Bonus",'topTotal': "Top Total", 'bonusYahtzeeCount': "Yahtzees Bonus", 'bottomTotal': "Bottom Total", 'total': "Total"}

    def __showOpenSlots__(self):
        print("Open Slots:\n")
        for x in self.slot:
            if self.slot[x] == -1:
                print("   " + str(self.slot_name[x]))

    def openSlots(self):
        for x in self.slot:
            if self.slot[x] == -1:
                print(str(str(x) + " - " + str(self.slot_name[x])))
    def __get_score__(self):

        #Total up the top
        top_total = 0
        i = 1
        while i < 7:
            if self.slot[i] > -1:
                top_total += self.slot[i]
            i += 1
        # Add the bonus to the top if it is over 63
        if top_total >= 63:
            self.slot['bonus'] = 35
        self.slot['topTotal'] = top_total + self.slot['bonus']
        print("Top Total: " + str(self.slot['topTotal']))

        # Total up the bottom
        bottom_total = 0
        while i < 14:
            if self.slot[i] > -1:
                bottom_total += self.slot[i]
            i += 1
        # Count bonus yahtzees
        bottom_total += self.slot['bonusYahtzeeCount'] * 100
        self.slot["bottomTotal"] = bottom_total
        print('Bottom Total: ' + str(self.slot['bottomTotal']))
        # add top and bottom together
        self.slot['total'] = self.slot['topTotal'] + self.slot['bottomTotal']
        print('Game Total: ' + str(self.slot['total']) + "\n")

    def __update_score__(self, dice):
        self.success = False
        while self.success == False:
            if game.__yahtzee__(dice):
                if self.slot[13] == -1:
                    print("Yahtzee Scored!\n")
                    time.sleep(5)
                    self.slot[13] = 50
                    self.success = True
                    break
                elif self.slot[13] == 50:
                     self.slot["bonusYahtzeeCount"] += 1
                     print("Bonus YAHTZEE!")
            inputString = "Where do you want to put this? Type from the following selection: \n "
            print(inputString)
            self.openSlots()
            while True:
                try:
                    slot = int(input())
                    break
                except:
                    print("Please enter a valid number")

            for x in self.slot:
                if self.slot[x] == -1:
                    pass
                    # print(self.slot_name[x])
            slot = int(slot)
            if slot < 7:
                place = "top"
            else:
                place = "bottom"

            if self.slot[slot] == -1:
                total = 0
                if place == "top":
                    for x in dice:
                        if(x == slot):
                            total += x
                else:
                    # 3 of a kind
                    if slot == 7:
                        sameCount = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
                        for x in dice:
                            sameCount[x] += 1
                        for x in sameCount:
                            if sameCount[x] >= 3:
                                for x in dice:
                                    total += x
                    # 4 of a kind
                    if slot == 8:
                        sameCount = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
                        for x in dice:
                            sameCount[x] += 1
                        for x in sameCount:
                            if sameCount[x] >= 4:
                                for x in dice:
                                    total += x
                    # Full House
                    if slot == 9:
                        if game.__yahtzee__(dice):
                            total = 25
                        else:
                            validate_2 = 0
                            validate_3 = 0
                            sameCount = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
                            for x in dice:
                                sameCount[x] += 1
                            for x in sameCount:
                                if sameCount[x] == 3:
                                    validate_3 = 1
                                if sameCount[x] == 2:
                                    validate_2 = 1
                            if validate_2+validate_3 == 2:
                                total = 25

                    # Small Straight
                    if slot == 10:
                        if game.__yahtzee__(dice):
                            total = 30
                        else:
                            dice.sort()
                            dice = list(set(dice))
                            for x in dice:
                                if x+1 in dice:
                                    if x+2 in dice:
                                        if x+3 in dice:
                                            print("4 set")
                                            total = 30
                    # Large Straight
                    if slot == 11:
                        if game.__yahtzee__(dice):
                            total = 40
                        else:
                            dice.sort()
                            dice = list(set(dice))
                            for x in dice:
                                if x+1 in dice:
                                    if x+2 in dice:
                                        if x+3 in dice:
                                            if x+4 in dice:
                                                print("5 set")
                                                total = 40

                    # Chance
                    if slot == 12:
                        for x in dice:
                            total += x
                if total > 0:
                    self.slot[slot] = total
                    print("\n" + str(self.slot_name[slot]) + " score is now: " + str(self.slot[slot]))
                    self.__get_score__()
                    self.success = True
                else:
                    if game.__scratch__() == True:
                        self.slot[slot] = 0
                        print("\n" + str(self.slot_name[slot]) + " score is now: " + str(self.slot[slot]))
                        self.__get_score__()
                        self.success = True
            else:
                print("\nYou already have something in your " + str(self.slot_name[slot]) + " box!\n\n")

class Game:
    def __init__(self):
        self.turns = 13
        #self.total_players = input("How Many Players?\n")
        #self.total_players = int(self.total_players)
        #self.player_names = []
        #self.__addPlayers__(self.total_players)
        #change later for add plalyers
        self.scoreCard = ScoreCard()
        self.yahtzee_count = 0
        self.round = 0


    def __add__(self, player):
        pass
    def __turns__(self):
        return self.turns
    def __players__(self):
        return self.total_players
    def __addPlayers__(self, players):
        self.players = players
        self.turns = self.turns * players
        i = 0
        while i < int(self.players):
            self.player_name = input("Enter Player " + str(i+1) +"\'s name\n")
            self.player_names.append(Player(self.player_name))
            i += 1
    def __yahtzee__(self, dice):
        return all(x == dice[0] for x in dice)

    def __start_round__(self):
        self.round += 1
        rolls = 1
        dice_reroll = ["n","n","n","n","n"]
        dice = [1,5,2,3,4]
        print("\nRound: " + str(self.round) + "\n")
        print("\n\n")
        self.scoreCard.__get_score__()
        self.scoreCard.__showOpenSlots__()
        print("\n")
        while rolls < 4:
            print("Roll: " + str(rolls))
            print("=============================")
            i = 0
            while i < 5:
                if(dice_reroll[i] == "n"):
                    dice[i] = random.randint(1,6)

                    #Fixing the roll remove later
                    #dice[i] = 5
                    # END fixing the game

                    dice_reroll[i] = ''
                print("Dice " + str(i+1) + ": " + str(dice[i]))
                i += 1
            if(self.__yahtzee__(dice) == True):
                print("YAHTZEE!")
                self.yahtzee_count += 1
            print("=============================")
            if rolls < 3:
                i = 0
                while i < 5:
                    dice_reroll[i] = input("Dice " + str(i+1) + " value: " + str(dice[i]) + " - Type n to re-roll\n")
                    i += 1
            else:
                self.scoreCard.__update_score__(dice)
            rolls += 1
        print("Total rounds: " + str(self.round) + "\n" + "Total yahtzees: " + str(self.yahtzee_count))

    def __start__(self):
        while int(game.turns) > self.round:
            self.__start_round__()
    def __scratch__(self):
        confirm = input("Are you sure you want to scratch? type y or n\n")
        if confirm == "y":
            return True
        else:
            return False

class Dice:
    pass

#--------FUNCTIONS---------

#-------GAME LOOP-------
stop = ""
while stop != "yes":
    game = Game()
    print("\n" * 3)
    game.__start__()
    stop = input("To stop type: yes")
#window.mainloop()
