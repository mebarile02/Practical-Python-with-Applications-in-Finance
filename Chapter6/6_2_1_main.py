'''
This module uses multiprocessing to run five processes of 2000000 simulations each.  This reduces run time by
almost (not quite) half.
'''

from MonteCarlo.Player import Player
from MonteCarlo.Game import Game
import random
import time
import multiprocessing

# I mostly modified the code from lecture.  Here, I don't use 'Done' in doWork,
# but use the len(res) == NumTasks approach suggested in the notes.

def doWork(input, output):
    while True:
        try:
            parallelPlayGame, args = input.get(timeout=1)
            res = parallelPlayGame(*args)
            output.put(res)
        except:
            break

def parallelPlayGame(sims=2000000):
    results = []
    p = Player()
    game = Game(p)
    for j in range(sims):
        res = game.playGame()
        results.append(res)
    return results

def main():
    input_queue = multiprocessing.Queue()
    output_queue = multiprocessing.Queue()

    numTasks = 5
    for i in range(numTasks):
        input_queue.put((parallelPlayGame, (2000000,)))

    s = time.time()

    for i in range(numTasks):
        multiprocessing.Process(target=doWork,args=(input_queue, output_queue)).start()

    res = []
    while (True):
        r = output_queue.get()
        res.append(r)
        if len(res) == numTasks:
            break


    e = time.time()

    flt = [item for sublist in res for item in sublist]
    print(f'The approximate probability of winning if the player chooses to always switch doors: '
          f'{flt.count(1)/len(flt)}')
    print(f'The total time taken to run 10,000,000 simulations with multiprocessing was {e-s} seconds.')


if __name__ == '__main__':
    main()