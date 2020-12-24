'''
This module contains the Game class.
'''

from MonteCarlo.Player import Player
import random

class Game(object):

    def __init__(self, player):
        if isinstance(player, Player):
            self._player = player
        else:
            raise TypeError('Please enter a valid player.')

    # This is the playGame function, which simulates the game.
    def playGame(self):
        doors = [1, 2, 3]
        playerdoor = int(self._player.choosedoor())
        prizedoor = random.choice(doors)
        doors.remove(playerdoor)
        try:
            doors.remove(prizedoor)
        except ValueError:
            pass
        d = random.choice(doors)
        c = self._player.switch()
        if c.lower() == 'y':
            if playerdoor == prizedoor:
                return 0
            else:
                return 1
        else:
            if playerdoor == prizedoor:
                return 1
            else:
                return 0

    # This is a parallelPlayGame functions which takes a passed in number of simulations.
    def parallelPlayGame(self, proc=5, sims=2000000):

        restot = []

        for i in range(proc):
            results = []
            p = Player()
            game = Game(p)
            for j in range(sims):
                res = game.playGame()
                results.append(res)
            restot.append(results)
