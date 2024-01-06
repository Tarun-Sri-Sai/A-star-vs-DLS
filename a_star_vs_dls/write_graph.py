from dir_create import make_new_dir
from os.path import join
from random import choice, randint
from a_star_vs_dls.random_adj import generate_random_adjacency_list


def main():
    valid_n_vertices_list = list(range(5, 27))
    n_vertices_list = set()
    while len(n_vertices_list) < 3:
        n_vertices_list.add(choice(valid_n_vertices_list))
    n_vertices_list = list(n_vertices_list)
    graphs_dir = join('a_star_vs_dls', 'graphs')
    make_new_dir(graphs_dir)
    for n_vertices in n_vertices_list:
        with open(join(graphs_dir, f'{n_vertices}_nodes.txt'), 'w') as fwrite:
            print(f'{n_vertices}', file=fwrite)

            vertices = [chr(i + 65) for i in range(n_vertices)]
            adjacency_list = generate_random_adjacency_list(
                vertices)
            for _, neighbors in adjacency_list.items():
                if len(neighbors) == 0:
                    print('None', file=fwrite)
                    continue
                print(' '.join([f'{k},{v}' for k, v in neighbors.items()]),
                      file=fwrite)

            start = choice(vertices)
            print(f'{start}', file=fwrite)
            while (end := choice(vertices)) == start:
                pass
            print(f'{end}', file=fwrite)
            print(f'{randint(5, n_vertices)}', file=fwrite)


if __name__ == '__main__':
    main()
