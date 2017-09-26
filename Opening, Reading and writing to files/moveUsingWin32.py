import os
import win32file
import tempfile

filename1 = tempfile.mktemp (".txt")
open (filename1, "w").close ()
filename2 = filename1 + ".copy"
print filename1, "=>", filename2

#
# Do a straight copy first, then try to copy without
# failing on collision, then try to copy and fail on
# collision. The first two should succeed; the third
# should fail.
#
win32file.CopyFile (filename1, filename2, 1)
win32file.CopyFile (filename1, filename2, 0)
win32file.CopyFile (filename1, filename2, 1)

if os.path.isfile (filename2): print "Success"

dirname1 = tempfile.mktemp (".dir")
os.mkdir (dirname1)
dirname2 = dirname1 + ".copy"
print dirname1, "=>", dirname2

#
# The CopyFile functionality doesn't seem to cope
# with directories.
#
win32file.CopyFile (dirname1, dirname2, 1)

if os.path.isdir (dirname2): print "Success"
