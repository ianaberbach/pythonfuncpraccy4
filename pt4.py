def max_num(x, y, z):
    return max([x, y, z])


print("The highest number is ", max_num(5000, 90, 5))


def mult_list(list):
    ans = 1
    for i in list:
        ans = ans * i
    return ans


list = [5, 8, 10, 42, 100]
print(mult_list(list))


def rev_string(str):
    return str[::-1]


str = "!edoc ot evol I"
print(rev_string(str))


def num_within(x, y, z):
    if x >= y and x <= z:
        return True
    else:
        return False


print(num_within(100, 80, 120))
print(num_within(1, 3, 5))


def pascal(n):
    trow = [1]
    y = [0]
    for x in range(max(n, 0)):
        print(trow)
        trow = [l+r for l, r in zip(trow+y, y+trow)]
    return n >= 1


pascal(6)
