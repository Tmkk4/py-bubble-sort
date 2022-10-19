# -*- coding: utf-8 -*-

"""
Bubble sort
- データ数 指定可能に
- 配列 or listの値は, 乱数を用いて生成
- 昇順 or 降順 設定可能に
"""
import random


def bubble_sort(lst):
    right_tmp = 0
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            right_tmp = lst[i+1]
            lst[i+1] = lst[i]
            lst[i] = right_tmp
            bubble_sort(lst)
    return lst


def generate_list(n):
    r = 0
    lst = []
    for i in range(n):
        r = random.randint(0, 100)
        lst.append(r)
    return lst


if __name__ == "__main__":
    n = int(input('data length? >>'))
    data = generate_list(n)
    print(f"generated data: {data}")
    result = bubble_sort(data)
    print(f"sorted: {result}")



