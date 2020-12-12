lst = []
with open("input.txt", "r") as inf, open("output.txt", "w") as ouf:
    for line in inf:
        lst.append(line.rstrip())
    for i in range(len(lst)-1, -1, -1):
        ouf.write(lst[i]+"\n")
