import timeit

def calculate_paths(max_jump, length):
    paths = 0
    if max_jump == 1:
        return 1
    if length <= 0:
        return 0
    if length <= 1:
        return 1
    for i in range(1, max_jump + 1):
        paths += calculate_paths(max_jump, length - i)
    return paths


def calculate_paths_m(max_jump, length):
    memoize = {}
    return calculate_paths_mem(memoize, max_jump, length)

def calculate_paths_mem(memo, max_jump, length):
    paths = 0
    if memo.get(length):
        return memo[length]
    if max_jump == 1:
        return 1
    if length <= 0:
        return 0
    if length <= 1:
        return 1
    for i in range(1, max_jump + 1):
        paths += calculate_paths_mem(memo, max_jump, length - i)
    memo[length] = paths
    return paths

# print(calculate_paths(3, 20))
# print(calculate_paths_m(3, 20))

def time_paths(jump, length):
    start_code = "from __main__ import calculate_paths"
    statement = f"calculate_paths({jump}, {length})"

    time = timeit.timeit(setup=start_code, stmt=statement, number=10)
    print(time)

def time_paths_memo(jump, length):
    start_code = "from __main__ import calculate_paths_m"
    statement = f"calculate_paths_m({jump}, {length})"

    time = timeit.timeit(setup=start_code, stmt=statement, number=10)

    print(time)

# time_paths(3, 25)
time_paths_memo(3, 500)

# for i in range(1, 30):
#     print(calculate_paths(3, i))
#     print(calculate_paths_m(3, i))