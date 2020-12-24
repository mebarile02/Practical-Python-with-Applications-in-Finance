'''
This module tests the Player and Game classes and runs 10000000 simulations, where the player chooses
to switch doors.  It demonstrates that the probability of winning by switching doors in 2/3.  This takes
about 25 seconds to run.  When using multiprocessing with 5 processes of 2000000 simulations each in 6.2.1,
that is reduced to about 13 seconds.
'''

from MonteCarlo.Player import Player
from MonteCarlo.Game import Game
import time

def main():

    results = []
    mike = Player()
    game = Game(mike)
    s = time.time()
    for i in range(10000000):
        res = game.playGame()
        results.append(res)
    e = time.time()
    print(f'Approximate probability of winning if player chooses to always switch doors: '
          f'{results.count(1)/len(results)}')
    print(f'The total time taken to run 10,000,000 simulations was {e-s} seconds.')


if __name__ == '__main__':
    main()