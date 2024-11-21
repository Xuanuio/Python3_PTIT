class DanhSach:
    def __init__(self, id, name, time, total):
        self.id = f'T0{id}'
        self.name = name
        self.time = time
        self.total = total

    def quality(self):
        return self.total * 60 / self.time

    def __str__(self):
        return f'{self.id} {self.name} {self.quality():.2f}'

def timer(s):
    h, m = map(int, s.split(':'))
    return h * 60 + m

# GPT version, rút gọn code & tối ưu các biến.....

if __name__ == '__main__':
    n = int(input())
    data = {}
    
    for _ in range(n):
        name = input()
        start_time = timer(input())
        end_time = timer(input())
        total_rain = int(input())
        
        if name not in data:
            data[name] = [0, 0]
        
        data[name][0] += end_time - start_time
        data[name][1] += total_rain
    
    ans = [DanhSach(i + 1, name, time, score) for i, (name, (time, score)) in enumerate(data.items())]
    for x in ans:
        print(x)