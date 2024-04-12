def for_loop(n):
    res = 0
    for i in range(1 , n + 1):
        res += i
    return res
print(for_loop(5))

def while_loop(n):
    res = 0
    i = 1
    while i <= n:
        res += i
        i += 1
    return res
print(while_loop(5))
# while循环比for循环的自由度更高，for循环的代码更加紧凑，while循环更加灵活

def while_loop_ii(n):
    res = 0
    i = 1
    while i <= n:
        res += i
        i += 1
        i *= 2
    return res
print(while_loop_ii(10))

def nested_for_loop(n):
    res = ""
    for i in range(1 , n + 1):
        for j in range(1 , n + 1):
            res += f"({i},{j}),"
    return res
print(nested_for_loop(5))
#时间复杂度为“平方关系”（函数的操作数量与n^2成正比/算法运行时间和输入数据大小n成“平方关系”）