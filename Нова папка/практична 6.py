import math

file = open('input.txt', 'r')
x = float(file.read())
n = 1 / (x**3 - math.e**1/x)
m = n**3/2
print(f"x = {x}\nn = {n}\nm = {m}")
    
f = open("output.txt", 'w')
f.write(f"n = {n}\nm = {m}") 

