# Find and return the parent of node n with path compression (iterative)
def find(n: int, parentOf: dict[int, int]) -> int:
    root = n
    # Kökü bulana kadar yukarı çık
    while parentOf[root] != root:
        root = parentOf[root]

    # Kökü bulduktan sonra tüm düğümleri köke bağla (path compression)
    while n != root:
        next_node = parentOf[n]
        parentOf[n] = root
        n = next_node

    return root


# Make u the parent of v
# parentOf[v] = u
def union(u: int, v: int, parentOf: dict[int, int]):
    parentOfV = find(v, parentOf)
    parentOfU = find(u, parentOf)
    parentOf[parentOfV] = parentOfU


## In order to use these helper funcktions we must first fill the parentOf
## Initially each node will be its own parent
## parentOf[i] = i

## then we can check if any two nodes are in the same group, by checking if they have the same parent
parentOf = dict()
x, y = 2, 3
print(find(x, parentOf) == find(y, parentOf))