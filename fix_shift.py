import re

with open('index.html', 'r') as f:
    text = f.read()

old_css = """    .bottom-nav-fixed { 
      position: fixed; 
      bottom: 0; 
      left: 0; 
      right: 0; 
      display: flex; 
      justify-content: center; 
      z-index: 1000; 
      background: transparent; 
      pointer-events: none; 
      padding-bottom: max(0.8rem, env(safe-area-inset-bottom)); 
    }"""

new_css = """    .bottom-nav-fixed { 
      position: fixed; 
      bottom: 0; 
      left: 0; 
      width: 100vw; 
      display: flex; 
      justify-content: center; 
      z-index: 1000; 
      background: transparent; 
      pointer-events: none; 
      padding-bottom: max(0.8rem, env(safe-area-inset-bottom)); 
    }"""

if old_css in text:
    text = text.replace(old_css, new_css)
    print("Replaced .bottom-nav-fixed")
else:
    print("Not found")

with open('index.html', 'w') as f:
    f.write(text)
