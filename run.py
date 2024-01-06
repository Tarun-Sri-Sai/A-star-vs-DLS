from a_star_vs_dls.write_graph import main as write_graph
from a_star_vs_dls.main import main as run
from graphs_for_avd.gen_graph import main as gen_graph
from graphs_for_avd.color_graph import main as color_graph
from graphs_for_avd.make_png import main as make_png


def main():
    write_graph()
    run()
    
    gen_graph()
    color_graph()
    make_png()


if __name__ == '__main__':
    main()
