from r2w import *

output = r2w_header() + """
<form enctype="multipart/form-data" action="?" method="POST">
<input type=file name=upfile />
<br />
"""

output += f"File contents: {content}" if content != "" else "No file uploaded."
output +="""
<input type=submit value=Upload />
</form>
""" + r2w_footer()
