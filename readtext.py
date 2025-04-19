def read_text_file(filename):
    """
    Reads the contents of a text file and returns it as a string.

    Parameters:
        filename (str): The name or path of the text file to be read.

    Returns:
        str: The contents of the file as a string if it exists,
             otherwise an empty string if the file cannot be found.

    Example usage:
        contents = read_text_file("example.txt")
        print(contents)
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return ""
filename = 'opening29.txt'    # change this to match your filename
story = read_text_file(filename)
if story != "":
    print(story)
else:
    print("Story is blank")