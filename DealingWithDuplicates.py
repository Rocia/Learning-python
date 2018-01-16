import os,sys,shutil
### copies a list of files from source. handles duplicates.
def rename(file_name, dst, num=1):
    #splits file name to add number distinction
    (file_prefix, exstension) = os.path.splitext(file_name)
    renamed = "%s(%d)%s" % (file_prefix,num,exstension)

    #checks if renamed file exists. Renames file if it does exist.
    if os.path.exists(dst + renamed):
        return rename(file_name, dst, num + 1)
    else:
        return renamed

def copy_files(src,dst,file_list):
    for files in file_list:
        src_file_path = src + files
        dst_file_path = dst + files
        if os.path.exists(dst_file_path):
            new_file_name =  rename(files, dst)
            dst_file_path = dst + new_file_name

        print "Copying: " + dst_file_path
        try:
            shutil.copyfile(src_file_path,dst_file_path)
        except IOError:
            print src_file_path + " does not exist"
            raw_input("Please, press enter to continue.")

def read_file(file_name):
    f = open(file_name)
    #reads each line of file (f), strips out extra whitespace and 
    #returns list with each line of the file being an element of the list
    content = [x.strip() for x in f.readlines()]
    f.close()
    return content
