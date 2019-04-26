import sys
from func import *


def sort_by_boxes(elem, boxes):
    for i in range(len(boxes)):
        if boxes[i][0] + elem <= 1:
            boxes[i][1].append(elem)
            temp = boxes[i][1]
            boxes[i] = sum(temp), temp
            break
    else:
        boxes.append((elem, [elem]))


def first(st, boxes):
    # st = my_sort(st)
    print(st)
    for i in st:
        sort_by_boxes(i, boxes)
    my_print(boxes)


def second(st, boxes):
    if len(st) != 0:
        first(st, boxes)
    _in = input()
    while _in != "exit":
        elem = parse(_in)
        st.append(elem)
        sort_by_boxes(elem, boxes)
        print(st)
        my_print(boxes)
        _in = input()


if __name__ == "__main__":
    # st = []
    st = read_from_file("in")
    boxes = [(0, [])]
    # first(st, boxes)
    second(st, boxes)
    sys.exit(0)
