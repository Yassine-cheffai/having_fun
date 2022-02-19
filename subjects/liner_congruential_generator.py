# user linear congruential generator formula to generate a random number
# https://coding-engineer.com/2019/10/28/random-number-generator-python/
# https://www.youtube.com/watch?v=C82JyCmtKWg
# https://towardsdatascience.com/building-a-pseudorandom-number-generator-9bc37d3a87d5

import time

seedInt = time.time()
# seedInt = 2
x = seedInt
a = 3
c = 1
m = 19
for i in range(1, 25):
    LCG = ((a * x) + c) % m
    print(int(LCG), end=" ")
    x = x + 1
