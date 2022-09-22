from dupont_fw import *

# calculates ROE using the DuPont Analysis Framework

d = dupont() # "d" is an object of the "dupont" Class
print(d.fw_calc(0.15, 10, 4)) # print() statement using the fw_calc() method

# output an ROE value of 6.0
