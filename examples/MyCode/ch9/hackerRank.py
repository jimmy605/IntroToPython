# def print_formatted():
#     N = int(input())
#     l = len(bin(N)) - 2

#     for i in range(1, N + 1):
#         f = ""
#         for c in "doXb":
#             if f:
#                 f += " "
#             f += "{:>" + str(l) + c + "}"
#         print(f.format(i, i, i, i))

# print_formatted()
# print_formatted()




funcs = ['print', 'pop', 'sort']

def check_func(item):
    return item()

print(check_func(funcs[0]))