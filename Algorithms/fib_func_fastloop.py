# Realization with fast loop
# 0, 1, 1, 2, 3, 5, 8, 13

def fib_fast_loop(index):
    a, b = 0, 1

    for i in range(index - 1):
        a, b = b, a + b   # 987

        # a = b
        # b = a + b

    return b

print(fib_fast_loop(500))
# 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125


