def one_bits(n):
    count = 0
    while n > 0:
        if n & 1:
            count = count + 1
        n = n >> 1
    return count

# Driver Function
print(one_bits(23))
