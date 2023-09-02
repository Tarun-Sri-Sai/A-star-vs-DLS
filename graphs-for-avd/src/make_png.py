from os import system, listdir, path, mkdir


def main():
    dots_path = path.join('..','dots')
    pngs_path = path.join('..','pngs')
    if not path.isdir(pngs_path):
        mkdir(pngs_path)
    files = listdir(path.join('..','dots'))
    for file in files:
        file_name = path.splitext(file)[0]
        dot_file = path.join(dots_path, f'{file_name}.dot')
        png_file = path.join(pngs_path, f'{file_name}.png')
        system(f'dot -Tpng {dot_file} > {png_file}')


if __name__ == '__main__':
    main()
