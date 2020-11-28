#!python
print("content-type: text/html\n")
print()
import cgi, os, view
#refactoring

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
    <form action="process_update.py" method="post">
    <!--기본 method는 get-->
        <input type="hidden" name="pageId" value="{form_default_title}">
        <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
        <p><textarea rows="4" name="description" placeholder="description">{form_default_description}</textarea></P>
        <p><input type="submit"></p>
    </form>
</body>
</html>
'''.format(title=pageId, desc=description, listStr=view.getList(), form_default_title=pageId, form_default_description=description))
