def check_all_the_same(ls):
    first = ls[0]

    for item in ls:
        if first != item:
            return False

    return True

def test():
    print(check_all_the_same([1, 1, 1]))
    print(check_all_the_same([1, 3, 2]))


if __name__ == "__main__":
    test()
