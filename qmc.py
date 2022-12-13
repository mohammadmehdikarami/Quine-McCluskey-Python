# Give boolean function variables
while True:
    print('Enter boolean function variables:')
    variables = input()
    if ',' in variables:
        variables = variables.replace(',', ' ')
    variables = variables.split()
    if len(variables) != len(set(variables)):
        print('Try again!\n')
        continue
    if len(variables) == 0:
        print('Try again!\n')
        continue
    break
num_of_variables = len(variables)
print(num_of_variables, variables)