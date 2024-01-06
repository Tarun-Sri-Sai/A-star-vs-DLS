from random import randint


def generate_random_adjacency_list(vertices):
    n_vertices = len(vertices)
    adjacency_list = {}
    for vertex in vertices:
        adjacency_list[vertex] = {}

        for _ in range(randint(0, n_vertices - 1)):
            curr_vertex = vertices[randint(0, n_vertices - 1)]

            while curr_vertex == vertex or curr_vertex in adjacency_list[vertex]:
                curr_vertex = vertices[randint(0, n_vertices - 1)]

            adjacency_list[vertex][curr_vertex] = randint(1, 99)

    return adjacency_list
