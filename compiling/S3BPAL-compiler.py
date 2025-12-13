import json
from pathlib import Path
import sys

def main():
    ## Load commands
    with open('commands.json', 'r') as file:
        commands = json.load(file)

    ## Load source code
    source_path = sys.argv[1]
    source_code = []
    if Path(source_path).exists():
        with open(source_path, 'r') as file:
            for line in file.readlines():
                line_split = line.strip().split('#')[0]
                if isinstance(line_split, tuple): code = line_split[0]
                else:                             code = line_split
                if not (code.strip() == ''):
                    source_code.append(code.strip().split(' '))
        print(source_code)
    else:
        print(f'File "{source_path}" not found!')
        quit()

    ## Compiling source code
    output_path = str(Path(source_path).stem) + ".pal"
    with open(output_path, 'w') as output:
        line_num = 0
        for command in source_code:
            compiled_line = ''
            compiled_line += commands[command[0]]["module"].replace(' ', '') + " "
            compiled_line += commands[command[0]]["cmd"].replace(' ', '')

            args_expected = commands[command[0]]["args"]
            i = 0
            for argument in args_expected:
                if '[' in command[i+1]:
                    compiled_line += " " + format((line_num + int(command[i+1].replace(' ', '').replace('[', '').replace(']', '').strip())), '0'+argument+'b').replace(' ', '')
                else:
                    compiled_line += " " + format(int(command[i+1]), '0'+argument+'b').replace(' ', '')
                i += 1

            while len(compiled_line.replace(' ', '')) < 16:
                compiled_line += '0'
            output.write(compiled_line + '\n')
            line_num += 1
            


if __name__ == "__main__":
    main()