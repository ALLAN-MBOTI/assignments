

from pathlib import Path


def modify_content(content: str) -> str:
    return content.upper()


def read_file(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def write_file(filename: str, content: str) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def main() -> None:
    """Main program execution."""
    filename = input("Enter the filename to read: ").strip()
    try:
        # Read original file
        original_content = read_file(filename)

        # Modify the content
        modified_content = modify_content(original_content)

        # Create output filename
        output_file = Path(filename).stem + "_modified.txt"

        # Write the modified content to a new file
        write_file(output_file, modified_content)

        print(f"File successfully modified and saved as '{output_file}'.")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: Unable to read the file.")


if __name__ == "__main__":
    main()
