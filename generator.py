import random
import json
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from tkinter import *


numbers = json.load(open("numbers.json"))   # Loading the data

def roll_number():  # Generating a random number
    return int(random.choice(list(numbers.keys())))


win_lose_ratio = []
balance_through_game = []


def martingale_strategy(number_of_games=100, balance=100, bet_amount=2):
    """
    This function always bets on red.
    On loss it doubles the bet.
    On win it bets with the starting bet amount.
    This is a common roulette strategy known as the Martingale strategy.
    """

    starting_money = balance  # This variable is used later on to determin if the is win or not.
    current_bet = bet_amount  # This variable contains the bet that is need to be made throughout the whole game

    for i in range(0, number_of_games):  # Playing as many games as asigned in the function properties
        roll = random.choice(list(numbers.keys()))  # Generating a random number
        bet = "red"  # Choseing a color to bet on

        if balance <= current_bet:  # This makes sure you cant end up on negative balance. If your balance
            current_bet = balance  # is lower than the bet you have to make, it bets everything you have left

        if numbers[roll][0] == bet:  # If you win
            balance += current_bet

            balance_through_game.append(balance)  # Ading the current balance to the list used for plotting the data
            current_bet = bet_amount  # Making the next bet the starting bet
        else:  # If you lose
            balance -= current_bet
            balance_through_game.append(balance)  # Ading the current balance to the list used for plotting the data
            if balance <= 0:  # Stops the game if the balance is 0 or lower
                balance_through_game.append(balance)
                break
            current_bet = current_bet * 2  # Doubling the bet for the next spin

    if starting_money > balance:  # Counts the wins and loses
        win_lose_ratio.append("loss")
    else:
        win_lose_ratio.append("win")

    return balance_through_game, win_lose_ratio


def plotting_martingale():
    plt.figure(figsize=(10, 5))

    # Plotting each of the 6 plots
    n_games = int(number_of_games.get())
    st_bet = int(bet_size.get())
    st_balance = int(number_of_games.get())

    martingale_strategy(number_of_games=n_games, balance=st_balance, bet_amount=st_bet)
    plt.title("Plot of balance throughout game using the Martingale strategy")
    plt.xlabel("Rolls", fontsize=15)
    plt.ylabel("Balance", fontsize=15)
    plt.plot(balance_through_game)
    plt.show()

    # Plotting the histogram
    num_of_games = 10000
    for i in range(0, num_of_games):
        martingale_strategy(number_of_games=n_games, balance=st_balance, bet_amount=st_bet)

    counts = Counter(win_lose_ratio)
    wins = counts["win"]
    loses = counts["loss"]

    plt.figure(figsize=(10, 5))
    plt.title("Won games compared to lost games using the Martingale strategy", fontsize=18)
    plt.bar(0, wins, label="Wins")
    plt.bar(1, loses, label="Losts")
    plt.ylabel("Number of games", fontsize=15)
    plt.yticks(fontsize=10)
    plt.tick_params(
        axis='x',
        which='both',
        bottom=False,
        top=False,
        labelbottom=False)

    plt.legend(fontsize=12)
    plt.show()


win_lose_ratio = []
balance_through_game = []


def reverse_martingale(number_of_games=100, balance=100, bet_amount=2):
    """
    This function always bets red. On win it doubles the bet.
    On loss it bets with the starting bet amount.
    This strategy is known as Reverse Martingale "Paroli".
    """

    starting_money = balance  # This variable is used later on to determin if the is win or not
    current_bet = bet_amount  # This variable contains the bet that is need to be made throughout the whole game

    for i in range(0, number_of_games):  # Playing as many games as asigned in the function properties
        roll = random.choice(list(numbers.keys()))  # Generating a random number
        bet = "red"  # The color the function bets on every time

        if balance <= current_bet:  # This makes sure you cant end up on negative balance. If your balance
            current_bet = balance  # is lower than the bet you have to make, it bets everything you have left

        if numbers[roll][0] == bet:  # If you win
            balance += current_bet

            balance_through_game.append(balance)  # Ading the current balance to the list used for plotting the data
            current_bet = current_bet * 2  # Doubling the bet for the next spin
        else:  # If you lose
            balance -= current_bet

            balance_through_game.append(balance)  # Ading the current balance to the list used for plotting the data
            current_bet = bet_amount  # Making the next bet the starting bet
            if balance <= 0:
                balance_through_game.append(balance)
                break
    if starting_money > balance:  # Counts the wins and loses
        win_lose_ratio.append("loss")
    else:
        win_lose_ratio.append("win")

    return balance_through_game, win_lose_ratio


