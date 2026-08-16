import re

with open('index.html', 'r') as f:
    text = f.read()

def safe_replace(old, new):
    global text
    if old in text:
        text = text.replace(old, new)
        print("Replaced:", old.strip())
    else:
        print("NOT FOUND:", old.strip())

# Mobile post-head
old_head = """    :is(#startup-community-feed, .startup-feed-wrapper) .post-head {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 4px;
    }"""
new_head = """    :is(#startup-community-feed, .startup-feed-wrapper) .post-head {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 2px;
    }"""

safe_replace(old_head, new_head)

with open('index.html', 'w') as f:
    f.write(text)
