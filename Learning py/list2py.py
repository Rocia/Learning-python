'''
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
'''
def rotate_left3(mylist):
    first = mylist.pop(0)
    sec = mylist.pop(1)
    mylist.insert(0, sec)
    mylist.insert(1, first)

    return mylist
