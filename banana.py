text = 'X-DSPAM-Confidence:    0.8475'
pos = text.find('0')
fin=float(text[pos:])
print(fin)
