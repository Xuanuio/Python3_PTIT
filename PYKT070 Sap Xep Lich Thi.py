class MonThi:
    pass

if __name__ == "__main__":
    mt, ct, lt = [], [], []
    with open("CATHI.in", "r") as f:
        for line in f:
            mt.append(line.strip())
    with open("CATHI.in", "r") as f:
        for line in f:
            ct.append(line.strip())
    with open("LICHTHI.in", "r") as f:
        for line in f:
            lt.append(line.strip())
    