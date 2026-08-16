import re

with open('index.html', 'r') as f:
    text = f.read()

old_css = """    .bottom-nav { 
      background: transparent; 
      backdrop-filter: blur(12px); 
      -webkit-backdrop-filter: blur(12px);
      border-radius: 2rem; 
      border: 1px solid rgba(255, 255, 255, 0.15);
      box-shadow: 0 8px 32px rgba(0,0,0,0.1);"""

new_css = """    .bottom-nav { 
      background: rgba(23, 27, 38, 0.85); 
      backdrop-filter: blur(20px); 
      -webkit-backdrop-filter: blur(20px);
      border-radius: 2rem; 
      border: 1px solid rgba(255, 255, 255, 0.10);
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);"""

text = text.replace(old_css, new_css)

with open('index.html', 'w') as f:
    f.write(text)
