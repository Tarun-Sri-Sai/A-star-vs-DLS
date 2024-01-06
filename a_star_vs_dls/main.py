from time import perf_counter
from os import listdir
from os.path import join, splitext
from a_star_vs_dls.input_parser import InputParser
from a_star_vs_dls.a_star_vs_dls import AStarVsDLS
from dir_create import make_new_dir


def print_path(path, file):
    i_max = len(path) - 1
    for i, vertex in enumerate(path):
        print(vertex, sep='', end='', file=file)

        if i == i_max:
            print('\n', file=file)
        else:
            print(' -> ', end='', file=file)


def log_a_star_path(a_star_success, a_star_path_file, graph, logs_writer):
    if a_star_success:
        print('Path found using A-star search!\t\t', end='',
              file=logs_writer)
        print_path(graph.a_star_path, logs_writer)

        with open(a_star_path_file, 'w') as f:
            print_path(graph.a_star_path, f)
    else:
        print('Path not found using A-star search!', file=logs_writer)


def log_dls_path(dls_success, dls_path_file, graph, logs_writer):
    if dls_success:
        print('Path found using Depth Limited search!\t', end='',
              file=logs_writer)
        print_path(graph.dls_path, logs_writer)
        with open(dls_path_file, 'w') as f:
            print_path(graph.dls_path, f)
    else:
        print('Path not found using Depth Limited search!',
              file=logs_writer)


def log_time_diff(end_time_a_star, end_time_dls, logs_writer):
    print(f'\nA-star search took\t\t\t\t{end_time_a_star:3.2f} microseconds',
          file=logs_writer)
    print(f'Depth Limited search took\t\t\t{end_time_dls:3.2f} microseconds',
          file=logs_writer)
    print('\n', '=' * 80, sep='', file=logs_writer)

    diff = end_time_dls - end_time_a_star
    if diff < 0:
        print(
            f'Depth Limited search was faster by\t\t{-diff:3.2f} microseconds',
            file=logs_writer)
    elif diff > 0:
        print(f'A-star search was faster by\t\t\t{diff:3.2f} microseconds',
              file=logs_writer)
    else:
        print('Both searches finished at the same time', file=logs_writer)
    print('=' * 80, file=logs_writer)


def log_visits_diff(graph, logs_writer):
    print(f'\nA-star search visits\t\t\t\t{graph.a_star_count}',
          file=logs_writer)
    print(f'Depth Limited search visits\t\t\t{graph.dls_count}',
          file=logs_writer)
    print('\n', '=' * 80, sep='', file=logs_writer)

    diff = graph.a_star_count - graph.dls_count
    if diff < 0:
        print(f'A-star search beats Depth Limited search by\t{-diff} visits',
              file=logs_writer)
    else:
        print(f'Depth Limited search beats A-star search by\t{diff} visits',
              file=logs_writer)
    print('=' * 80, file=logs_writer)


def log_cost_diff(a_star_cost, dls_cost, logs_writer):
    print(f'\nA-star search found a path that costs\t\t{a_star_cost}',
          file=logs_writer)
    print(f'Depth Limited search found a path that costs\t{dls_cost}',
          file=logs_writer)
    print('\n', '=' * 80, sep='', file=logs_writer)

    diff = a_star_cost - dls_cost
    if diff < 0:
        print(f'A-star search found a path cheaper by\t\t{-diff}',
              file=logs_writer)
    elif diff > 0:
        print(f'Depth Limited search found a path cheaper by\t{diff}',
              file=logs_writer)
    else:
        print(f'Both searches found the same path', file=logs_writer)
    print('=' * 80, file=logs_writer)


def run_logs(file_in, logs_writer, paths_dir):
    input = InputParser(file_in, logs_writer)
    graph = AStarVsDLS(input.adjacency_list, input.heuristics)

    print('', file=logs_writer)

    start_time = perf_counter() * 1e6
    a_star_success = graph.a_star_algorithm(input.start, input.end)
    end_time_a_star = perf_counter() * 1e6 - start_time

    n_vertices = len(input.vertices)
    a_star_path_file = join(paths_dir, f'{n_vertices}_nodes_1.txt')

    log_a_star_path(a_star_success, a_star_path_file, graph, logs_writer)

    start_time = perf_counter() * 1e6
    dls_success = graph.depth_limited_search(
        input.start, input.end, input.depth)
    end_time_dls = perf_counter() * 1e6 - start_time
    dls_path_file = join(paths_dir, f'{n_vertices}_nodes_2.txt')

    log_dls_path(dls_success, dls_path_file, graph, logs_writer)

    print('\n', '=' * 30, ' Algorithm Analysis ', '=' * 30, sep='',
          file=logs_writer)

    log_time_diff(end_time_a_star, end_time_dls, logs_writer)

    log_visits_diff(graph, logs_writer)

    a_star_cost = sum(
        graph.adjacency_list[graph.a_star_path[i]][graph.a_star_path[i + 1]]
        for i in range(len(graph.a_star_path) - 1))
    dls_cost = sum(
        graph.adjacency_list[graph.dls_path[i]][graph.dls_path[i + 1]]
        for i in range(len(graph.dls_path) - 1))

    log_cost_diff(a_star_cost, dls_cost, logs_writer)


def main():
    graphs_dir = join('a_star_vs_dls', 'graphs')

    logs_dir = join('a_star_vs_dls', 'logs')
    make_new_dir(logs_dir)

    paths_dir = join('a_star_vs_dls', 'paths')
    make_new_dir(paths_dir)

    for file in listdir(graphs_dir):
        with open(join(graphs_dir, file), 'r') as file_in:
            file_name = splitext(file)[0]
            with open(join(logs_dir, f'{file_name}.log'), 'w') as logs_writer:
                run_logs(file_in, logs_writer, paths_dir)


if __name__ == '__main__':
    main()
