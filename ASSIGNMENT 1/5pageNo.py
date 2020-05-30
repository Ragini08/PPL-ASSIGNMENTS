pgno = ['2', '4-6', '12', '16', '17', '20', '21']
print(pgno)
for j in pgno:
    if '-' in str(j):
        y = str(j)
        x = y.find('-')
        a = int(y[: x])
        b = int(y[x + 1:])
        for k in range(a, b + 1):
            pgno.append(str(k))
        pgno.remove(j)
pgno.sort()
for i in range(1, 25+1):
    if str(i) not in pgno:
        print(i)

