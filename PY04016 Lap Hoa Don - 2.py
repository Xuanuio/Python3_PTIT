from datetime import datetime

class HoaDon:
    def __init__(self, id, name, room, start, end, service):
        self.id = 'KH' + format(id, '02d')
        self.name = name
        self.room = room
        self.start = start
        self.end = end
        self.service = service

    def room_price(self):
        floor = self.room // 100
        if floor == 1:
            return 25
        elif floor == 2:
            return 34
        elif floor == 3:
            return 50
        else:
            return 80
    
    def days_number(self):
        return (datetime.strptime(self.end, '%d/%m/%Y') - datetime.strptime(self.start, '%d/%m/%Y')).days + 1
    
    def total(self):
        return self.room_price() * self.days_number() + self.service

    def __str__(self):
        return f'{self.id} {self.name} {self.room} {self.days_number()} {self.total()}'

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        name = input().strip()
        room = int(input().strip())
        start = input().strip()
        end = input().strip()
        service = int(input().strip())
        a.append(HoaDon(i + 1, name, room, start, end, service))
    a.sort(key=lambda x: -x.total())
    for x in a:
        print(x)