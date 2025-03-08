p = 71

def get_congruent(number):
    return number % p

# Problem 1

print('')
print('Problem 1')
print('')

input = [-1, -4, -160, 500]

for x in input:
     print(f'For {x}, congruent is {get_congruent(x)}')