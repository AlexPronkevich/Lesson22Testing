def check_mirror(ls):
    num = len(ls) // 2
    for index in range(num):
        if ls[index] != ls[len(ls) - 1 - index]:
            return False

    return True


def test():
    print(check_mirror([1, 2, 3, 2, 1]))
    print(check_mirror([1, 2, 3, 3, 2, 1]))
    print(check_mirror([1, 2, 3, 2, 1, 1, 2]))


if __name__ == "__main__":
    test()
