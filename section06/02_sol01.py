'''
02 이진트리 순회(깊이우선탐색)

'''

def pre_order(arr, n):
    if n >= len(arr):
        return
    else:
        print(arr[n], end=' ')
        pre_order(arr, n * 2)
        pre_order(arr, (n * 2) + 1)


def in_order(arr, n):
    if n >= len(arr):
        return
    else:
        in_order(arr, n * 2)
        print(arr[n], end=' ')
        in_order(arr, n * 2 + 1)


def post_order(arr, n):
    if n >= len(arr):
        return
    else:
        post_order(arr, n * 2)
        post_order(arr, n * 2 + 1)
        print(arr[n], end=' ')


tree = [0, 1, 2, 3, 4, 5, 6, 7]

print('전위순회 출력:', end=' ')
pre_order(tree, 1)
print()
print(f'중위순회 출력:', end=' ')
in_order(tree, 1)
print()
print(f'후위순회 출력:', end=' ')
post_order(tree, 1)