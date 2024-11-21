class DanhSach:
    def __init__(self, id, name, time, total):
        self.id = 'T0' + str(id)
        self.name = name
        self.time = time
        self.total = total

    def quality(self):
        return self.total * 60 / self.time

    def __str__(self):
        return self.id + ' ' + self.name + ' ' + '%.2f' % self.quality()
    
def timer(s):
    h, m = map(int, s.split(':'))
    return h * 60 + m

# Xuanuio version, code trâu.....
    
if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        b = []
        for _ in range(4):
            b.append(input())
        a.append(b)
    tmp, lst, cnt = [], [], 0
    for i in range(n):
        time, total = 0, 0
        if a[i][0] not in tmp:
            tmp.append(a[i][0])
            res = []
            res.append(a[i][0])
            res.append(timer(a[i][2]) - timer(a[i][1]))
            res.append(int(a[i][3]))
            lst.append(res)
        else:
            for j in range(len(tmp)):
                if a[i][0] == tmp[j]:
                    lst[j][1] += timer(a[i][2]) - timer(a[i][1])
                    lst[j][2] += int(a[i][3])
    ans = []
    for i in range(len(lst)):
        ans.append(DanhSach(i + 1, lst[i][0], lst[i][1], lst[i][2]))
    for x in ans:
        print(x)
        