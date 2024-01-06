from os import listdir
from os.path import join, splitext, exists


def main():
    dir_path = join('graphs_for_avd', 'dots')
    files = listdir(dir_path)
    for file in files:
        paths_dir = join('a_star_vs_dls', 'paths')
        file_1 = join(paths_dir, f'{splitext(file)[0]}_1.txt')

        if exists(file_1):
            with open(file_1, 'r') as f:
                graph_path = f.read().strip()

            path_nodes = graph_path.split(' -> ')
            path_list = []

            for i in range(len(path_nodes) - 1):
                path_list.append((path_nodes[i], path_nodes[i + 1]))
            path_set = set(path_list)
        else:
            path_set = set()

        with open(join(dir_path, splitext(file)[0] + '_c1.dot'), 'w') as writer:
            with open(join(dir_path, file), 'r') as reader:
                for line in reader.readlines():
                    line = line.strip()

                    if line == '}' or line == 'digraph {\nlabel: \'A-star\'\n':
                        writer.write('\t' + line + '\n')
                        continue

                    if (line[0:1], line[5:6]) not in path_set:
                        writer.write('\t' + line + '\n')
                        continue

                    writer.write('\t' + line[0:-1] + ', color="red"]' + '\n')

        file_2 = join(paths_dir, f'{splitext(file)[0]}_2.txt')

        if exists(file_2):
            with open(file_2, 'r') as f:
                graph_path = f.read().strip()

            path_nodes = graph_path.split(' -> ')
            path_list = []

            for i in range(len(path_nodes) - 1):
                path_list.append((path_nodes[i], path_nodes[i + 1]))
            path_set = set(path_list)
        else:
            path_set = set()

        with open(join(dir_path, splitext(file)[0] + '_c2.dot'), 'w') as writer:
            with open(join(dir_path, file), 'r') as reader:
                for line in reader.readlines():
                    line = line.strip()

                    if line == '}' or line == 'digraph {\nlabel: \'DLS\'\n':
                        writer.write('\t' + line + '\n')
                        continue

                    if (line[0:1], line[5:6]) not in path_set:
                        writer.write('\t' + line + '\n')
                        continue

                    writer.write('\t' + line[0:-1] + ', color="red"]' + '\n')


if __name__ == '__main__':
    main()
