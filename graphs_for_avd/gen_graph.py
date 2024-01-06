from os.path import join, splitext
from os import listdir
from dir_create import make_new_dir


def write_to(writer, graphs_path, file):
    printed = 'digraph {\n'

    with open(join(graphs_path, file), 'r') as reader:
        nnodes = int(reader.readline().strip())
        vertices = [chr(0x41 + i) for i in range(nnodes)]

        for vertex in vertices:

            for pair in reader.readline().strip().split():
                if pair == 'None':
                    continue

                neigh, wt = (pair.split(','))
                printed += ('\t' + vertex + ' -> ' + neigh +
                            f' [weight={(100 / float(wt)):.2f}]\n')

    printed += '}'
    writer.write(printed)


def main():
    graphs_path = join('a_star_vs_dls', 'graphs')
    files = listdir(graphs_path)

    dots_path = join('graphs_for_avd', 'dots')
    make_new_dir(dots_path)

    for file in files:
        with open(join(dots_path, splitext(file)[0] + '.dot'), 'w') as writer:
            write_to(writer, graphs_path, file)


if __name__ == '__main__':
    main()
