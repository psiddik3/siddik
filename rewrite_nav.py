import re

with open('index.html', 'r') as f:
    text = f.read()

# 1. Update .bottom-nav
old_bottom_nav = """    .bottom-nav { 
      background: rgba(0, 0, 0, 0.4); 
      backdrop-filter: blur(24px); 
      -webkit-backdrop-filter: blur(24px);
      border-radius: 2rem; 
      border: 1px solid rgba(255,255,255,0.1);
      box-shadow: 0 8px 32px rgba(0,0,0,0.3); 
      display: flex; 
      flex-wrap: nowrap; 
      justify-content: center; 
      gap: 1.25rem; 
      padding: 0.35rem 1rem; 
      pointer-events: auto; 
      width: 800px; 
      max-width: 94%; 
      margin-bottom: 0; 
      overflow-x: auto;
      scrollbar-width: none;
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s ease;
    }"""

new_bottom_nav = """    .bottom-nav { 
      background: rgba(255, 255, 255, 0.75); 
      backdrop-filter: blur(30px) saturate(150%); 
      -webkit-backdrop-filter: blur(30px) saturate(150%);
      border-radius: 2rem; 
      border: 1px solid rgba(255, 255, 255, 0.6);
      box-shadow: 0 8px 32px rgba(0,0,0,0.08), inset 0 1px 1px rgba(255, 255, 255, 0.9); 
      display: flex; 
      flex-wrap: nowrap; 
      justify-content: space-between; 
      gap: 0.25rem; 
      padding: 0.35rem 0.5rem; 
      pointer-events: auto; 
      width: 100%; 
      max-width: 500px; 
      margin-bottom: 0; 
      overflow-x: auto;
      scrollbar-width: none;
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s ease;
    }"""
text = text.replace(old_bottom_nav, new_bottom_nav)

# 2. Update .nav-item
old_nav_item = """    .nav-item { 
      flex: 1 1 auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      font-size: 0.75rem; 
      font-weight: 600; 
      padding: 0.3rem 0.4rem; 
      border-radius: 1.5rem; 
      transition: all 0.2s; 
      color: rgba(255,255,255,0.65); 
      white-space: nowrap; 
      cursor: pointer; 
      background: none; 
      border: none;
      gap: 0.15rem;
    }"""
new_nav_item = """    .nav-item { 
      flex: 1 1 0px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      font-size: 0.7rem; 
      font-weight: 700; 
      padding: 0.4rem 0.1rem; 
      border-radius: 1.25rem; 
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1); 
      color: rgba(0, 0, 0, 0.5); 
      white-space: nowrap; 
      cursor: pointer; 
      background: transparent; 
      border: none;
      gap: 0.2rem;
      min-width: 0;
    }"""
text = text.replace(old_nav_item, new_nav_item)

# 3. Update .nav-item.active
old_active = """    .nav-item.active { 
      color: #ffffff; 
      background: rgba(255, 255, 255, 0.15); 
      backdrop-filter: blur(10px); 
      -webkit-backdrop-filter: blur(10px);
    }
    .nav-item.active i { color: #ffffff; }"""

new_active = """    .nav-item.active { 
      color: #000000; 
      background: rgba(255, 255, 255, 0.95); 
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08), inset 0 1px 1px #ffffff;
    }
    .nav-item.active i { color: #000000; }"""
text = text.replace(old_active, new_active)

# 4. Update mobile media query spacing
old_mobile_nav = "      .bottom-nav { padding: 0.24rem 1.6rem; width: max-content; max-width: 98%; gap: 1.3rem; }"
new_mobile_nav = "      .bottom-nav { padding: 0.35rem 0.5rem; width: 100%; max-width: 96%; gap: 0.2rem; margin: 0 auto; }"
text = text.replace(old_mobile_nav, new_mobile_nav)

old_mobile_item = "      .nav-item { font-size: 0.68rem; padding: 0.18rem 0.2rem; }"
new_mobile_item = "      .nav-item { font-size: 0.65rem; padding: 0.35rem 0; }"
text = text.replace(old_mobile_item, new_mobile_item)


with open('index.html', 'w') as f:
    f.write(text)
