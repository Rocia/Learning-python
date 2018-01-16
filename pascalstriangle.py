''' 
expected Output:
               1
            1    1
          1    2    1
       1    3    3    1
    1    4    6    4    1
1    5    10    10    5    1
'''
def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        prev_ln = pascal(n-1)
        for i in range(len(prev_ln)-1):
            line.append(prev_ln[i] + prev_ln[i+1])
        line += [1]
    return line
num = int(input("Enter the number of rows you wish to see in the pascals triangle:"))
print(pascal(num))
