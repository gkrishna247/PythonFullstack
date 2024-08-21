def write(*store):
    f=open("21082024/ksr.txt",'a')
    for input in store:
        f.write(input)
        f.write("\n")
    f.close()
