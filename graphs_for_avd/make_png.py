from os import listdir, system
from os.path import join, splitext
from dir_create import make_new_dir


def main():
    dots_path = join('graphs_for_avd', 'dots')
    pngs_path = join('graphs_for_avd', 'pngs')
    make_new_dir(pngs_path)
    for file in listdir(dots_path):
        file_name = splitext(file)[0]
        dot_file = join(dots_path, f'{file_name}.dot')
        png_file = join(pngs_path, f'{file_name}.png')
        system(f'dot -Tpng {dot_file} > {png_file}')


if __name__ == '__main__':
    main()
