import glob, os

#*****Define the directory******

os.chdir("D:/Files")#***Change the directory as requered

#*****Loop to get the txt files and display the name

for file in glob.glob("*.txt"):
    print(file)
