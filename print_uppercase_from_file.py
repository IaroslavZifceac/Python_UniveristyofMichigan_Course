# It ask to input the name of the file which will be printed in uppercase

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    line = line.upper()
    print(line)
