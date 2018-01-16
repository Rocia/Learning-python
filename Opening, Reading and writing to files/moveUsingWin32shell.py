import os
from win32com.shell import shell, shellcon
import tempfile

filename1 = tempfile.mktemp (".txt")
open (filename1, "w").close ()
filename2 = filename1 + ".copy"
print filename1, "=>", filename2

#
# Do a straight copy first, then try to copy with
# rename-on-collision, then without. The first two
# should succeed (the second with a confirmation dialog);
# the third should fail.
#
shell.SHFileOperation (
  (0, shellcon.FO_COPY, filename1, filename2, 0, None, None)
)
shell.SHFileOperation (
  (0, shellcon.FO_COPY, filename1, filename2, shellcon.FOF_RENAMEONCOLLISION, None, None)
)
shell.SHFileOperation (
  (0, shellcon.FO_COPY, filename1, filename2, 0, None, None)
)

if os.path.isfile (filename2): print "Success"

dirname1 = tempfile.mktemp (".dir")
os.mkdir (dirname1)
dirname2 = dirname1 + ".copy"
print dirname1, "=>", dirname2

#
# The CopyFile functionality doesn't seem to cope
# with directories.
#
shell.SHFileOperation (
  (0, shellcon.FO_COPY, dirname1, dirname2, 0, None, None)
)

if os.path.isdir (dirname2): print "Success"

