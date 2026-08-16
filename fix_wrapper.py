import re
with open('index.html', 'r') as f:
    text = f.read()

target = "container.innerHTML = filtered.map(p => postMarkup(p, p.id)).join('');"
replacement = "container.innerHTML = '<div class=\"startup-feed-wrapper\">' + filtered.map(p => postMarkup(p, p.id)).join('') + '</div>';"

text = text.replace(target, replacement)

with open('index.html', 'w') as f:
    f.write(text)
