"""
    simplify path
"""


def to_stack(path):
    return [part for part in path.split("/") if part and part != "."]


def simplify_path(path):
    stack = to_stack(path)

    new = []
    while stack:
        item = stack.pop(0)
        if item == "..":
            if new:
                new.pop()
            continue
        new.append(item)

    return "/" + ("/".join(new) if new else "")


def main():
    path1 = "/home/"
    assert simplify_path(path1) == "/home"

    path2 = "/a/./b/../../c/"
    assert simplify_path(path2) == "/c"

    path3 = "/home//foo/"
    assert simplify_path(path3) == "/home/foo"

    path4 = "/../"
    assert simplify_path(path4) == "/"

    path5 = "././././"
    assert simplify_path(path5) == "/"

    path6 = "././././../basic_algorithms/"
    assert simplify_path(path6) == "/basic_algorithms"


if __name__ == '__main__':
    main()
