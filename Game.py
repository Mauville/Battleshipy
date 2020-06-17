import random
from datetime import datetime
from time import sleep
from matplotlib import pyplot as plt

# DEMO
# ship1 = "j10"
# ship2 = "b9 c9"
# ship3 = "a5 c5"
# ship4 = "j1 j4"
# ship5 = "a1 e1"

def shipgenerator(board: list):
    # Ship1
    board[random.randint(0, 9)][random.randint(0, 9)] = "O"
    # Generate ship 2 to ship 5
    i = 3
    while i < 7:
        ship = generateship(i)
        if shipvalidator(ship[0], ship[1], board):
            placeship(ship[0], ship[1], board)
            i += 1
    return board


def gameprinter(aiboard: list, playerboard: list, notification: str, playername: str, enemyname: str):
    header = """
    ____        __  __  __    _____ __    _     
   / __ )____ _/ /_/ /_/ /__ / ___// /_  (_)___ 
  / __  / __ `/ __/ __/ / _ \\\\__ \/ __ \/ / __ \\
 / /_/ / /_/ / /_/ /_/ /  __/__/ / / / / / /_/ /
/_____/\__,_/\__/\__/_/\___/____/_/ /_/_/ .___/ 
                                       /_/      
"""
    separator = "================================================="
    newpage = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print(newpage)
    print(separator, end=" ")
    print(header, end="")
    print(separator)
    legend = """     O  Ship
     @  Hit
     X  Miss """
    boardprinter(aiboard, enemyname + "'s Board")
    boardprinter(playerboard, playername + "'s Board")
    print(separator)
    if notification:
        print((notification + "!").center(45))
    else:
        print()
    print(legend)
    print(separator)
    if notification:
        sleep(2)


def shotvalidator(shot: str, board: list):
    """
    Validates a shot
    :param shot: A string of the type "letterNUMBER"
    :param board: A 2D list containing the board
    :return: Whether the shot is valid.
    """
    valid = False
    # validate len
    if len(shot) > 1 and len(shot) <= 3:
        # Validate letterNUMBER format
        letter = shot[0]
        numbers = shot[1:]
        if letter.isalpha() and numbers.isnumeric():
            # Validate letter in letter range
            characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
            if letter in characters:
                # Validate number in board range
                if 1 <= int(numbers) <= 10:
                    # Validate place not operated
                    coords = shotparser(shot)
                    if board[coords[0]][coords[1]] == " " or board[coords[0]][coords[1]] == "O":
                        valid = True
    return valid


def shotparser(shot: str):
    """
    Parse a shot of the form "letterNUMBER" to array coordinates. 
    :param shot: A string of the type "letterNUMBER"
    :return: A tuple with the int values of the coordinates.
    """
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 't', 'u',
                  'v', 'w', 'x', 'y', 'z']
    # Get index of letter
    return int(shot[1:]) - 1, characters.index(shot[0])


def validateship(coordinates: str, board: list):
    coords = shipparser(coordinates)
    return shipvalidator(coords[0], coords[1], board)


def place(coordinates: str, board: list):
    coords = shipparser(coordinates)
    return placeship(coords[0], coords[1], board)


def plotPieAttacks(turns, hitconfirms, player):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    confirmpercent = hitconfirms * 100 / turns
    labels = 'Success', 'Failure'
    sizes = [confirmpercent, 100 - confirmpercent]
    fig1, ax1 = plt.subplots()
    ax1.set_title(player + "'s Attacks")
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig(str(datetime.now()).replace(":", ".") + "_AttackPIE" + player + ".png")
    plt.show()


def enemyattack(playerboard):
    """
    Attacks a random point on a board that has not been previously attacked.
    :param playerboard: The 2D array board to attack
    :return: A valid shot coordinate.
    """
    while True:
        attempt = shotgenerator()
        # Generates a valid shot
        if playerboard[attempt[0]][attempt[1]] == " " or playerboard[attempt[0]][attempt[1]] == "O":
            break
    return attempt


