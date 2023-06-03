from os import system, listdir, path


def main():
    files = listdir('dots')
    for file in files:
        file_name = path.splitext(file)[0]
        system(f'dot -Tpng dots/{file_name}.dot > pngs/{file_name}.png')


if __name__ == '__main__':
    main()
