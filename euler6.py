# The sum of the squares of the first ten natural numbers is,

# 1^2+2^2+...+10^2=385

# The square of the sum of the first ten natural numbers is,

# (1+2+...+10)^2=55^2=3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 
# 3025 - 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# define sum of squares = 0
# define sum = 0
# define i = 1

# while i <= 100
    # sum of squares = sum of squares + i*i
    # sum = sum + i
    # i = i + 1

# square of sum = sum * sum
# diff = square of sum - sum of squares
# display diff

# sum_of_squares = 0
# sum = 0
# i = 1

# while i <= 100:
    # sum_of_squares += i * i
    # sum += i
    # i += 1

sum_of_squares = 0
sum = 0

for i in range(1, 101):
    sum_of_squares += i * i
    sum += i
    

square_of_sum = sum ** 2 # use for ^2

diff = square_of_sum - sum_of_squares

print(diff)