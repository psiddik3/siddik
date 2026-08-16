import re

with open('index.html', 'r') as f:
    text = f.read()

old_bottom_nav = """    .bottom-nav { 
      background: rgba(0, 0, 0, 0.3); 
      backdrop-filter: blur(20px); 
      -webkit-backdrop-filter: blur(20px);
      border-radius: 2rem; 
      border: 1px solid rgba(255, 255, 255, 0.10);
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25); 
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
new_bottom_nav = """    .bottom-nav { 
      background: rgba(18, 22, 33, 0.65); 
      backdrop-filter: blur(28px) saturate(120%); 
      -webkit-backdrop-filter: blur(28px) saturate(120%);
      border-radius: 40px; 
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-top: 1px solid rgba(255, 255, 255, 0.25);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.05); 
      display: flex; 
      flex-wrap: nowrap; 
      justify-content: space-between; 
      gap: 0.25rem; 
      padding: 0.35rem 0.4rem; 
      pointer-events: auto; 
      width: 100%; 
      max-width: 500px; 
      margin-bottom: 0; 
      overflow-x: auto;
      scrollbar-width: none;
      transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.3s ease;
    }"""
text = text.replace(old_bottom_nav, new_bottom_nav)

old_nav_item = """    .nav-item { 
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
      color: #ffffff; 
      text-shadow: 0 1px 2px rgba(0,0,0,0.4);
      white-space: nowrap; 
      cursor: pointer; 
      background: transparent; 
      border: none;
      gap: 0.2rem;
      min-width: 0;
    }"""
new_nav_item = """    .nav-item { 
      flex: 1 1 0px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      font-size: 0.65rem; 
      font-weight: 700; 
      padding: 0.45rem 0.1rem; 
      border-radius: 30px; 
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1); 
      color: #ffffff; 
      text-shadow: 0 1px 2px rgba(0,0,0,0.4);
      white-space: nowrap; 
      cursor: pointer; 
      background: transparent; 
      border: none;
      gap: 0.25rem;
      min-width: 0;
    }"""
text = text.replace(old_nav_item, new_nav_item)

old_nav_active = """    .nav-item.active { 
      color: #ffffff; 
      background: rgba(255, 255, 255, 0.15); 
      box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.1);
    }"""
new_nav_active = """    .nav-item.active { 
      color: #ffffff; 
      background: rgba(255, 255, 255, 0.12); 
      box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.15), 0 2px 8px rgba(0, 0, 0, 0.15);
    }"""
text = text.replace(old_nav_active, new_nav_active)

old_nav_icon = """    .nav-item i { font-size: 1.25rem; transition: color 0.2s, transform 0.2s; color: rgba(255, 255, 255, 0.45); text-shadow: none; }"""
new_nav_icon = """    .nav-item i { font-size: 1.35rem; transition: color 0.2s, transform 0.2s; color: rgba(255, 255, 255, 0.55); text-shadow: 0 1px 2px rgba(0,0,0,0.3); }"""
text = text.replace(old_nav_icon, new_nav_icon)

with open('index.html', 'w') as f:
    f.write(text)
