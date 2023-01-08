fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line.rstrip()
    for w in line.split():
        if w not in lst:
            lst.append(w) 
print(lst)