class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.right = None


def insert(root: Node, value: int) -> Node:
    if not root:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def traverse(root: Node, result: list[int]) -> None:
    if not root:
        return
    traverse(root.left, result)
    result.append(root.value)
    traverse(root.right, result)


def binary_sort(massive) -> list[int]:
    root: Node = None
    for value in massive:
        root = insert(root, value)
    result: list[int] = []
    traverse(root, result)
    return result
