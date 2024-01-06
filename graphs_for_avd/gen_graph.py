from os.path import join, splitext
from os import listdir
from dir_create import make_new_dir


def main():
    graphs_path: str = join('a_star_vs_dls', 'graphs')
    files: list[str] = listdir(graphs_path)
    dots_path: str = join('graphs_for_avd', 'dots')
    make_new_dir(dots_path)
    for file in files:
        with open(join(dots_path, splitext(file)[0] + '.dot'), 'w') as writer:
            printed: str = 'digraph {\n'
            with open(join(graphs_path, file), 'r') as reader:
                nnodes: int = int(reader.readline().strip())
                vertices: list[str] = [chr(0x41 + i) for i in range(nnodes)]
                for vertex in vertices:
                    for pair in reader.readline().strip().split():
                        if pair == 'None':
                            continue
                        neigh, wt = (pair.split(','))
                        printed += ('\t' + vertex + ' -> ' + neigh +
                                    f' [weight={(100 / float(wt)):.2f}]\n')
            printed += '}'
            writer.write(printed)


if __name__ == '__main__':
    main()
