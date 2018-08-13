import os,re,io

commentLines = 0
whiteLines = 0
comment = False
count = 0

path = 'D:\source\swoole'


def tree(path):
    filelist = os.listdir(path)
    for file in filelist:
        if os.path.isdir(os.path.join(path,file)):
            tree(os.path.join(path,file))
        else:
            filename = os.path.basename(os.path.join(path,file))
            if filename.endswith(".py"):
                file = io.open(os.path.join(path,file))
                parse(file)
                file.close()

def parse(file):
    global commentLines
    global whiteLines
    global comment
    global count
    for line in file.readlines():
        count += 1
        if line.startswith("#"):
            commentLines += 1
        elif re.match("^[\\s&&[^\\n]]*$",line):
            whiteLines += 1

print("我们")
exit
tree(path)
print('总行数',count)
print('注释',commentLines)
print('空行',whiteLines)