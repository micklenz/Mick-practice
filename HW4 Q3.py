def mail():
    fname = input("Enter a file: ")
    fhand = open(fname)
    lst = []
    d = {}
    for line in fhand:
        if line.startswith('From '):
            lst = line.split()
            d[lst[1]] = d.get(lst[1], 0) + 1
            lst = []
    for mail, number in d.items():
        lst.append((number, mail))
        lst.sort(reverse = True)
        print(lst[0])

mail()
