import re

with open('index.html', 'r') as f:
    text = f.read()

# Add a slight text-shadow to .nav-item
old_nav_item = """      color: #ffffff; 
      white-space: nowrap; 
      cursor: pointer;"""
new_nav_item = """      color: #ffffff; 
      text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);
      white-space: nowrap; 
      cursor: pointer;"""
text = text.replace(old_nav_item, new_nav_item)

# Ensure icons also have a text-shadow so they don't vanish
old_icon = """    .nav-item i { font-size: 1.25rem; transition: transform 0.2s; }"""
new_icon = """    .nav-item i { font-size: 1.25rem; transition: transform 0.2s; text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5); }"""
text = text.replace(old_icon, new_icon)

with open('index.html', 'w') as f:
    f.write(text)
