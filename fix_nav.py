with open('index.html', 'r') as f:
    text = f.read()

# Replace bottom-nav background
old_bottom_nav_bg = """    .bottom-nav { 
      background: rgba(255, 255, 255, 0.85); 
      backdrop-filter: blur(20px); 
      -webkit-backdrop-filter: blur(20px);
      border-radius: 2rem; 
      border: 1px solid rgba(0,0,0,0.08);"""

new_bottom_nav_bg = """    .bottom-nav { 
      background: rgba(0, 0, 0, 0.4); 
      backdrop-filter: blur(24px); 
      -webkit-backdrop-filter: blur(24px);
      border-radius: 2rem; 
      border: 1px solid rgba(255,255,255,0.1);"""

text = text.replace(old_bottom_nav_bg, new_bottom_nav_bg)

# Replace nav-item default color
old_nav_item_color = """      color: rgba(0,0,0,0.6); 
      white-space: nowrap;"""

new_nav_item_color = """      color: rgba(255,255,255,0.65); 
      white-space: nowrap;"""

text = text.replace(old_nav_item_color, new_nav_item_color)

# Replace active color and add transparent blur background
old_active = """    .nav-item.active { color: #000; }
    .nav-item.active i { color: #000; }"""

new_active = """    .nav-item.active { 
      color: #ffffff; 
      background: rgba(255, 255, 255, 0.15); 
      backdrop-filter: blur(10px); 
      -webkit-backdrop-filter: blur(10px);
    }
    .nav-item.active i { color: #ffffff; }"""

text = text.replace(old_active, new_active)

with open('index.html', 'w') as f:
    f.write(text)
