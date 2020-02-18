import random
import string



def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

    
def fillWithText():
    f = open("test.txt", "a")
    for i in range(100):
        f.write(randomString(100))
        f.write("\n")
    f.close()


def insertOnFirstLine(spanLine1, file1Name):
    file1 = open(file1Name, "r")
    oline = file1.readlines()
    oline.insert(0, spanLine1)
    file1.close()
    file1 = open(file1Name, "w")
    file1.writelines(oline)
    file1.close()

        
fillWithText()
spanLine1 = "<span class=\"remove-page-title\"></span>"
file1Name = "test.txt"
insertOnFirstLine(spanLine1, file1Name)
# f = open("test.txt", "r")
# spanLine1 = "<span class=\"remove-page-title\"></span>"
# oline = f.readlines()
# oline.insert(0, spanLine1)
# f.close()
# f = open("test.txt", "w")
# f.writelines(oline)
# f.close()
# print(f.read())
