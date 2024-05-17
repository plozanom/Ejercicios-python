"""
A client forgot his safe-box pin, which is five digits an has the following conditions about the pin:

    1. The sum of the fifth and third digits is 14
    2. The first digit is smaller than two times the second digit in one unit
    3. The fourth digit is graeter than the second digit in one unit
    4. The sum of the second and third digit is 10
    5. The sum of all digits in the pin is 30.

According to the conditions, you have to find the safe-box pin.
"""

"""
ECUATIONS:

pin = abcde
c+e = 14 -> c = 14-e
a = 2b-1
d = b+1
b+c = 10 -> b = 10-c
a+b+c+d+e = 30
"""

for i in range(10):

    fift=i
    third = 14-fift
    second = 10-third
    first = 2*second-1
    fourth = second+1
    
    if (first+second+third+fourth+fift) == 30:
        print(f'The pin for the safe-box is: {first}{second}{third}{fourth}{fift}')