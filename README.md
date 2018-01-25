# RandomNumberGenerator

Write a custom random number generation algo which should be 73% biased to the higher number. Like if I want a random number between 1 to 10 100times then it should give number more than 5 73times and less than 5 27times.

The algorithm is as follows:

Step 1 : TAKE TWO INPUTS FROM THE USER
        
        input1 is lower range
        input2 is upper range
        
Step 2 : CALCULATING THE MID VALUE
        
        mid_value = ( input1 + input2 ) / 2
        
Step 3 : GENERATING RANDOM NUMBERS IN GIVEN RANGE

	We have used two loops:
        
	The first while loop generates random numbers 73 times above the mid value.	
	The second while loop generates random numbers 27 times above the mid value. 
        
	Both the loops uses the linear congruential generator equation
        
		Xn+1 = ( a * Xn + c ) mod m

        where X is the sequence of pseudorandom values,
	        m,    0 < m                – the "modulus"
	        a,    0 < a < m            – the "multiplier"
 	        c,    0 <= c < m           – the "increment"
	        X0,   0 <= X0 < m          – the "seed" or "start value"

Step 4: IT FINALLY PRINT THE FINAL LIST

	prints the min_list,max_list,final_list with 73% biased higher random numbers.

Brief Explanation :

1. The program first takes two inputs:
       	lower and upper range.
2. It then calculates the mid value to seperate the range into two parts the upper limit and the lower limit.
3. The first while loop generates random numbers using the linear congruential generator equation ,73% biased to higher numbers. These numbers are stored in max_list.
4. The second loop generates random numbers which are 27% biased to lower range and these numbers are stored in min_list.
5. The program finally prints the max_list and min_list.
6. Both the list are then concatenated to form the final list with random numbers.	

Note :

	This algo only generates 100 random numbers. We can generate n random numbers by multiplying 0.73 to n for the max_list length
	and 0.27 to n for min_list length.
