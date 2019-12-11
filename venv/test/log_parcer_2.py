import os
import shutil
import re

src = "C:\\vv_log\\log.log"
new_dir = "log2"
dst = "C:\\PycharmProjects\\vv_prj\\venv\\test\\log2\\"
print(src)
print(dst)

def get_file ():
    if not os.path.isdir(new_dir):
        os.mkdir(shutil.copy)
    shutil.copy(src, "log2")
get_file ()


def parce_file ():

    f = open(dst + "log.log", "r")
    f2 = open(dst + "issues.txt", "w+")

    for line in f:
        #issue = re.findall(r"[\s+]wifi[\s+]", line)
        issue = re.findall('.', line)

        if issue:

            f2.write(line)
            #f2.write("------------------------\n")

            print(line)




parce_file ()

