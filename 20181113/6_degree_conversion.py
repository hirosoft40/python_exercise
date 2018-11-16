
# 6. Celsius to Fahrenheit
cel = int(input('Temperature in Celsius?'))
fah = round(cel * 1.8 + 32, 2)   # calculating Fahrenheit. Rounded to 2 decimals for display purpose.
print ("%d celsius is %.2f Fahrenheit." % (cel, fah))
