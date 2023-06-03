from typing import List
import os


def main():
    files: List[str] = os.listdir("graphs")
    for file in files:
        with open("dots/" + file[0:-3] + "dot", "w") as writer:
            printed: str = "digraph {\n"
            with open("graphs/" + file, "r") as reader:
                nnodes: int = int(reader.readline().strip())
                reader.readline()
                vertices: List[str] = [chr(0x41 + i) for i in range(nnodes)]
                for vertex in vertices:
                    for pair in reader.readline().strip().split():
                        if pair == "None": continue
                        neigh, wt = (pair.split(","))
                        printed += ("\t" + vertex + ' -> ' + neigh + f" [weight={(100 / float(wt)):.2f}]\n")
            printed += "}"
            writer.write(printed)


if __name__ == "__main__":
    main()
