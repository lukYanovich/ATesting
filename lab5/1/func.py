import math as m
import random


def my_sort(_arr):
    def quicksort(nums):
        if len(nums) <= 1:
            return nums
        else:
            q = random.choice(nums)
            s_nums = []
            m_nums = []
            e_nums = []
            for n in nums:
                if n > q:
                    s_nums.append(n)
                elif n < q:
                    m_nums.append(n)
                else:
                    e_nums.append(n)
            return quicksort(s_nums) + e_nums + quicksort(m_nums)

    return quicksort(_arr)


def parse(elem):
    if '/' in elem:
        line = list(elem.split("/"))
        elem = float(line[0]) / float(line[1])
    elif 's' in elem:
        line = list(elem.split("s"))
        elem = m.sqrt(float(line[1]))
    else:
        elem = float(elem)
    if 0 < elem <= 1.0:
        return elem
    else:
        raise Exception("incorrect data")


def read_from_file(filename):
    file = open("./in/" + filename + ".txt")
    st = list(file.readline().split())
    for i in range(len(st)):
        st[i] = parse(st[i])
    return st


def my_print(arr):
    for i in range(len(arr)):
        print(str(i + 1) + ":", arr[i])
