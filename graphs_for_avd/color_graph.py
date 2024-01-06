from os import listdir
from os.path import join, splitext, exists


def get_path(file):
    if exists(file):
        with open(file, 'r') as f:
            graph_path = f.read().strip()

        path_nodes = graph_path.split(' -> ')
        path_list = []

        for i in range(len(path_nodes) - 1):
            path_list.append((path_nodes[i], path_nodes[i + 1]))
        return set(path_list)

    return set()


def write_dot(path_set, read_file, dot_file):
    with open(dot_file, 'w') as writer:
        with open(read_file, 'r') as reader:
            for line in reader.readlines():
                line = line.strip()

                if line == '}' or line == 'digraph {\nlabel: \'A-star\'\n':
                    writer.write('\t' + line + '\n')
                    continue

                if (line[0:1], line[5:6]) not in path_set:
                    writer.write('\t' + line + '\n')
                    continue

                writer.write('\t' + line[0:-1] + ', color="red"]' + '\n')


def main():
    dir_path = join('graphs_for_avd', 'dots')
    files = listdir(dir_path)
    for file in files:
        paths_dir = join('a_star_vs_dls', 'paths')
        file_1 = join(paths_dir, f'{splitext(file)[0]}_1.txt')

        path_set = get_path(file_1)
        c1_dot_file = join(dir_path, splitext(file)[0] + '_c1.dot')
        write_dot(path_set, join(dir_path, file), c1_dot_file)

        file_2 = join(paths_dir, f'{splitext(file)[0]}_2.txt')

        path_set = get_path(file_2)
        c2_dot_file = join(dir_path, splitext(file)[0] + '_c2.dot')
        write_dot(path_set, join(dir_path, file), c2_dot_file)


if __name__ == '__main__':
    main()
