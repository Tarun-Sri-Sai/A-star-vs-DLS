from os import listdir, path


def main():
    dir_path: str = path.join('..', 'dots')
    files: list[str] = listdir(dir_path)

    for file in files:
        print(file)
        graph_path: str = input('graph path1: ')
        path_nodes: list[str] = graph_path.split(' -> ')
        path_list: list[tuple[str, str]] = []
        for i in range(len(path_nodes) - 1):
            path_list.append((path_nodes[i], path_nodes[i + 1]))

        path_set = set(path_list)

        with open(path.join(dir_path, path.splitext(file)[0] + '_c1.dot'), 'w') as writer:
            with open(path.join(dir_path, file), 'r') as reader:
                for line in reader.readlines():
                    line = line.strip()
                    if line == '}' or line == 'digraph {\nlabel: \'A-star\'\n':
                        writer.write('\t' + line + '\n')
                        continue

                    if (line[0:1], line[5:6]) not in path_set:
                        writer.write('\t' + line + '\n')
                        continue

                    writer.write('\t' + line[0:-1] + ', color=\'red\']' + '\n')

        graph_path: str = input('graph path2: ')
        path_nodes: list[str] = graph_path.split(' -> ')
        path_list: list[tuple[str, str]] = []
        for i in range(len(path_nodes) - 1):
            path_list.append((path_nodes[i], path_nodes[i + 1]))

        path_set = set(path_list)

        with open(path.join(dir_path, path.splitext(file)[0] + '_c2.dot'), 'w') as writer:
            with open(path.join(dir_path, file), 'r') as reader:
                for line in reader.readlines():
                    line = line.strip()
                    if line == '}' or line == 'digraph {\nlabel: \'DLS\'\n':
                        writer.write('\t' + line + '\n')
                        continue

                    if (line[0:1], line[5:6]) not in path_set:
                        writer.write('\t' + line + '\n')
                        continue

                    writer.write('\t' + line[0:-1] + ', color=\'red\']' + '\n')


if __name__ == '__main__':
    main()
