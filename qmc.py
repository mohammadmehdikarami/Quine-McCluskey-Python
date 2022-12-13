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

# Give boolean function minterms
while True:
    print('Enter boolean function minterms:')
    minterms = input()
    if ',' in minterms:
        minterms = minterms.replace(',', ' ')
    minterms = minterms.split()
    try:
        minterms = [int(m) for m in minterms]
        if len(minterms) != len(set(minterms)):
            print('Try again!\n')
            continue
        if max(minterms) >= 2 ** num_of_variables:
            print('Try again!\n')
            continue
        if min(minterms) < 0:
            print('Try again!\n')
            continue
        break
    except:
        print('Try again!\n')
num_of_minterms = len(minterms)
print(num_of_minterms, minterms)