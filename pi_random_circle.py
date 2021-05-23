import random
from tqdm import tqdm 
from math import pi 
from argparse import ArgumentParser as AP
print(f"Imports complete")

parser = AP()
parser.add_argument("n_points")
args =(parser.parse_args())

num_points = int(args.n_points)
def calculate_pi(num):
	num_points_circle = 0
	for i in tqdm(range(num)):
		x1, y1 = random.random(), random.random()
		if x1*x1+y1*y1 <= 1:
			num_points_circle +=1
		else:
			pass
	return num_points_circle/num*4

result = calculate_pi(num_points)
error = (pi-result)/pi*100
print(f"Result = {result}")
print("Error = %.6f Percent"%(error))
