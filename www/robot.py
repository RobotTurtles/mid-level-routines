import sys
sys.path.append('/home/pi/robotturtles/mid-level-routines')
import cgi
import cgitb; cgitb.enable()  # for troubleshooting
from Utilities.ManageCommandsFromFile import ReadCommandFromFile


mFile = ReadCommandFromFile("robotCommand.txt")

print "Content-type: text/html"
print

print """
<html>
<head><title>Turtle Response</title></head>
<body>
Turtle Saw: 
"""
form = cgi.FieldStorage()

r_cmd = form.getvalue("r_cmd", "{no message}")
r_arg = form.getvalue("r_arg", "{no arg}")

if(r_cmd != "{no message}"):
    mFile.write_command(r_cmd)

print """
   <p>Previous message: %s, args: %s</p>

   <p>SendCommand:
  <form method="post" action="robot.py">    
	<p>message: <input type="text" name="r_cmd"/></p>
	<p>argument: <input type="text" name="r_arg"/></p>
	<input type="submit" name="Update">
  </form>

</body>

</html>
""" % (cgi.escape(r_cmd), cgi.escape(r_arg))


