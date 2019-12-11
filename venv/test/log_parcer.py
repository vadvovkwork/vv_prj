import os
import re

def get_log():

    #create dir
    if not os.path.isdir("log"):
        os.mkdir("log")

    #create file
    path_to_file = "C:\\PycharmProjects\\vv_prj\\venv\\test\\log\\"
    f = open (path_to_file + "vv.txt", "w")

    #add vv text
    #f.write("vv TEST\n")
    #f.write("Error\n")

    #copy data to vv.txt from log
    path_to_log = "C:\\vv_log\\"
    f = open(path_to_file + "vv.txt", "a+")
    f2 = open(path_to_log + "log.log", "r+")
    # copy data from vv.txt list container
    line_list = []
    for line in f2:
        f.write(line)
        line_list.append(line)
    print(line_list)

    print(len(line_list))


    #get Fail, Error, Exception
    f = open(path_to_file + "vv.txt", "r+")
    f_res = open(path_to_file + "vv_res.txt", "w+")
    i = 0
    for line in f:

        issue = re.findall(r"Error | Fail | Exception", line)

        if issue:
            f_res.write(line_list[i-1])
            f_res.write(line)
            f_res.write(line_list[i+1])
            f_res.write("------------------------\n")

        i=i+1
get_log()