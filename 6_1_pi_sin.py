from math import pi, sin
from argparse import ArgumentParser as AP

parser = AP()
parser.add_argument("n_sides")
args = parser.parse_args()

n = int(args.n_sides)
for i in range(n,n+1):
	result = i*sin(180/i*pi/180)
	error = (pi-result)/pi*100
	print(f"Sides = {i}, Pi = {result}, Error = {error} %")
print(f'Actual Pi = {pi}')
