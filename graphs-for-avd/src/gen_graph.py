from os import listdir, path, mkdir


def main():
    graphs_path: str = path.join('..', '..', 'a-star-vs-dls', 'graphs')
    files: list[str] = listdir(graphs_path)
    dots_path: str = path.join('..', 'dots')
    if not path.isdir(dots_path):
        mkdir(dots_path)
    for file in files:
        with open(path.join(dots_path, path.splitext(file)[0] + '.dot'), 'w') as writer:
            printed: str = 'digraph {\n'
            with open(path.join(graphs_path, file), 'r') as reader:
                nnodes: int = int(reader.readline().strip())
                reader.readline()
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
