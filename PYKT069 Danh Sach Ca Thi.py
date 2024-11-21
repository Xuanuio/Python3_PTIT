class MonThi:
    def __init__(self, id, day, time, room):
        self.id = 'C' + format(id, "03d")
        self.day = day
        self.time = time
        self.room = room

    def __str__(self):
        return f"{self.id} {self.day} {self.time} {self.room}"
    
if __name__ == "__main__":
    a = []
    with open("CATHI.in", "r") as f:
        n = int(f.readline())
        for i in range(n):
            a.append(MonThi(i+1, f.readline().strip(), f.readline().strip(), f.readline().strip()))
    a.sort(key = lambda x : (x.day, x.time, x.id))
    for x in a:
        print(x)
