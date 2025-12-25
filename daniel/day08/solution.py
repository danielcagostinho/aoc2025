import math


def read_input(filename="input.txt"):
    with open(filename) as f:
        return f.read().strip()


def calculate_distance(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]
        return True

    def get_component_sizes(self):
        components = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            if root not in components:
                components[root] = 0
            components[root] += 1
        return list(components.values())


def part1(data):
    points = [tuple(map(int, line.split(","))) for line in data.split("\n")]
    pairs = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = calculate_distance(points[i], points[j])
            pairs.append((d, i, j))
    pairs.sort()
    uf = UnionFind(len(points))
    for dist, i, j in pairs[:1000]:
        uf.union(i, j)

    sizes = sorted(uf.get_component_sizes(), reverse=True)
    return sizes[0] * sizes[1] * sizes[2]


def part2(data):
    points = [tuple(map(int, line.split(","))) for line in data.split("\n")]
    pairs = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = calculate_distance(points[i], points[j])
            pairs.append((d, i, j))
    pairs.sort()
    uf = UnionFind(len(points))
    num_components = len(points)

    for dist, i, j in pairs:
        if uf.union(i, j):
            num_components -= 1
            if num_components == 1:
                return points[i][0] * points[j][0]


if __name__ == "__main__":
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
