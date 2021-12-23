text = "X-DSPAM-Confidence:    0.8475";
pos = text.find(' ')
slicedValue = text[pos:]
f_slicedValue = float(slicedValue)
print(f_slicedValue)
