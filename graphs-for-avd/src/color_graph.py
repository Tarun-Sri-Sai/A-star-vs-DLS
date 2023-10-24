import os


def main():
    dir_path: str = os.path.join('..', 'dots')
    files: list[str] = os.listdir(dir_path)
    for file in files:
        paths_dir = os.path.join('..', '..', 'a-star-vs-dls', 'paths')
        file_1 = os.path.join(paths_dir, f'{os.path.splitext(file)[0]}_1.txt')
        if os.path.exists(file_1):
            with open(file_1, 'r') as f:
                graph_path: str = f.read().strip()
            path_nodes: list[str] = graph_path.split(' -> ')
            path_list: list[tuple[str, str]] = []
            for i in range(len(path_nodes) - 1):
                path_list.append((path_nodes[i], path_nodes[i + 1]))
            path_set = set(path_list)
        else:
            path_set = set()
        with open(os.path.join(dir_path, os.path.splitext(file)[0] + '_c1.dot'), 'w') as writer:
            with open(os.path.join(dir_path, file), 'r') as reader:
                for line in reader.readlines():
                    line = line.strip()
                    if line == '}' or line == 'digraph {\nlabel: \'A-star\'\n':
                        writer.write('\t' + line + '\n')
                        continue
                    if (line[0:1], line[5:6]) not in path_set:
                        writer.write('\t' + line + '\n')
                        continue
                    writer.write('\t' + line[0:-1]
                                 + ', color="red"]' + '\n')
        file_2 = os.path.join(paths_dir, f'{os.path.splitext(file)[0]}_2.txt')
        if os.path.exists(file_2):
            with open(file_2, 'r') as f:
                graph_path: str = f.read().strip()
            path_nodes: list[str] = graph_path.split(' -> ')
            path_list: list[tuple[str, str]] = []
            for i in range(len(path_nodes) - 1):
                path_list.append((path_nodes[i], path_nodes[i + 1]))
            path_set = set(path_list)
        else:
            path_set = set()
        with open(os.path.join(dir_path, os.path.splitext(file)[0] + '_c2.dot'), 'w') as writer:
            with open(os.path.join(dir_path, file), 'r') as reader:
                for line in reader.readlines():
                    line = line.strip()
                    if line == '}' or line == 'digraph {\nlabel: \'DLS\'\n':
                        writer.write('\t' + line + '\n')
                        continue
                    if (line[0:1], line[5:6]) not in path_set:
                        writer.write('\t' + line + '\n')
                        continue
                    writer.write('\t' + line[0:-1]
                                 + ', color="red"]' + '\n')


if __name__ == '__main__':
    main()
