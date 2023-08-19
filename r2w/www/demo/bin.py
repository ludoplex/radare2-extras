from r2.r_bin import *

try:
	b=RBin ()
	b.load ("/bin/ls", None)
	baddr = b.get_baddr ()
	code = "".join(
		"offset=0x%08x va=0x%08x name=%s</br>" % (i.offset, baddr + i.rva, i.name)
		for i in b.get_imports()
	)
except:
	code = ""

output = """
<html>
<tt>
<h2><a href="/">r2w</a> : RBin demo</h2>

%s
"""%(code)
