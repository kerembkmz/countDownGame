from itertools import permutations
import random
import time


def picknumbers():
    firstFour = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    n1 = random.choice(firstFour)

    n2 = random.choice(firstFour)

    n3 = random.choice(firstFour)

    n4 = random.choice(firstFour)

    numTwo = [10, 15, 20, 25, 30, 35, 40, 45,
              50, 55, 60, 65, 70, 75, 80, 85, 90]
    n5 = random.choice(numTwo)

    n6 = random.choice(numTwo)
    return n1, n2, n3, n4, n5, n6


def game():
    t = 30  # 30 secs
    goal_number = random.randint(101, 999)
    n1, n2, n3, n4, n5, n6 = picknumbers()
    A = (n1, n2, n3, n4, n5, n6)
    list_list = permutations(A)

    calc1 = "((((({} + {})-{})*{})/{})+{})"
    calc2 = "((((({} + {})-{})*{})/{})-{})"
    calc3 = "((((({} + {})-{})*{})/{})*{})"
    calc4 = "((((({} + {})-{})*{})/{})/{})"

    list_of_calcs = []

    def calcs(list):
        for i in list:
            list_of_calcs.append(calc1.format(
                i[0], i[1], i[2], i[3], i[4], i[5]))
            list_of_calcs.append(calc2.format(
                i[0], i[1], i[2], i[3], i[4], i[5]))
            list_of_calcs.append(calc3.format(
                i[0], i[1], i[2], i[3], i[4], i[5]))
            list_of_calcs.append(calc4.format(
                i[0], i[1], i[2], i[3], i[4], i[5]))

    calcs(list_list)
    list_of_conc = []
    for i in list_of_calcs:
        list_of_conc.append(eval(i))

    def absolute_difference_function(list_value):
        return abs(list_value - goal_number)
    print(n1)
    print(n2)
    print(n3)
    print(n4)
    print(n5)
    print(n6)
    print("goal number is" + str(goal_number))

    print("you have 30 seconds to find the number, or come close to it, your time starts now.")
    closest_val = min(
        list_of_conc, key=absolute_difference_function)
    player1 = input("Type your equation here player1 : ")
    numPlayer1 = eval(player1)
    print("Your Answer is : ", numPlayer1)
    player2 = input("Type your equation here player2: ")
    numPlayer2 = eval(player2)
    print("Your Answer is : ", numPlayer2)
    def closerPlayer(goal_number):
        if (goal_number - numPlayer1) == (goal_number - numPlayer2):
            print("Draw")
        elif (goal_number - numPlayer1) < (goal_number - numPlayer2):
            print("Player1 wins")
        else:
            print("Player2 wins")
    time.sleep(30)
    closerPlayer(goal_number)
    for i in list_of_calcs:
        if eval(i) == goal_number:
            print(i + "" + "=" + str(goal_number))
        elif eval(i) == closest_val:
            print("can't get to the exact value, closest is" + str(closest_val))
            print(i + "" + "=" + str(closest_val))

game()


