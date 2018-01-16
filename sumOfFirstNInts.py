def sum_n(n):
    if n== 0:
        return 0
    else:
        return n + sum_n(n-1)
if __name__ == "__main__":
	num = int(input("enter a number:"))        