def plotHistogram(streak, title):
    plt.title(title)
    plt.hist(streak, bins=5)
    plt.savefig(str(datetime.now()).replace(":", ".") + "_HIST.png")
    plt.show()


def plotPieIntegrity(hitconfirms, enemy):
    confirmpercent = hitconfirms * 100 / 15
    labels = 'Destroyed', 'Intact'
    sizes = [confirmpercent, 100 - confirmpercent]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.set_title(enemy + "'s Fleet Integrity")
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig(str(datetime.now()).replace(":", ".") + "_IntegrityPIE" + enemy + ".png")
    plt.show()


def boardprinter(board: list, title: str):
    """
    # Prints a board with a title.
    # board = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], ]
    :param board: A list to decorate.
    :param title: The title of the list
    :return: A decorated string of the board.
    """
    padding = "            "
    header = padding + "  |A|B|C|D|E|F|G|H|I|J|"
    protoboard = ""
    for i in range(10):
        newrow = str(board[i])
        newrow = newrow.replace("[", "#|").replace(
            ", ", "|").replace("'", "").replace("]", "|")
        # Prepend number column
        if i == 9:
            newrow = newrow.replace("#", padding + str(i + 1), 1)
        else:
            newrow = newrow.replace("#", padding + str(i + 1) + " ", 1)
        protoboard += newrow + "\n"

    print(title.center(46))
    print(header)
    print(protoboard)


def shotgenerator():
    """
    Generates a valid shot

    :return: Tuple with 2D array coordinates.
    """
    return random.randint(0, 9), random.randint(0, 9)


def shipvalidator(point1: tuple, point2: tuple, board: list):
    """
    Validates a ship placement.
    Assumes points are already valid.

    :param point1: Tuple containing ints of ship point 1
    :param point2: Tuple containing ints of ship point 2
    :param board: A 2D list containing the board
    :return: Whether the ship placement is valid
    """
    valid = True
    # Is horizontal
    if point1[0] == point2[0]:
        # No collisions
        for i in range(min(point1[1], point2[1]), max(point1[1], point2[1])):
            if board[point1[0]][i] != " ":
                valid = False
    # Is vertical
    elif point1[1] == point2[1]:
        # Doesn't overlap
        for i in range(min(point1[0], point2[0]), max(point1[0], point2[0])):
            if board[i][point1[1]] != " ":
                valid = False
    else:
        valid = False
    return valid


def shipparser(coordinates: str):
    rawcoords = coordinates.split(" ")
    return shotparser(rawcoords[0]), shotparser(rawcoords[1])


def placeship(point1: tuple, point2: tuple, board: list):
    """
    Places a ship on an board.
    Assumes ship is valid.

    :param point1: Tuple containing ints of ship point 1
    :param point2: Tuple containing ints of ship point 2
    :param board: A 2D list containing the board
    :return: The board with the ship in place.
    """
    # Is horizontal
    if point1[0] == point2[0]:
        for i in range(min(point1[1], point2[1]), max(point1[1], point2[1]) + 1):
            board[point1[0]][i] = "O"
    # Is vertical
    elif point1[1] == point2[1]:
        for i in range(min(point1[0], point2[0]), max(point1[0], point2[0]) + 1):
            board[i][point1[1]] = "O"
    return board


def generateship(length: int):
    """
    Generate a ship of length N.

    :param length: Length of ship.
    :return: A tuple containing point 1 and point 2 of a ship.
    """
    length = length - 1
    vertical = bool(random.randint(0, 1))
    if vertical:
        col1 = random.randint(0, 9)
        row1 = random.randint(0, 9 - length)
        col2 = col1
        row2 = row1 + length
        return (col1, row1), (col2, row2)
    if not vertical:
        col1 = random.randint(0, 9 - length)
        row1 = random.randint(0, 9)
        col2 = col1 + length
        row2 = row1
        return (col1, row1), (col2, row2)

#Boards
myboard = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
secretboard = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
               [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]
visibleboard = [[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]]


# Fill AI board
secretboard = shipgenerator(secretboard)

# Get turn
myturn = bool(random.randint(0, 1))

