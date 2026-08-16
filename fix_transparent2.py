import re

with open('index.html', 'r') as f:
    text = f.read()

# Make background pure transparent
old_bg = """    .bottom-nav { 
      background: rgba(0, 0, 0, 0.1);"""
new_bg = """    .bottom-nav { 
      background: transparent;"""
text = text.replace(old_bg, new_bg)

old_border = "border: 1px solid rgba(0, 0, 0, 0.1);"
new_border = "border: 1px solid rgba(255, 255, 255, 0.15);"
text = text.replace(old_border, new_border)

with open('index.html', 'w') as f:
    f.write(text)
