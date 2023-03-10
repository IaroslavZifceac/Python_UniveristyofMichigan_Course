def computepay (h, r):
    if h > 40:
            gross = 40*r+(h-40)*1.5*r
    else :
            gross = 40*r
    return gross

hrs = input ("Enter Hours:")
rate = input ("Rate per hour:")
try:
   h = float(hrs)
   r = float(rate)
except:
   print("The input value should be between 0.0 and 1.0")
   quit()
p = computepay (h, r)
print ("Pay", p)
