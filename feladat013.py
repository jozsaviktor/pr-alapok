#be: szam
#ki: a szám negatív

'''
szam = int(input('Adj meg egy számot!'))
if szam < 0:
    print(f'A megadott szám negatív')
print('>> A program vége!<<')
'''

#be: szam
#ki: a szám negatív vagy nem negatív
"""
szam = int(input('Adj meg egy számot!'))
if szam < 0:
    print(f'A megadott szám {szam} negatív')
else:
    print(f'A megadott szám {szam} nemnegatív.')
print('>> A program vége!<<')
"""

#be: szam
#ki: a szám negatív vagy nem negatív vagy 0

"""
szam = int(input('Adj meg egy számot! '))
if szam < 0:
    print(f'A megadott szám {szam} negatív.')
elif szam == 0:
    print(f'A megadott szám {szam} nulla.')
else:
    print(f'A megadott szám {szam} pozitív.')
print('>> A program vége! <<')
"""

szam = int(input('Adj meg egy számot! '))
if szam < 0:
    print(f'A megadott szám {szam} negatív.')
elif szam > 0:
    print(f'A megadott szám {szam} pozitív.')
elif szam == 0:
    print(f'A megadott szám {szam} nulla.')
print('>> A program vége! <<')