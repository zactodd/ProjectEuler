"""
Question 107:
The following undirected network consists of seven vertices and twelve edges with a total weight of 243.


The same network can be represented by the matrix below.

    	A	B	C	D	E	F	G
A	-	16	12	21	-	-	-
B	16	-	-	17	20	-	-
C	12	-	-	28	-	31	-
D	21	17	28	-	18	19	23
E	-	20	-	18	-	-	11
F	-	-	31	19	-	-	27
G	-	-	-	23	11	27	-
However, it is possible to optimise the network by removing some edges and still ensure that all points on the network remain connected. The network which achieves the maximum saving is shown below. It has a weight of 93, representing a saving of 243 − 93 = 150 from the original network.


Using network.txt (right click and 'Save Link/Target As...'), a 6K text file containing a network with forty vertices, and given in matrix form, find the maximum saving which can be achieved by removing redundant edges whilst ensuring that the network remains connected.
"""


NETWORK_FILE = "../resources/network.txt"
with open(NETWORK_FILE, "r") as f:
    WEIGHTS = [[int(v) if v != "-" else None for v in line.strip("\n").split(",")] for line in f.readlines()]


def answer():
    nodes = len(WEIGHTS)
    s = sum(WEIGHTS[i][j] for i in range(nodes) for j in range(i + 1, nodes) if WEIGHTS[i][j] is not None)
    connected = {0}
    for _ in range(nodes - 1):
        l, new_node = min(
            (WEIGHTS[j][k], k) for j in connected for k in range(nodes)
            if k not in connected and WEIGHTS[j][k] is not None)
        connected.add(new_node)
        s -= l
    return s


if __name__ == '__main__':
    print("Answer is:", answer())