# Stats
player_total_attacks = 0
player_total_hits = 0
player_streak_history = []

ai_total_attacks = 0
ai_total_hits = 0
ai_streak_history = []

currentstreak = 0
name = input("Yer name? ")
# name = "Mike"
ainame = input("Yer rival's name? ")
# ainame = "Cunk"

gameprinter(visibleboard, myboard, "", name, ainame)
ship1 = input("Patrol Ship (Size 1)")
# ship1 = "j11"
if shotvalidator(ship1, myboard):
    coords = shotparser(ship1)
    myboard[coords[0]][coords[1]] = "O"
    gameprinter(visibleboard, myboard, "Ship placed", name, ainame)
ship2 = input("Submarine (Size 2)")
# ship2 = "b9 c9"
if validateship(ship2, myboard):
    myboard = place(ship2, myboard)
    gameprinter(visibleboard, myboard, "Ship placed", name, ainame)
ship3 = input("Destroyer (Size 3)")
# ship3 = "a5 c5"
if validateship(ship3, myboard):
    myboard = place(ship3, myboard)
    gameprinter(visibleboard, myboard, "Ship placed", name, ainame)
ship4 = input("Battleship (Size 4)")
# ship4 = "j1 j4"
if validateship(ship4, myboard):
    myboard = place(ship4, myboard)
    gameprinter(visibleboard, myboard, "Ship placed", name, ainame)
ship5 = input("Carrier (Size 5)")
# ship5 = "a1 e1"
if validateship(ship5, myboard):
    myboard = place(ship5, myboard)
    gameprinter(visibleboard, myboard, "Ship placed", name, ainame)

# goodtogo = "Y"
goodtogo = input("Ready? y/n ").upper()

if goodtogo != "Y":
    exit(0)

playing = True
mistake = False

while playing:
    while myturn:
        if not mistake:
            gameprinter(visibleboard, myboard, "", name, ainame)
        coords = input("Please input a coordinate: ")
        if not shotvalidator(coords, secretboard):
            mistake = True
            gameprinter(visibleboard, myboard, "Invalid", name, ainame)
            continue
        mistake = False
        coords = shotparser(coords)
        player_total_attacks += 1
        if secretboard[coords[0]][coords[1]] == "O":
            secretboard[coords[0]][coords[1]] = "@"
            visibleboard[coords[0]][coords[1]] = "@"
            gameprinter(visibleboard, myboard, "Hit", name, ainame)
            player_total_hits += 1
            currentstreak += 1
            if player_total_hits == 15:
                playing = False
                gameprinter(visibleboard, myboard, "You Won", name, ainame)
                break
            continue
        else:
            visibleboard[coords[0]][coords[1]] = "X"
            gameprinter(visibleboard, myboard, "Missed", name, ainame)
            if currentstreak != 0:
                player_streak_history.append(currentstreak)
                currentstreak = 0
            myturn = not myturn
    while not myturn:
        myturn = not myturn
        ai_total_attacks += 1
        attack = enemyattack(myboard)
        if myboard[attack[0]][attack[1]] == "O":
            myboard[attack[0]][attack[1]] = "@"
            gameprinter(visibleboard, myboard, ainame + " hit you", name, ainame)
            myturn = not myturn
            ai_total_hits += 1
            currentstreak += 1
            if ai_total_hits == 15:
                playing = False
                gameprinter(visibleboard, myboard, "You Lost", name, ainame)
                break
            continue
        else:
            myboard[attack[0]][attack[1]] = "X"
            gameprinter(visibleboard, myboard, ainame + " missed you", name, ainame)
            if currentstreak != 0:
                ai_streak_history.append(currentstreak)
                currentstreak = 0

# Plots
plotPieAttacks(player_total_attacks, player_total_hits, name)
plotPieAttacks(ai_total_attacks, ai_total_hits, "AI")

plotHistogram(ai_streak_history, ainame + " Streaks")
plotHistogram(player_streak_history, name + " Streaks")

plotPieIntegrity(player_total_hits, ainame)
plotPieIntegrity(ai_total_hits, name)
