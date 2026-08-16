with open('index.html', 'r') as f:
    text = f.read()

old_active = """    .nav-item.active { 
      color: #ffffff; 
      background: rgba(0, 0, 0, 0.2); 
      box-shadow: none;
    }"""
new_active = """    .nav-item.active { 
      color: #ffffff; 
      background: rgba(255, 255, 255, 0.15); 
      box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.1);
    }"""

text = text.replace(old_active, new_active)

# Ensure text color on inactive tabs is slightly dimmer to create contrast for the active tab
old_inactive = """      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1); 
      color: #ffffff; 
      text-shadow: 0 1px 2px rgba(0, 0, 0, 0.5);"""
new_inactive = """      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1); 
      color: rgba(255, 255, 255, 0.6); 
      text-shadow: none;"""

text = text.replace(old_inactive, new_inactive)

with open('index.html', 'w') as f:
    f.write(text)
