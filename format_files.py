'''
    Make sure all the files you want to format are in this directory,
    and that you also have a folder labelled "data" in this directory

    You may need to adjust the file names because some are labelled, "NEW"
'''

import os

currentPath = os.getcwd()

l1 = ["1", "2"]
l2 = ["A", "B", "C", "D"]

for num in l1:
    for letter in l2:
        try:
            fin = open(f"L2PRT{num}{letter}_NEW.txt", "r")
            fout = open(f"L2PRT{num}{letter}_NEW_format.txt", "w")
        except:
            continue

        for line in fin:
            if "Ambient" in line:   
                continue
            elif line[0] == "\n":
                continue
            else:
                line = line.replace("Deg C", "DegC")
                fout.write(','.join(line.split(sep="	")))

        fin.close()
        fout.close()
        try:
            os.rename(os.path.join(currentPath, f"L2PRT{num}{letter}_NEW_format.txt"), os.path.join(currentPath, f"data\\L2PRT{num}{letter}_NEW_format.csv"))
        except Exception as e:
            print(e)


