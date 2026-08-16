import re

with open('index.html', 'r') as f:
    text = f.read()

# 1. Reduce dark background slightly
old_bg = "background: rgba(0, 0, 0, 0.45);"
new_bg = "background: rgba(0, 0, 0, 0.3);"
text = text.replace(old_bg, new_bg)

# 2. Make font (text) always white, but keep icons dimmed in inactive state
old_nav_color = """      color: rgba(255, 255, 255, 0.6); 
      text-shadow: none;"""
new_nav_color = """      color: #ffffff; 
      text-shadow: 0 1px 2px rgba(0,0,0,0.4);"""
text = text.replace(old_nav_color, new_nav_color)

old_icon = """    .nav-item i { font-size: 1.25rem; transition: transform 0.2s; text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5); }"""
new_icon = """    .nav-item i { font-size: 1.25rem; transition: color 0.2s, transform 0.2s; color: rgba(255, 255, 255, 0.45); text-shadow: none; }"""
text = text.replace(old_icon, new_icon)

with open('index.html', 'w') as f:
    f.write(text)
