import os


def main():
    files = os.listdir("dots")
    for file in files:
        file_name = file[0:-4]
        os.system(f"dot -Tpng dots/{file_name}.dot > pngs/{file_name}.png")

if __name__ == "__main__":
    main()