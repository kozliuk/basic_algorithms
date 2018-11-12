

def is_valid_anagram(string1, string2):
    if len(string1) != len(string2):
        return False

    l2 = list(string2)
    for char in string1:
        if char in l2:
            index = l2.index(char)
            l2.pop(index)

    if not l2:
        return True
    return False


def main():
    strings = ("car", "rat")
    assert is_valid_anagram(*strings) is False

    strings = ("server", "revers")
    assert is_valid_anagram(*strings) is True


if __name__ == '__main__':
    main()