import os
import random
import shutil
import random_adj


def main():
    valid_n_vertices_list = list(range(5, 27))
    n_vertices_list = set()
    while len(n_vertices_list) < 3:
        n_vertices_list.add(random.choice(valid_n_vertices_list))
    n_vertices_list = list(n_vertices_list)
    graphs_dir = os.path.join('..', 'graphs')
    if os.path.isdir(graphs_dir):
        shutil.rmtree(graphs_dir)
    os.mkdir(graphs_dir)
    for n_vertices in n_vertices_list:
        with open(os.path.join(graphs_dir, f'{n_vertices}_nodes.txt'), 'w') as fwrite:
            print(f'{n_vertices}', file=fwrite)
            print(f'{2}', file=fwrite)

            vertices = [chr(i + 65) for i in range(n_vertices)]
            adjacency_list = random_adj.generate_random_adjacency_list(
                vertices)
            for _, neighbors in adjacency_list.items():
                if len(neighbors) == 0:
                    print('None', file=fwrite)
                    continue
                print(' '.join([f'{k},{v}' for k, v in neighbors.items()]),
                      file=fwrite)

            start = random.choice(vertices)
            print(f'{start}', file=fwrite)
            while (end := random.choice(vertices)) == start:
                ...
            print(f'{end}', file=fwrite)
            print(f'{random.randint(5, n_vertices)}', file=fwrite)
            print(f'{1}', file=fwrite)


if __name__ == '__main__':
    main()
