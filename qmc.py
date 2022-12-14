# Decimal to binary converter function
def decimal_to_binary(number, num_of_bits):
    binary = ''
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    binary = '0' * (num_of_bits - len(binary)) + binary
    return binary

# Function for count number of character in string
def number_of_char(string, char):
    counter = 0
    for c in string:
        if c == char:
            counter += 1
    return counter

# Graph class
class Graph(object):
    def __init__(self, graph = None):
        if graph == None:
            graph = {}
        self.__graph = graph
    
    def add_node(self, node):
        if node not in self.__graph:
            self.__graph[node] = []
    
    def add_edge(self, edge):
        (node_1, node_2) = tuple(edge)
        if node_1 in self.__graph:
            self.__graph[node_1].append(node_2)
        else:
            self.__graph[node_1] = [node_2]
    
    def nodes(self):
        return list(self.__graph.keys())

    def edges(self):
        edges = []
        for node in self.__graph:
            for neighbour in self.__graph[node]:
                if (node, neighbour) not in edges:
                    edges.append((node, neighbour))
        return edges
    
    def __str__(self):
        res = 'Nodes: '
        for node in self.nodes():
            res += str(node) + ' '
        res += '\n'
        res += 'Edges: '
        for edge in self.edges():
            res += str(edge) + ' '
        return res

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

# Create graph
graph = Graph()

# Add minterms and don't cares to graph
for n in minterms + dont_cares:
    graph.add_node(decimal_to_binary(n, num_of_variables))