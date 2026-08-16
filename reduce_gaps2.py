with open('index.html', 'r') as f:
    text = f.read()

text = text.replace('margin-bottom: 6px;', 'margin-bottom: 2px;')
text = text.replace('margin-bottom: 4px;', 'margin-bottom: 2px;')

with open('index.html', 'w') as f:
    f.write(text)
print("Done!")
