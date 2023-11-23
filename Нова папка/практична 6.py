import math

def data(file_path='input.txt'):
    with open(file_path, 'r') as file:
        x = float(file.read())
        n = 1 / (x**3 - math.e**1/x)
        m = n**3/2

    return x, n, m

result = data()  

result_str = f"x: {result[0]}\n n: {result[1]}\n m: {result[2]}"

print(result_str)


with open("output.txt", 'w') as f:
    f.write(result_str)