def plotting_reverse_martingale():
    plt.figure(figsize=(10, 5))

    # Plotting each of the 6 plots
    n_games = int(number_of_games.get())
    st_bet = int(bet_size.get())
    st_balance = int(number_of_games.get())

    reverse_martingale(number_of_games=n_games, balance=st_balance, bet_amount=st_bet)
    plt.title("Plot of balance throughout game using the Recersed Martingale strategy")
    plt.xlabel("Rolls", fontsize=15)
    plt.ylabel("Balance", fontsize=15)
    plt.plot(balance_through_game)
    plt.show()

    # Plotting the histogram
    num_of_games = 10000
    for i in range(0, num_of_games):
        reverse_martingale(number_of_games=n_games, balance=st_balance, bet_amount=st_bet)

    counts = Counter(win_lose_ratio)
    wins = counts["win"]
    loses = counts["loss"]

    plt.figure(figsize=(10, 5))
    plt.title("Won games compared to lost games using the Reversed Martingale strategy", fontsize=18)
    plt.bar(0, wins, label="Wins")
    plt.bar(1, loses, label="Losts")
    plt.ylabel("Number of games", fontsize=15)
    plt.yticks(fontsize=10)
    plt.tick_params(
        axis='x',
        which='both',
        bottom=False,
        top=False,
        labelbottom=False)

    plt.legend(fontsize=12)
    plt.show()


win_lose_ratio = []
balance_through_game = []


def counter_betting(number_of_games=100, balance=100, bet_amount=2):
    """
    This function always bets on odd red. On loss it doubles the bet.
    On win it bets with the starting bet amount.
    This type of strategy where you bet on 2 binary bets is known as Counter Betting.
    """
    starting_money = balance  # This variable is used later on to determin if the is win or not.
    current_bet = bet_amount * 2  # This variable contains the bet that is need to be made throughout the whole game
    # It is times two because you bet on 2 different bets.

    for i in range(0, number_of_games):  # Playing as many games as asigned in the function properties
        roll = random.choice(list(numbers.keys()))  # Generating a random number
        bet1 = "red"  # Assigning the first bet
        bet2 = "odd"  # Assigning the second bet

        if balance <= current_bet:  # This makes sure you cant end up on negative balance. If your balance
            current_bet = balance  # is lower than the bet you have to make, it bets everything you have left

        if numbers[roll][0] == bet1 and numbers[roll][1] == bet2:  # If you win
            balance += current_bet

            balance_through_game.append(balance)  # Adding the current balance to the list used for plotting the data
            current_bet = bet_amount * 2  # Doubling the bet for the next spin
        elif numbers[roll][0] == bet1 or numbers[roll][1] == bet2:  # If you win one bet and lose the other one
            balance += 0  # The balance does not change in that case
            balance_through_game.append(balance)  # Adding the current balance to the list used for plotting the data
        elif numbers[roll][0] != bet1 and numbers[roll][1] != bet2:  # If you lose
            balance -= current_bet

            balance_through_game.append(balance)  # Adding the current balance to the list used for plotting the data
            if balance <= 0:  # Stops the game if the balance is 0 or lower
                break
            current_bet = current_bet * 2
    if starting_money > balance:
        win_lose_ratio.append("loss")
    else:
        win_lose_ratio.append("win")

    return balance_through_game, win_lose_ratio


