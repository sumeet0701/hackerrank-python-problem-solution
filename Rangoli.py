"""
You are given an integer, . Your task is to print an alphabet rangoli of size . 
(Rangoli is a form of Indian folk art based on creation of patterns.)
"""

def rangoli(n):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    data = [alpha[i] for i in range(n)]
    item = list(range(n))
    item = item[:-1] + item[::-1]
    for i in item:
        temp = data[-(i+1):]
        row = temp[::-1]+temp[1:]
        print("-".join(row).center(n*4-3, "-"))


n = int(input())
rangoli(n=n)


