'''
This module addresses the string manipulation problems in exercise 4.1.1.
'''

def main():
    s = '  The Python course is the best course that I have ever taken.   '

    print(f'The string length is {len(s)}.\n')
    oind = s.index('o')
    print(f'The index of the first "o" in the string is {oind}.\n')
    print(f'Trim off the leading spaces only: \n{s.lstrip()}\n')
    print(f'Trim off the trailing spaces only: \n{s.rstrip()}\n')
    print(f'Trim off both leading and trailing spaces: \n{s.strip()}\n')
    s = s.strip()
    print(f'Fully capitalize the string: \n{s.upper()}\n')
    print(f'Fully lowercase the string: \n{s.lower()}\n')
    cd = s.count('d')
    cthe = s.count('the')
    print(f'Number of occurrences of the letter "d" in the string is {cd}.\n')
    print(f'Number of occurrences of the word "the" in the string is {cthe}.\n')
    print(f'The first 15 characters of the string: \n{s[:15]}\n')
    print(f'The last 10 characters of the string: \n{s[-10:]}\n')
    print(f'Characters 5-23 of the string: \n{s[4:23]}\n')
    incourse = s.find('course')
    print(f'The index of the first occurrence of the word "course": \n{incourse}\n')
    incourse2 = s.find('course', s.find('course') + 1)
    print(f'The index of the second occurrence of the word "course": \n{incourse2}\n')
    sect = s.find('t', s[6:33].rfind('t') - 1)
    print(f'The index of the second to last occurrence of the letter "t", '
          f'between the 7th and 33rd character of the string: \n{sect}\n ')
    repper = s.replace('.', '!')
    print(f'Replace period with exclamation point: {repper}\n')
    repcourse = s.replace('course','class')
    print(f'Replace course with class: {repcourse}')


if __name__ == '__main__':
    main()