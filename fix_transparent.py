import re

with open('index.html', 'r') as f:
    text = f.read()

# 1. Update .bottom-nav
old_bottom_nav = """    .bottom-nav { 
      background: rgba(255, 255, 255, 0.75); 
      backdrop-filter: blur(30px) saturate(150%); 
      -webkit-backdrop-filter: blur(30px) saturate(150%);
      border-radius: 2rem; 
      border: 1px solid rgba(255, 255, 255, 0.6);
      box-shadow: 0 8px 32px rgba(0,0,0,0.08), inset 0 1px 1px rgba(255, 255, 255, 0.9);"""

new_bottom_nav = """    .bottom-nav { 
      background: rgba(0, 0, 0, 0.1); 
      backdrop-filter: blur(12px); 
      -webkit-backdrop-filter: blur(12px);
      border-radius: 2rem; 
      border: 1px solid rgba(0, 0, 0, 0.1);
      box-shadow: 0 8px 32px rgba(0,0,0,0.1);"""
text = text.replace(old_bottom_nav, new_bottom_nav)

# 2. Update .nav-item color
old_nav_item_color = "      color: rgba(0, 0, 0, 0.5);"
new_nav_item_color = "      color: #ffffff;"
text = text.replace(old_nav_item_color, new_nav_item_color)

# 3. Update .nav-item.active
old_active = """    .nav-item.active { 
      color: #000000; 
      background: rgba(255, 255, 255, 0.95); 
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08), inset 0 1px 1px #ffffff;
    }
    .nav-item.active i { color: #000000; }"""

new_active = """    .nav-item.active { 
      color: #ffffff; 
      background: rgba(0, 0, 0, 0.2); 
      box-shadow: none;
    }
    .nav-item.active i { color: #ffffff; }"""
text = text.replace(old_active, new_active)

with open('index.html', 'w') as f:
    f.write(text)
