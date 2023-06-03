import os
from typing import List, Tuple


def main():
    files: List[str] = os.listdir("dots")

    for file in files:
        print(file)
        path: str = input("graph path1: ")
        path_nodes: List[str] = path.split(" -> ")
        path_list: List[Tuple[str, str]] = []
        for i in range(len(path_nodes) - 1):
            path_list.append((path_nodes[i], path_nodes[i + 1]))
        
        path_set = set(path_list)

        with open("dots/" + file[0:-4] + "_c1.dot", "w") as writer:
            with open("dots/" + file, "r") as reader:
                for line in reader.readlines():
                    line = line.strip()
                    if line == "}" or line == "digraph {\nlabel: \"A-star\"\n":
                        writer.write("\t" + line + "\n")
                        continue

                    if (line[0:1], line[5:6]) not in path_set:
                        writer.write("\t" + line + "\n")
                        continue

                    writer.write("\t" + line[0:-1] + ", color=\"red\"]" + '\n')

        path: str = input("graph path2: ")
        path_nodes: List[str] = path.split(" -> ")
        path_list: List[Tuple[str, str]] = []
        for i in range(len(path_nodes) - 1):
            path_list.append((path_nodes[i], path_nodes[i + 1]))
        
        path_set = set(path_list)

        with open("dots/" + file[0:-4] + "_c2.dot", "w") as writer:
            with open("dots/" + file, "r") as reader:
                for line in reader.readlines():
                    line = line.strip()
                    if line == "}" or line == "digraph {\nlabel: \"DLS\"\n":
                        writer.write("\t" + line + "\n")
                        continue

                    if (line[0:1], line[5:6]) not in path_set:
                        writer.write("\t" + line + "\n")
                        continue

                    writer.write("\t" + line[0:-1] + ", color=\"red\"]" + '\n')




if __name__ == "__main__":
    main()