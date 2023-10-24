import sys


sys.setrecursionlimit(int(1e8))


class AStarVsDLS:
    def __init__(self, adjacency_list, heuristics):
        self.adjacency_list = adjacency_list
        self.heuristics = heuristics
        self.dls_path = []
        self.a_star_path = []
        self.a_star_count = 0
        self.dls_count = 0

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def get_heuristic(self, n):
        return self.heuristics[n]

    def a_star_algorithm(self, start_node, stop_node):
        open_list = set([start_node])
        closed_list = set([])
        g = {}
        g[start_node] = 0
        parents = {}
        parents[start_node] = start_node
        while len(open_list) > 0:
            n = None
            for v in open_list:
                if n == None or g[v] + self.get_heuristic(v) < g[n] + self.get_heuristic(n):
                    n = v
            if n == None:
                return False
            if n == stop_node:
                while parents[n] != n:
                    self.a_star_path.append(n)
                    n = parents[n]
                self.a_star_path.append(start_node)
                self.a_star_path.reverse()
                return True
            for m, weight in self.get_neighbors(n).items():
                self.a_star_count += 1
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            open_list.remove(n)
            closed_list.add(n)
        return False

    def depth_limited_search(self, start_vertex, target_vertex, depth_limit):
        self.dls_path.append(start_vertex)
        if self.dls(start_vertex, target_vertex, depth_limit):
            return True
        else:
            return False

    def dls(self, current_vertex, target_vertex, depth_limit):
        if current_vertex == target_vertex:
            return True
        if depth_limit == 0:
            return False
        for neighbor, _ in self.get_neighbors(current_vertex).items():
            self.dls_count += 1
            self.dls_path.append(neighbor)
            if self.dls(neighbor, target_vertex, depth_limit - 1):
                return True
            self.dls_path.pop()
        return False
