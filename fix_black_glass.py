import re

with open('index.html', 'r') as f:
    text = f.read()

old_css = """    .bottom-nav { 
      background: rgba(23, 27, 38, 0.1); 
      backdrop-filter: blur(10px); 
      -webkit-backdrop-filter: blur(10px);"""

new_css = """    .bottom-nav { 
      background: rgba(0, 0, 0, 0.45); 
      backdrop-filter: blur(20px); 
      -webkit-backdrop-filter: blur(20px);"""

if old_css in text:
    text = text.replace(old_css, new_css)
    print("Replaced successfully!")
else:
    print("Could not find exact match.")

with open('index.html', 'w') as f:
    f.write(text)
