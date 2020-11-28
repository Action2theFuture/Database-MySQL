#!python
print("content-type: text/html\n")
print()
import cgi, os, view, html_sanitizer
sanitizer = html_sanitizer.Sanitizer()
'''
files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
'''
#print(listStr) <<< 이거 이상해
form = cgi.FieldStorage()
if 'id' in form:
    tilte = pageId = form.getvalue("id")
    description = open('data/'+pageId, 'r').read()
    #security - replace
    # description = description.replace('<', '%lt;')
    # description = description.replace('>', '%gt;')

    #security - html_sanitizer(using)
    tilte = sanitizer.sanitize(tilte)
    description = sanitizer.sanitize(description)
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action ="process_delete.py" method="post">
            <input type="hidden" name="pageId" value="{}">
            <input type="submit" value="delete">
        </form>
    '''.format(pageId)
else:
    tilte = pageId = 'Welcome'
    description = 'Hello, web'
    update_link = ''
    delete_action = ''
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
    {update_link}
    {delete_action}
    <h2>{title}</h2>
    <p>{desc}</p>
</body>
</html>
'''.format(
title=tilte,
desc=description,
listStr=view.getList(),
update_link=update_link,
delete_action=delete_action)
)
