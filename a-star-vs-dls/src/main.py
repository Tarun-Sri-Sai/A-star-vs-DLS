from sys import setrecursionlimit, stdout, stdin
from random import randint
from time import perf_counter
from os import getcwd


setrecursionlimit(int(1e8))


INF = int(1e9)


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


class Input:
    def __init__(self):
        print('How do you want your input:\n\t1. Stdin\n\t2. File path')
        choice = int(input('\nEnter your choice: '))
        match choice:
            case 1:
                self.get_adjacency_list()

                self.start = input('Enter starting node: ')
                self.end = input('Enter destination node: ')
                self.depth = int(
                    input('Enter depth for depth limited search: '))

                self.get_heuristics()

            case 2:
                print('\n', getcwd(), sep='')
                with open(input('\nEnter file path: '), 'r') as file_in:
                    self.get_adjacency_list(file_in)

                    self.start = file_in.readline().strip()
                    self.end = file_in.readline().strip()
                    self.depth = int(file_in.readline().strip())

                    self.get_heuristics(file_in)

    def generate_random_adjacency_list(self):
        n_vertices = len(self.vertices)
        for vertex in self.vertices:
            self.adjacency_list[vertex] = {}

            for _ in range(randint(0, n_vertices - 1)):
                curr_vertex = self.vertices[randint(0, n_vertices - 1)]

                while curr_vertex == vertex or curr_vertex in self.adjacency_list[vertex]:
                    curr_vertex = self.vertices[randint(0, n_vertices - 1)]

                self.adjacency_list[vertex][curr_vertex] = randint(1, 99)

    def read_custom_adjacency_list(self, file_in=stdin):
        if file_in == stdin:
            print('\nEnter the adjacency list', end=' ')
            print(
                'format: \'vertex_name,weight\' pairs separated by space, \'None\' for empty list):')

        for vertex in self.vertices:
            if file_in == stdin:
                print(f'For {vertex}: ', end='')
                stdout.flush()

            line = file_in.readline().strip()

            self.adjacency_list[vertex] = {}

            if line == 'None':
                continue

            pairs = line.split()

            for pair in pairs:
                comma_sep_fields = pair.split(sep=',')
                self.adjacency_list[vertex][comma_sep_fields[0]] = int(
                    comma_sep_fields[1])

    def get_adjacency_list(self, file_in=stdin):
        if file_in == stdin:
            print('Enter number of vertices: ', end='')
            stdout.flush()

        n_vertices = int(file_in.readline().strip())

        if n_vertices > 26:
            return

        self.vertices = [chr(i + 65) for i in range(n_vertices)]
        print(f'Vertices: {self.vertices}\n')

        self.adjacency_list = {}

        if file_in == stdin:
            print(
                'How do you want your graph:\n\t1. Randomly generated\n\t2. Custom input')
            print('\nEnter your Choice: ', end='')
            stdout.flush()

        choice = int(file_in.readline().strip())

        match choice:
            case 1:
                self.generate_random_adjacency_list()

            case 2:
                self.read_custom_adjacency_list(file_in)

        self.print_graph()

    def print_graph(self):
        print('\nGraph:')
        for vertex in self.vertices:
            print(f'{vertex}: ', end='')
            if not self.adjacency_list[vertex]:
                print('{}')
                continue

            i_max = len(self.adjacency_list[vertex]) - 1

            print('{', end='')
            for i, (neighbor, weight) in enumerate(self.adjacency_list[vertex].items()):
                print(f'{neighbor}: {weight:3d}', end='')
                if i == i_max:
                    print('}')
                else:
                    print(', ', end='')

                stdout.flush()

        print()

    def get_heuristics(self, file_in=stdin):
        self.heuristics = {}

        if file_in == stdin:
            print(
                '\nHow do you want your heuristics:\n\t1. Calculated\n\t2. Custom input')
            print('\nEnter your Choice: ', end='')
            stdout.flush()

        choice = int(file_in.readline().strip())

        match choice:
            case 1:
                for vertex in self.vertices:
                    if vertex == self.end:
                        self.heuristics[vertex] = 0
                        continue

                    self.heuristics[vertex] = self.find_heuristic(vertex)

            case 2:
                for vertex in self.vertices:
                    if file_in == stdin:
                        print(f'Enter heuristic for {vertex}: ', end='')
                        stdout.flush()

                    self.heuristics[vertex] = int(file_in.readline().strip())

        self.print_heuristics()

    def print_heuristics(self):
        print('\nHeuristics:\t', end='')
        for i, vertex in enumerate(self.vertices):
            print(
                f'({vertex}: ', f'{self.heuristics[vertex]:3d})' if self.heuristics[vertex] < INF else 'INF)', sep='', end='')
            if (i + 1) % 7 != 0 and i < len(self.vertices) - 1:
                print(', ', end='')
            else:
                print('\n\t\t', end='')
            stdout.flush()

    def find_heuristic(self, start):
        queue = [start]
        visited = set(start)
        dist = 0

        while queue:
            size = len(queue)

            for _ in range(size):
                node = queue.pop(0)
                if node == self.end:
                    return dist * 10

                for neighbor in self.adjacency_list[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            dist += 1

        return INF


def main():
    input = Input()

    graph = AStarVsDLS(input.adjacency_list, input.heuristics)

    print()

    start_time = perf_counter() * 1e6
    a_star_success = graph.a_star_algorithm(input.start, input.end)
    end_time_a_star = perf_counter() * 1e6 - start_time

    if a_star_success:
        i_max = len(graph.a_star_path) - 1

        print('Path found using A-star search!\t\t', end='')
        stdout.flush()
        for i, vertex in enumerate(graph.a_star_path):
            print(vertex, sep='', end='')
            if i == i_max:
                print('\n')
            else:
                print(' -> ', end='')
            stdout.flush()
    else:
        print('Path not found using A-star search!')

    start_time = perf_counter() * 1e6
    dls_success = graph.depth_limited_search(
        input.start, input.end, input.depth)
    end_time_dls = perf_counter() * 1e6 - start_time

    if dls_success:
        i_max = len(graph.dls_path) - 1

        print('Path found using Depth Limited search!\t', end='')
        stdout.flush()
        for i, vertex in enumerate(graph.dls_path):
            print(vertex, sep='', end='')
            if i == i_max:
                print('\n')
            else:
                print(' -> ', end='')
            stdout.flush()
    else:
        print('Path not found using Depth Limited search!')

    print('\n', '=' * 30, ' Algorithm Analysis ', '=' * 30, sep='')
    print(f'\nA-star search took\t\t\t\t{end_time_a_star:3.2f} microseconds')
    print(f'Depth Limited search took\t\t\t{end_time_dls:3.2f} microseconds')
    print('\n', '=' * 80, sep='')

    diff = end_time_dls - end_time_a_star
    if diff < 0:
        print(
            f'Depth Limited search was faster by\t\t{-diff:3.2f} microseconds')
    elif diff > 0:
        print(f'A-star search was faster by\t\t\t{diff:3.2f} microseconds')
    else:
        print('Both searches finished at the same time')

    print('=' * 80)
    print(f'\nA-star search visits\t\t\t\t{graph.a_star_count}')
    print(f'Depth Limited search visits\t\t\t{graph.dls_count}')
    print('\n', '=' * 80, sep='')

    diff = graph.a_star_count - graph.dls_count
    if diff < 0:
        print(f'A-star search beats Depth Limited search by\t{-diff} visits')
    else:
        print(f'Depth Limited search beats A-star search by\t{diff} visits')

    print('=' * 80)

    a_star_cost = sum(graph.adjacency_list[graph.a_star_path[i]][graph.a_star_path[i + 1]]
                      for i in range(len(graph.a_star_path) - 1))
    dls_cost = sum(graph.adjacency_list[graph.dls_path[i]][graph.dls_path[i + 1]]
                   for i in range(len(graph.dls_path) - 1))

    print(f'\nA-star search found a path that costs\t\t{a_star_cost}')
    print(f'Depth Limited search found a path that costs\t{dls_cost}')
    print('\n', '=' * 80, sep='')

    diff = a_star_cost - dls_cost
    if diff < 0:
        print(f'A-star search found a path cheaper by\t\t{-diff}')
    elif diff > 0:
        print(f'Depth Limited search found a path cheaper by\t{diff}')
    else:
        print(f'Both searches found the same path')

    print('=' * 80)


if __name__ == '__main__':
    main()
