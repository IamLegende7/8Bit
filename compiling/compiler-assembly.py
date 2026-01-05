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
    else:
        print(f'File "{source_path}" not found!')
        quit()

    ## Compiling source code
    compiled_lines = []
    output_path = str(Path(source_path).stem) + ".pal"

    line_num = 1
    for command in source_code:
        if command[0] == "SET":
            address_line = int(command[1])
            compiled_value = format(int(command[2]), '016b').replace(' ', '')

            print(f'[L\033[1mx\033[0m] \033[1;32mSET\033[0m')
            print(f'   ┣━ Module is: \033[1;35mxx\033[0m')
            print(f'   ┗━ Wrote at {address_line}: \033[1;33m{compiled_value}\033[0m')

            if len(compiled_lines)-1 < address_line-1:
                for i in range((address_line-1)-(len(compiled_lines)-1)):
                    compiled_lines.append("00 0000 00000 00000")
                compiled_lines.append(compiled_value)
            elif len(compiled_lines)-1 == address_line-1:
                compiled_lines.append(compiled_value)
            elif len(compiled_lines)-1 > address_line-1:
                compiled_lines[address_line] = compiled_value

        else:


            # Command as String
            command_str = command[0]
            for piece in command[1:]:
                command_str += ' ' + piece
            print(f'[L\033[1m{line_num}\033[0m] \033[1;32m{command_str}\033[0m')

            # Get module & command
            module = commands[command[0]]["module"].replace(' ', '') + " "
            cmd = commands[command[0]]["cmd"].replace(' ', '')
            print(f'   ┣━ Module is: \033[1;35m{module}\033[0m')
            print(f'   ┣━ CMD is: \033[1;35m{cmd}\033[0m')

            # Add to compiled line
            compiled_line = ''
            compiled_line += module
            compiled_line += cmd

            # Arguments
            args_expected = commands[command[0]]["args"]
            if len(args_expected) > 0:
                print(f'   ┣━ Arguments: ')

                for i in range(len(args_expected)):
                    if '[' in command[i+1]:
                        argument_value = line_num + int(command[i+1].replace(' ', '').replace('[', '').replace(']', '').strip())
                        extra_steps = f' -> {argument_value}'
                    else:
                        argument_value = int(command[i+1])
                        extra_steps = ''
                    argument_value_formatted = format(argument_value, '0'+args_expected[i]+'b').replace(' ', '')
                    compiled_line += " " + argument_value_formatted
                    # Visual feedback
                    print(f'   ┃  ┗━ {command[i+1]}{extra_steps} -> \033[1;35m{argument_value_formatted}\033[0m')


            # Fill up with zeros
            while len(compiled_line.replace(' ', '')) < 16:
                compiled_line += '0'
            
            # Write
            print(f'   ┗━ Result: \033[1;33m{compiled_line}\033[0m')

            if len(compiled_lines)-1 < line_num-1:
                for i in range((line_num-1)-(len(compiled_lines)-1)):
                    compiled_lines.append("00 0000 00000 00000")
                compiled_lines.append(compiled_line)
            elif len(compiled_lines)-1 == line_num-1:
                compiled_lines.append(compiled_line)
            elif len(compiled_lines)-1 > line_num-1:
                compiled_lines[line_num] = compiled_line

            line_num += 1

    # Write to file
    with open(output_path, 'w') as output:
        for x in compiled_lines:
            output.write(x+'\n')

if __name__ == "__main__":
    main()