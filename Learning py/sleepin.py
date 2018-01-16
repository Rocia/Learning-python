'''
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
'''
import sys
def sleep_in(weekday, vacation):
    if ((weekday == True) and (vacation == True)) or ((weekday == True) and (vacation == False)):
        sleepin = False
    elif ((weekday == False) and (vacation == True)) or ((weekday == False) and (vacation == False)):
        sleepin = True
    return sleepin


def checkip(x):
    if ((x != 'Y') and (x != 'N')):
        print("invalid input")
        sys.exit()
    else:
        state = True if x == 'Y' else False
    return state


a = input("Is today a weekday?(Y/N)")
checkip(a)
b = input("Is today a vacation?(Y/N)")
checkip(b)
print(str(sleep_in(a, b)))