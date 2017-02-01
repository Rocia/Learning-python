f =open(r"C:\Users\scaela\Desktop\a.txt","w")
    f.write("abcdefghijklmnopqrstuvwxyz\n");
    f.seek(10,0)
    f.write("Whats Up?")
    f.close()
