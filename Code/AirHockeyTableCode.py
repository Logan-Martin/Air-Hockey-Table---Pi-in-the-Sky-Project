import board # type: ignore
import digitalio  # type: ignore
import time

resetButton = digitalio.DigitalInOut(board.GP18) # Button stuff
resetButton.direction = digitalio.Direction.INPUT
resetButton.pull = digitalio.Pull.DOWN

led1 = digitalio.DigitalInOut(board.GP19)
led1.direction = digitalio.Direction.OUTPUT

scoreNeededToWinGame = 7

player1 = {
    "score": 1
}
player2 = {
    "score": 0
}

def playerWonFunction(whoWon):
    print(str(whoWon) + " won the game!")


def playerScoredFunction(whoScored):
    if whoScored.score + 1 != scoreNeededToWinGame:
        whoScored.score = whoScored.score + 1
    else:
        print("Winning point scored.")
        playerWonFunction(whoScored)


def resetScoreFunction():
    print("Resetting Score.")
    player1Score = 0
    player2Score = 0

while True:
    time.sleep(0.01)
    led1.value = True
    if resetButton.value == True and player1["score"] + player2["score"] != 0 : # When player press button, and combined score does not equal 0, then reset score. (Maybe make something for protecting the score?)
       print("Reseting score, maybe.")


     