def plotting_counter_betting():
    plt.figure(figsize=(10, 5))

    # Plotting each of the 6 plots
    n_games = int(number_of_games.get())
    st_bet = int(bet_size.get())
    st_balance = int(number_of_games.get())

    counter_betting(number_of_games=n_games, balance=st_balance, bet_amount=st_bet)
    plt.title("Plot of balance throughout game using the Counter Betting strategy")
    plt.xlabel("Rolls", fontsize=15)
    plt.ylabel("Balance", fontsize=15)
    plt.plot(balance_through_game)
    plt.show()

    # Plotting the histogram
    num_of_games = 10000
    for i in range(0, num_of_games):
        counter_betting(number_of_games=n_games, balance=st_balance, bet_amount=st_bet)

    counts = Counter(win_lose_ratio)
    wins = counts["win"]
    loses = counts["loss"]

    plt.figure(figsize=(10, 5))
    plt.title("Won games compared to lost games using the Counter Betting strategy", fontsize=18)
    plt.bar(0, wins, label="Wins")
    plt.bar(1, loses, label="Losts")
    plt.ylabel("Number of games", fontsize=15)
    plt.yticks(fontsize=10)
    plt.tick_params(
        axis='x',
        which='both',
        bottom=False,
        top=False,
        labelbottom=False)

    plt.legend(fontsize=12)
    plt.show()


win_lose_ratio = []
balance_through_game = []


def single_number(number_of_games=100, balance=100, bet_amount=2):
    """
    This function always bets on four. On loss it doesnt double the bet.
    """
    starting_money = balance  # This variable is used later on to determin if the is win or not.
    current_bet = bet_amount  # This variable contains the bet that is need to be made throughout the whole game

    for i in range(0, number_of_games):  # Playing as many games as assigned in the function properties
        roll = random.choice(list(numbers.keys()))  # Generating a random number
        bet = "four"  # Assigning the number to bet on

        if numbers[roll][3] == bet:  # If you win
            balance += current_bet * 36

            balance_through_game.append(balance)  # Adding the current balance to the list used for plotting the data
        else:  # If you lose%
            balance -= current_bet

            balance_through_game.append(balance)  # Adding the current balance to the list used for plotting the data
            if balance <= 0:  # Stops the game if the balance is 0 or lower
                balance_through_game.append(
                    balance)  # Adding the current balance to the list used for plotting the data
                break
    if starting_money > balance:  # Counts the wins and loses
        win_lose_ratio.append("loss")
    else:
        win_lose_ratio.append("win")

    return balance_through_game, win_lose_ratio


def plotting_single_number():
    plt.figure(figsize=(10, 5))

    # Plotting each of the 6 plots
    n_games = int(number_of_games.get())
    st_bet = int(bet_size.get())
    st_balance = int(number_of_games.get())

    single_number(number_of_games=n_games, balance=st_balance, bet_amount=st_bet)
    plt.title("Plot of balance throughout game using the Single number bet strategy")
    plt.xlabel("Rolls", fontsize=15)
    plt.ylabel("Balance", fontsize=15)
    plt.plot(balance_through_game)
    plt.show()

    # Plotting the histogram
    num_of_games = 10000
    for i in range(0, num_of_games):
        single_number(number_of_games=n_games, balance=st_balance, bet_amount=st_bet)

    counts = Counter(win_lose_ratio)
    wins = counts["win"]
    loses = counts["loss"]

    plt.figure(figsize=(10, 5))
    plt.title("Won games compared to lost games using the Single number bet strategy", fontsize=18)
    plt.bar(0, wins, label="Wins")
    plt.bar(1, loses, label="Losts")
    plt.ylabel("Number of games", fontsize=15)
    plt.yticks(fontsize=10)
    plt.tick_params(
        axis='x',
        which='both',
        bottom=False,
        top=False,
        labelbottom=False)

    plt.legend(fontsize=12)
    plt.show()


balance_through_game = []  # List containing the balance throughout the game
win_lose_ratio = []  # List containing if the game is a win or lose. Used in the histogram of many games


