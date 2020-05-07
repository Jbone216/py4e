 #Write code using find() and string slicing (see section 6.10)
 #to extract the number at the end of the line below.
 #Convert the extracted value to a floating point number

text = "X-DSPAM-Confidence:    0.8475";
newtext = text.find(';')

number = text[24:]
print(float(number)))
