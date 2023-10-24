import os
import dir_create


def main():
    dots_path = os.path.join('..', 'dots')
    pngs_path = os.path.join('..', 'pngs')
    dir_create.make_new_dir(pngs_path)
    for file in os.listdir(dots_path):
        file_name = os.path.splitext(file)[0]
        dot_file = os.path.join(dots_path, f'{file_name}.dot')
        png_file = os.path.join(pngs_path, f'{file_name}.png')
        os.system(f'dot -Tpng {dot_file} > {png_file}')


if __name__ == '__main__':
    main()
