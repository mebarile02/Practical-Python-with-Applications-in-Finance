'''
This module addresses problem 4.3.1, parts a-i.
'''


import os
import shutil

def main():

    # This creates a new directory on my desktop.
    os.mkdir('/Users/michaelbarile/Desktop/NewDir')

    # This renames the directory to NewDirRename.
    os.rename('/Users/michaelbarile/Desktop/NewDir','/Users/michaelbarile/Desktop/NewDirRename')

    # Here, I remove the directory.
    os.rmdir('/Users/michaelbarile/Desktop/NewDirRename')

    # And here, it is created again.
    os.mkdir('/Users/michaelbarile/Desktop/NewDir')

    with open('/Users/michaelbarile/Desktop/NewDir/test1.txt', 'w') as fn:
        fn.write('Test line.')

    with open('/Users/michaelbarile/Desktop/NewDir/test2.txt', 'w') as fn:
        fn.write('Test line 2.')

    os.remove('/Users/michaelbarile/Desktop/NewDir/test1.txt')

    os.rename('/Users/michaelbarile/Desktop/NewDir/test2.txt', '/Users/michaelbarile/Desktop/NewDir/test3.txt')

    os.mkdir('/Users/michaelbarile/Desktop/NewDir/NewSubDir')

    shutil.move('/Users/michaelbarile/Desktop/NewDir/test3.txt',
                '/Users/michaelbarile/Desktop/NewDir/NewSubDir/test3.txt')

    shutil.rmtree('/Users/michaelbarile/Desktop/NewDir')









if __name__ == '__main__':
    main()