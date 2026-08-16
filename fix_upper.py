with open('index.html', 'r') as f:
    text = f.read()

# 1. updateUserAvatars
text = text.replace("name.charAt(0).toUpperCase()", "name.charAt(0).toLowerCase()")

# 2. username generation
text = text.replace("username.charAt(0).toUpperCase() + username.slice(1)", "username.toLowerCase()")

# 3. recruiterName toUpperCase
text = text.replace("${(recruiterName || '?').charAt(0).toUpperCase()}", "${(recruiterName || '?').charAt(0).toLowerCase()}")

with open('index.html', 'w') as f:
    f.write(text)
