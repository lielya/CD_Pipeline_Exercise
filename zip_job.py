from zipfile import ZipFile

VERSION = "1.2.0"


def main():
    files_names_to_create = ["a", "b", "c", "d"]
    for file_name in files_names_to_create:
        create_zip_with_text_file(file_name)


def create_zip_with_text_file(file_name: str):
    txt_file_name = f"{file_name}.txt"
    try:
        create_txt_file(txt_file_name)
        create_zip_file(txt_file_name)

    except OSError:
        print(f"There is a problem creating the file: {file_name}")


def create_txt_file(file_name: str):
    with open(file_name, "w") as text_file:
        text_file.write("example")


def create_zip_file(content_file_name: str):
    content_file_prefix = ".".join(content_file_name.split(".")[:-1])
    zip_file_name = f"{content_file_prefix}_{VERSION}.zip"
    with ZipFile(zip_file_name, "w") as zip_file:
        zip_file.write(content_file_name)


if __name__ == "__main__":
    main()
