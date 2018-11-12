
def is_isomorphic_strings(s1, s2):
    if len(s1) != len(s2):
        return False
    temp = {}
    for char1, char2 in zip(s1, s2):
        if char1 in temp:
            if temp[char1] != char2:
                return False
        else:
            if char2 in temp:
                return False
            temp[char1] = char2
    return True


def main():
    strings = ("egg", "add")
    assert is_isomorphic_strings(*strings) is True

    strings = ("foo", "bar")
    assert is_isomorphic_strings(*strings) is False


if __name__ == '__main__':
    main()
