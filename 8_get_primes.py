from tqdm import tqdm 
import time 
import math 

def is_prime(n):
    # Tests whether n is prime or not
    if n==2 or n==3 or n==5:
        return True
    else:    
        if (n%10)%2 == 0:
            return False
        elif sum([int(i) for i in str(n)])%3 == 0:
            return False
        elif n%10 == 0 or n%10 == 5:
            return False
        else:
            for i in range(3, math.floor(math.sqrt(n))+1):
                if n%i == 0:
                    return False
                else:
                    pass
        return True

MAX_NUM = int(10e7) + 1
bef = time.time()
count = 0
with open('./PRIMES.txt', 'w') as write_file:
    for i in tqdm(range(MAX_NUM)):
        if is_prime(i):
            count += 1
            write_file.write(str(i)+'\n')
        else:
            pass 
aft = time.time()

print(count/MAX_NUM*100, 'Percent')
print(f"Max Num = {MAX_NUM}")
print(aft-bef, 'Seconds')
