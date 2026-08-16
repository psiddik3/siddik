import re

with open('index.html', 'r') as f:
    text = f.read()

# updateUserAvatars
text = text.replace("name.charAt(0).toLowerCase()", "name.substring(0, 2).toLowerCase()")

# recruiterName
text = text.replace("(recruiterName || '?').charAt(0).toLowerCase()", "(recruiterName || '?').substring(0, 2).toLowerCase()")

# post.authorName
text = text.replace("(post.authorName || '?').charAt(0).toLowerCase()", "(post.authorName || '?').substring(0, 2).toLowerCase()")

with open('index.html', 'w') as f:
    f.write(text)
