import sys
import func
import time
from pynput.keyboard import Listener


def prefix(s):
    v = [0] * len(s)
    for i in range(1, len(s)):
        k = v[i - 1]
        while k > 0 and s[k] != s[i]:
            k = v[k - 1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return v


def kmp(s, t):
    index = -1
    f = prefix(s)
    k = 0
    for i in range(len(t)):
        while k > 0 and s[k] != t[i]:
            k = f[k - 1]
        if s[k] == t[i]:
            k = k + 1
        if k == len(s):
            index = i - len(s) + 1
            break
    return index


if __name__ == "__main__":
    func.word = input()
    time.sleep(0.2)
    # Collect events until released
    with Listener(
            on_press=func.on_press,
            on_release=func.on_release) as listener:
        listener.join()
    sys.exit()
