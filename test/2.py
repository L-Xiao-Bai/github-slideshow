def fact(x):
    if x==0:
        return 1
    return x * fact(x-1)
print('请输入：')
x=int(input())
print(fact(x))