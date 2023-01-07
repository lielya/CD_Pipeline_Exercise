from zipfile import ZipFile

VERSION = '1.2.0'
TXT_SUFFIX = '.txt'
ZIP_SUFFIX = '.zip'


def main():
    arr = ['a', 'b', 'c', 'd']
    for file in arr:
        txt_file = f'{file}{TXT_SUFFIX}'

        try:
            create_txt_files(txt_file)
            create_zip_files(file, txt_file)

        except FileNotFoundError:
            print("There is a problem creating this file")


def create_txt_files(file):
    new_file = open(file, 'w')


def create_zip_files(file, txt_file):
    zip_file_name = f'{file}_{VERSION}{ZIP_SUFFIX}'
    with ZipFile(zip_file_name, 'w') as zip_file:
        zip_file.write(txt_file)


if __name__ == '__main__':
    main()
