class InvalidFileFormatError(Exception):
    pass


class InvalidDataError(Exception):
    pass


def read_file(filename):
    file = None

    try:
        if not filename.endswith(".txt"):
            raise InvalidFileFormatError(
                "Only .txt files are allowed."
            )

        file = open(filename, "r")

        data = file.read()

        if data.strip() == "":
            raise InvalidDataError(
                "File does not contain valid data."
            )

        print("File content:")
        print(data)

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except InvalidFileFormatError as e:
        print("Error:", e)

    except InvalidDataError as e:
        print("Error:", e)

    finally:
        if file:
            file.close()

        print("File operation completed.")


filename = input("Enter file name: ")

read_file(filename)