    import os, subprocess
    src = "/path/to/your/source/directory"
    dst = "/path/to/your/destination/directory/"
    listOfFiles = os.listdir(src)
    for f in listOfFiles:
           fullPath = src + "/" + f
           subprocess.Popen("mv" + " " + fullPath + " " + dst,shell=True)
