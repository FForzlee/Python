def algorithm(n):
    a = 1
    a += 1
    a *= 2
    for i in range(n):
        print(0)
print(algorithm(5))

def linear_log_recur(n: float) -> int:
    """线性对数阶"""
    if n <= 1:
        return 1
    count: int = linear_log_recur(n // 2) + linear_log_recur(n // 2)
    for _ in range(n):
        count += 1
    return count