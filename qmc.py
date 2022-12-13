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

# Give boolean function don't cares
while True:
    print('Enter boolean function don\'t cares (or enter -1):')
    dont_cares = input()
    if ',' in dont_cares:
        dont_cares = dont_cares.replace(',', ' ')
    dont_cares = dont_cares.split()
    try:
        dont_cares = [int(d) for d in dont_cares]
        if len(dont_cares) == 1 and dont_cares[0] == -1:
            dont_cares = list()
            break
        if len(dont_cares) != len(set(dont_cares)):
            print('Try again!\n')
            continue
        if max(dont_cares) >= 2 ** num_of_variables:
            print('Try again!\n')
            continue
        if min(dont_cares) < 0:
            print('Try again!\n')
            continue
        if len(set(minterms) & set(dont_cares)) > 0:
            print('Try again!\n')
            continue
        break
    except:
        print('Try again!\n')
num_of_dont_cares = len(dont_cares)
print(num_of_dont_cares, dont_cares)