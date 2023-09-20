from dataclasses import dataclass
if __name__ == "__main__":
    @dataclass
    class Container:
        num: int
        idx: int

    ls = [2, 6, 5, 8, 11]
    temp = []
    target = 14
    ans = []
    di = {}
    for idx, num in enumerate(ls):
        temp.append(Container(num=num, idx=idx))
    ls = temp[::]
    ls.sort(key=lambda x: x.num)
    left, right = 0, len(ls) - 1
    while left <= right:
        su = ls[left].num + ls[right].num
        if su > target:
            right -= 1
        elif su < target:
            left += 1
        else:
            print(ls[left].idx, ls[right].idx)
            exit()
