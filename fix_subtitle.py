with open('index.html', 'r') as f:
    text = f.read()

text = text.replace("let subtitle = post.authorTitle || 'Community Member';", "let subtitle = post.authorTitle || 'Community User';")

with open('index.html', 'w') as f:
    f.write(text)