def dalambert_strategy(number_of_games=250, balance=100, bet_amount=2):
    """
    This function always bets on red.
    On loss it adds 1 to the next bet.
    On win it decreases the next bet by 1, until it has reached the starting bet.
    This strategy is knows as D'alembert.
    """
    starting_money = balance  # This variable is used later on to determin if the is win or not
    starting_bet = bet_amount  # This variable keeps the first bet. Used later to make sure you can't bet less than it
    current_bet = bet_amount  # This variable contains the bet that is need to be made throughout the whole game

    for i in range(0, number_of_games):  # Playing as many games as asigned in the function properties
        roll = random.choice(list(numbers.keys()))  # Generating a random number
        bet = "red"  # Assigning the color to bet on

        if balance <= current_bet:  # This makes sure you cant end up on negative balance. If your balance
            current_bet = balance  # is lower than the bet you have to make, it bets everything you have left

        if numbers[roll][0] == bet:  # If you win
            balance += current_bet
            balance_through_game.append(balance)  # Adding the current balance to the list used for plotting the data
            if current_bet <= starting_bet:  # Makes sure you can't bet lower than your starting bet
                pass
            else:
                current_bet -= 1
        else:  # If you lose
            balance -= current_bet
            current_bet += 1
            balance_through_game.append(balance)  # Adding the current balance to the list used for plotting the data
            if balance <= 0:  # Stops the game if the balance is 0 or lower
                balance_through_game.append(
                    balance)  # Adding the current balance to the list used for plotting the data
                break

    if starting_money >= balance:  # Counts the wins and loses
        win_lose_ratio.append("loss")
    else:
        win_lose_ratio.append("win")

    return balance_through_game, win_lose_ratio


balance_through_game = []


def plotting_dalambert():
    plt.figure(figsize=(10, 5))

    # Plotting each of the 6 plots
    n_games = int(number_of_games.get())
    st_bet = int(bet_size.get())
    st_balance = int(number_of_games.get())

    dalambert_strategy(number_of_games=n_games, balance=st_balance, bet_amount=st_bet)
    plt.title("Plot of balance throughout game using the D'Alambert strategy")
    plt.xlabel("Rolls", fontsize=15)
    plt.ylabel("Balance", fontsize=15)
    plt.plot(balance_through_game)
    plt.show()

    # Plotting the histogram
    num_of_games = 10000
    for i in range(0, num_of_games):
        dalambert_strategy(number_of_games=n_games, balance=st_balance, bet_amount=st_bet)

    counts = Counter(win_lose_ratio)
    wins = counts["win"]
    loses = counts["loss"]

    plt.figure(figsize=(10, 5))
    plt.title("Won games compared to lost games using the D’Alembert strategy", fontsize=18)
    plt.bar(0, wins, label="Wins")
    plt.bar(1, loses, label="Losts")
    plt.ylabel("Number of games", fontsize=15)
    plt.yticks(fontsize=10)
    plt.tick_params(
        axis='x',
        which='both',
        bottom=False,
        top=False,
        labelbottom=False)

    plt.legend(fontsize=12)
    plt.show()


window = Tk()  # The main tkinter function
window.geometry("600x110")  # Setting the size of the window

large_font = ("Courier", 20)  # Setting fonts to use in the application
small_font = ("Courier", 15)

l1 = Label(window, text="Starting Balance")  # Making the labels
l1.config(font=large_font)
l1.grid(row=1, column=0)

l2 = Label(window, text="Bet size")
l2.config(font=large_font)
l2.grid(row=2, column=0)

l3 = Label(window, text="Number of games")
l3.config(font=large_font)
l3.grid(row=3, column=0)

starting_balance = StringVar(window)  # Making the text boxes with all their properties
e1 = Entry(window, textvariable=starting_balance, font=small_font)
e1.insert(0, 100)
e1.grid(row=1, column=1)

bet_size = StringVar(window)
e2 = Entry(window, textvariable=bet_size, font=small_font)
e2.insert(0, 2)
e2.grid(row=2, column=1)

number_of_games = StringVar(window)
e3 = Entry(window, textvariable=number_of_games, font=small_font)
e3.insert(0, 100)
e3.grid(row=3, column=1)

menubar = Menu(window)  # Making the Function Buttons and assigning each of them with a function
menubar.add_command(label="Martingale", command=plotting_martingale)
menubar.add_command(label="Reversed Martingale", command=plotting_reverse_martingale)
menubar.add_command(label="Counter Betting", command=plotting_counter_betting)
menubar.add_command(label="Single number bet", command=plotting_single_number)
menubar.add_command(label="D’Alembert strategy", command=plotting_dalambert)
window.config(menu=menubar)

window.title("Roulette Simulator")

window.mainloop()
