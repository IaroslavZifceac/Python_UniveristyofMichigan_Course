# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
nr = 0
m = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    nr = nr + 1
    pos = line.find('0')
    fin = float(line[pos:])
    m = m+fin
print("Average spam confidence:",m/nr)
