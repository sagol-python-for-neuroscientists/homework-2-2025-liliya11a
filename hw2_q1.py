MORSE_CODE = {
    'A': '.-',     'B': '-...',   'C': '-.-.',  'D': '-..',
    'E': '.',      'F': '..-.',   'G': '--.',   'H': '....',
    'I': '..',     'J': '.---',   'K': '-.-',   'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',   'P': '.--.',
    'Q': '--.-',   'R': '.-.',    'S': '...',   'T': '-',
    'U': '..-',    'V': '...-',   'W': '.--',   'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---', '3': '...--',
    '4': '....-',  '5': '.....',  '6': '-....', '7': '--...',
    '8': '---..',  '9': '----.',
    '.': '.-.-.-', ',': '--..--', ':': '---...', "'": '.----.',
    '-': '-....-',
}


def english_to_morse(
    input_file: str = "lorem.txt",
    output_file: str = "lorem_morse.txt"
):
    """Convert lorem.txt → lorem_morse.txt, one Morse-word per line,
    preserving blank lines exactly.

    Parameters
    ----------
    input_file : str
        Path to the text file to convert.
    output_file : str
        Path where the Morse output will be written.
    """
    # 1. Read entire file and uppercase it so keys match MORSE_CODE:
    with open(input_file, 'r') as infile:
        text = infile.read().upper()

    # 2. Split on '\n' (not splitlines) so empty lines become '' entries in `lines`:
    lines = text.split('\n')

    # 3. For each input line:
    #    - if it's empty, append '' to output (a blank line)
    #    - otherwise, split into words and convert each word → one Morse string
    output_lines = []
    for line in lines:
        if line == "":
            # preserve blank line
            output_lines.append("")
        else:
            # for each word, join the letters’ codes *without* spaces
            for word in line.split():
                morse_word = "".join(
                    MORSE_CODE.get(char, "") for char in word
                )
                output_lines.append(morse_word)

    # 4. Write them back joined by '\n', *without* an extra trailing newline:
    with open(output_file, 'w') as outfile:
        outfile.write("\n".join(output_lines))


if __name__ == '__main__':
    # run it on the default files
    english_to_morse()
