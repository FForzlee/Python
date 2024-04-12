#终止条件、递归调用自身、返回结果
def recur(n):
    #终止条件
    if n == 1:
        return 1
    #递归调用
    res = recur(n - 1)
    #返回结果
    return n + res
    #递归深度为n
print(recur(5))
#递归函数每次调用自身时，系统都会为新开启的函数分配内存，以存储局部变量、调用地址和其他信息等。这将导致两方面的结果
#函数的上下文数据都存储在称为“栈帧空间”的内存区域中，直至函数返回后才会被释放。因此，递归通常比迭代更加耗费内存空间
#递归调用函数会产生额外的开销。因此递归通常比循环的时间效率更低
#如果函数在返回前的最后一步才进行递归调用，则该函数可以被编译器或解释器优化，使其在空间效率上与迭代相当。这种情况被称为「尾递归 tail recursion」
def tail_recur(n,res):
    if n == 0:
        return res
    return tail_resur(n - 1 , res + n)

def fib(n):
    if n == 1 or n == 2:
        return n - 1
    res = fib(n - 1) + fib(n - 2)
    return res