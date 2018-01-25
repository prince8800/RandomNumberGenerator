import math
import time

class RandomGenerator():
    def __init__(self, start_value=time.time(), a=1664525, c=1013904223, m=math.pow(2, 32)):
        # initialising variables for the linear equation
        self.a = a             # multiplier 0 < a < m
        self.c = c             # incrementer 0 <= c < a
        self.m = m	       # modulus 0 < m, m is taken as a power of 2  
        self.start_value = start_value

    def linear_gen(self):
        # Creates random number using linear congruential generator method
        self.start_value = int(self.c + self.start_value * self.a) % self.m
        value = 0
        value = self.start_value / self.m
        return value

    def linear_gen_to_range(self,min,max):
        # Generates random number within the range
        linear_gen = self.linear_gen()
        value = min + linear_gen * (max-min)
        return value

if __name__ == "__main__":
    obj = RandomGenerator()
    min_list = []
    max_list = []
    final_list = []
    min_lmt = int(input("Enter Lower range \n"))
    max_lmt =int(input("Enter Upper range \n"))
    mid_val = (min_lmt + max_lmt) / 2
    # for generating random numbers 73 times near to the upper range
    while len(max_list) != 73:
        val = int(obj.linear_gen_to_range(mid_val+1, max_lmt+1))
        max_list.append(val)
        continue
    #  for generating random numbers 27 times near to the lower range
    while len(min_list) != 27:
        val = int(obj.linear_gen_to_range(min_lmt,mid_val-1))
        min_list.append(val)
        continue

    print("Number of values in max_list :" + str(len(max_list)))
    print(max_list)
    print("Number of values in min_list :" + str(len(min_list)))
    print(min_list)
    final_list = min_list+max_list
    print("Final list: ")
    print(final_list)
