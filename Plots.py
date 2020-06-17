import random
from datetime import datetime
from time import sleep
from matplotlib import pyplot as plt

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



plotHistogram([0,0,0,1,1,1,1,1,3,3,3,3],"Player")
plotPieAttacks(15, 5,"puraya")
plotPieIntegrity(13, "AI")
