""" replace_line function """


def replace_line(input_file_name, output_file_name, replace_line, replace_str):
    """ 行を指定された文字に書き換える """
    f = open(input_file_name, "r")
    fw = open(output_file_name, "w")

    lines = f.readlines()
    for line in lines:
        line = line.rstrip()

        if replace_line == "blank":
            if line != "":
                fw.write(line + "\n")
            elif line == "" and replace_str is not None:
                fw.write(replace_str + "\n")
        else:
            if line == replace_line:
                fw.write(replace_str + "\n")
            else:
                fw.write(line + "\n")

    f.close()
    fw.close()
