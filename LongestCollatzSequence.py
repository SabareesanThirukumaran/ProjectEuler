cache = {1: 1}

def get_collatz_length(n):
    if n in cache:
        return cache[n]
    
    if n % 2 == 0:
        length = 1 + get_collatz_length(n // 2)
    else:
        length = 1 + get_collatz_length(3 * n + 1)
    
    cache[n] = length
    return length

max_len = 0
starting_num = 0

for i in range(1, 1000000):
    current_len = get_collatz_length(i)
    if current_len > max_len:
        max_len = current_len
        starting_num = i

print(starting_num)

# Keep a dictionary of all visited starting paths
# Recursively calculate the length of the path for each starting number