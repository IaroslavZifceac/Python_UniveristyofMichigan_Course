#extract all the digits that are folowing after 0, including 0

text = 'X-DSPAM-Confidence:    0.8475'
pos = text.find('0')
fin=float(text[pos:])
print(fin)
