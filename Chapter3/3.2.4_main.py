'''
This module tests the functionality of the modified Fibonacci generator function.
'''

from functions.fibonacci import fibonacci

def main():

    # Here, we can see that fib is a generator.
    fib = fibonacci()
    print(type(fib))

    # I print the first two values of the sequence, and then iterate through and display the next
    # hundred values of the sequence.
    print(next(fib))
    print(next(fib))

    for i in range(0, 100):
        print(next(fib))


if __name__ == '__main__':
    main()


