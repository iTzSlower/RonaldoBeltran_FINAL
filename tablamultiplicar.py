import sys

print(sys.argv)

numero= int(sys.argv[1])

for i in range(1, 10):
    print(f"{numero} x {i} = {numero*i}")