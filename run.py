from a_star_vs_dls.write_graph import write_graph
from a_star_vs_dls.main import main as run
from graphs_for_avd.gen_graph import main as gen_graph
from graphs_for_avd.color_graph import main as color_graph
from graphs_for_avd.make_png import main as make_png
from sys import argv, exit


def is_valid(vertex):
    return isinstance(vertex, int) and 1 <= vertex <= 26


def parse_arguments():
    if len(argv) != 4:
        print('Enter no. of vertices for 3 graphs')
        exit()
    
    vertices = [int(x) for x in argv[1:]]

    if len(vertices) > len(set(vertices)):
        print('No. of vertices must be unique')
        exit()
    
    if any(not is_valid(x) for x in vertices):
        print('No. of vertices should be integers in the range 1 to 26')
        exit()
    
    return vertices


def main():
    write_graph(parse_arguments())
    run()
    
    gen_graph()
    color_graph()
    make_png()


if __name__ == '__main__':
    main()
