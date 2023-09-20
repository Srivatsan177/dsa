from dataclasses import dataclass

if __name__ == "__main__":
    ls = [1, 0, -1, 0, -2, 2]
    target = 0


    @dataclass
    class Container:
        num: int
        idx: int
        def __str__(self):
            return self.num


    def two_sum(ls, i, j, target, ans, dp):
        print(dp)
        while i < j:
            su = ls[i].num + ls[j].num
            if su > target:
                j -= 1
            elif su < target:
                i += 1
            else:
                ans.append([i for i in (dp + [ls[i], ls[j]])])
                return


    def k_sum(ls, k, t, target, ans, dp=[]):
        if k == 2:
            two_sum(ls, t, len(ls) - 1, target, ans, dp)
        else:
            for i in range(t, len(ls)):
                dp.append(ls[i])
                k_sum(ls, k - 1, i + 1, target - ls[i].num, ans, dp)
                dp.pop()
    ls = [Container(num=num, idx=idx) for idx, num in enumerate(ls)]
    ls = sorted(ls, key=lambda x: x.num)
    ans = []
    k_sum(ls, 4, 0, target, ans)
    print(ans)
