import re

with open('index.html', 'r') as f:
    text = f.read()

def safe_replace(old, new):
    global text
    if old in text:
        text = text.replace(old, new)
        print("Replaced:", old.strip())
    else:
        print("NOT FOUND:", old.strip())

safe_replace('margin-bottom: 5px !important;', 'margin-bottom: 2px !important;')
safe_replace('margin-top: 3px !important;\n        padding-top: 3px !important;', 'margin-top: 2px !important;\n        padding-top: 3px !important;')

with open('index.html', 'w') as f:
    f.write(text)
