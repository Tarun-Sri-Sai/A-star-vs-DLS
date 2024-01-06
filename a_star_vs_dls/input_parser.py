from sys import stdin


INF = int(1e9)


class InputParser:
    def __init__(self, file_in, logs_writer):
        self.file_in = file_in
        self.logs_writer = logs_writer

        self.get_adjacency_list()

        self.start = self.file_in.readline().strip()
        self.end = file_in.readline().strip()
        self.depth = int(self.file_in.readline().strip())

        self.get_heuristics()

    def read_custom_adjacency_list(self):
        for vertex in self.vertices:
            if self.file_in == stdin:
                print(f'For {vertex}: ', end='')

            line = self.file_in.readline().strip()
            self.adjacency_list[vertex] = {}

            if line == 'None':
                continue

            pairs = line.split()
            for pair in pairs:
                cs_fields = pair.split(sep=',')
                self.adjacency_list[vertex][cs_fields[0]] = int(cs_fields[1])

    def get_adjacency_list(self):
        n_vertices = int(self.file_in.readline().strip())
        if n_vertices > 26:
            return

        self.vertices = [chr(i + 65) for i in range(n_vertices)]
        self.adjacency_list = {}

        self.read_custom_adjacency_list()
        self.print_graph()

    def print_graph(self):
        print('\nGraph:', file=self.logs_writer)
        for vertex in self.vertices:
            print(f'{vertex}: ', end='', file=self.logs_writer)

            if not self.adjacency_list[vertex]:
                print('{}', file=self.logs_writer)
                continue

            i_max = len(self.adjacency_list[vertex]) - 1
            print('{', end='', file=self.logs_writer)

            neighbors = self.adjacency_list[vertex].items()

            for i, (neighbor, weight) in enumerate(neighbors):
                print(f'{neighbor}: {weight:3d}', end='',
                      file=self.logs_writer)

                if i == i_max:
                    print('}', file=self.logs_writer)
                else:
                    print(', ', end='', file=self.logs_writer)

        print('', file=self.logs_writer)

    def get_heuristics(self):
        self.heuristics = {}
        for vertex in self.vertices:
            if vertex == self.end:
                self.heuristics[vertex] = 0
                continue

            self.heuristics[vertex] = self.find_heuristic(vertex)

        self.print_heuristics()

    def print_heuristics(self):
        print('\nHeuristics:\t', end='', file=self.logs_writer)
        for i, vertex in enumerate(self.vertices):
            print(f'({vertex}: ',
                  f'{self.heuristics[vertex]:3d})'
                  if self.heuristics[vertex] < INF else 'INF)',
                  sep='',
                  end='',
                  file=self.logs_writer)

            if (i + 1) % 7 != 0 and i < len(self.vertices) - 1:
                print(', ', end='', file=self.logs_writer)
            else:
                print('\n\t\t', end='', file=self.logs_writer)

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
