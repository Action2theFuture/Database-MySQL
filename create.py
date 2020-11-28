#!python
print("content-type: text/html\n")
print()
import cgi, os, view
#refactoring
'''
def getList():
    files = os.listdir('data')
    listStr = ''
    for item in files:
        listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr
'''
'''
files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
'''
    #print(listStr) <<< 이거 이상해
form = cgi.FieldStorage()
if 'id' in form:
    pageId = form.getvalue("id")
    description = open('data/'+pageId, 'r').read()
else:
    pageId = 'Welcome'
    description = 'Hello, web'
print('''<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<title>WEB1 - Welcome</title>
</head>
<body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>{listStr}</ol>
    <a href="create.py">create</a>
    <form action="process_create.py" method="post">
    <!--기본 method는 get-->
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea rows="4" name="description" placeholder="description"></textarea></P>
        <p><input type="submit"></p>
    </form>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=view.getList()))
