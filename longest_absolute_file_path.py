
def path_len(stack):
    return len("/".join(st[1] for st in stack))


def longest_absolute_file_path(string):
    max_l = 0
    if not string:
        return max_l
    split = [(item.count("\t"), item.strip()) for item in string.split("\n")]
    stack = []
    for item in split:
        depth, value = item
        if stack:
            peek_depth = stack[-1][0]
            for _ in range(peek_depth - depth + 1):
                stack.pop()
        stack.append(item)
        if "." in value:
            candidate = path_len(stack)
            if candidate > max_l:
                max_l = candidate
    return max_l


def main():
    test_string = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    answer = longest_absolute_file_path(test_string)
    assert answer == 32

    test_string = "dir\n"
    answer = longest_absolute_file_path(test_string)
    assert answer == 0

    test_string = "dir\n\tsubdir1\n\t\tfile1.someext\n\t\tfile2.some"
    answer = longest_absolute_file_path(test_string)
    assert answer == 25


if __name__ == '__main__':
    main()
