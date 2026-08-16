with open('index.html', 'r') as f:
    text = f.read()

text = text.replace('margin: 0 auto 10px auto;', 'margin: 0 auto 2px auto;')
text = text.replace('padding: 0 6px !important;\n        border: none !important;', 'padding: 0 6px !important;\n        border: none !important;\n        margin-bottom: 2px !important;')

with open('index.html', 'w') as f:
    f.write(text)
print("Padding fixed!")
