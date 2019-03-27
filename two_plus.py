A = input("请输入一组数字,用空格分隔")
L = list(map(int, A.split()))
MAX = []
def max_list(l):
    max = l[0]
    sum = 0
    i = len(l)
    for number in l:
        sum += number
        if sum > max:
             max = sum
        if sum < 0:
             sum = 0
    MAX.append(max)
def Max(l):
    for i in range(len(l)):
        max_list(l)
        l.append(l.pop(0))
    return max(MAX)
print(Max(L))
