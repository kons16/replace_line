from argparse import ArgumentParser


def get_option():
    argparser = ArgumentParser()
    argparser.add_argument('-i', '--input', type=str,
                           help='Input file name')
    argparser.add_argument('-o', '--output', type=str,
                           help='Output file name')
    argparser.add_argument('-l', '--line', type=str,
                           help='The line you want to replace')
    argparser.add_argument('-r', '--replace', type=str,
                           help='replace string')
    return argparser.parse_args()


def replace_func(input_file_name, output_file_name, replace_line, replace_str):
    """ 行を指定された文字に書き換える """
    f = open(input_file_name, "r")
    fw = open(output_file_name, "w")

    lines = f.readlines()
    for line in lines:
        line = line.rstrip()

        if replace_line == "blank":
            if line != "":
                fw.write(line + "\n")
        else:
            if line == replace_line:
                fw.write(replace_str + "\n")
            else:
                fw.write(line + "\n")

    f.close()
    fw.close()


if __name__ == '__main__':
    args = get_option()

    input_file_name = args.input
    output_file_name = args.output
    replace_line = args.line
    replace = args.replace

    replace_func(input_file_name, output_file_name, replace_line, replace)
