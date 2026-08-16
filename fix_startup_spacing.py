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

# Desktop post-head
safe_replace('      :is(#startup-community-feed, .startup-feed-wrapper) .post-head {\n        margin-bottom: 18px;\n      }', '      :is(#startup-community-feed, .startup-feed-wrapper) .post-head {\n        margin-bottom: 6px;\n      }')

# Desktop post-title
safe_replace('margin: 18px 0 10px;', 'margin: 6px 0 4px;')

# Desktop post-copy
safe_replace('font-size: 14.5px; color: #9ca3af; line-height: 1.65; margin-bottom: 8px;', 'font-size: 14.5px; color: #9ca3af; line-height: 1.65; margin-bottom: 4px;')

# Desktop source-row
safe_replace('padding-top: 4px; margin-top: 8px;', 'padding-top: 4px; margin-top: 4px;')

# Mobile post-title
safe_replace('margin: 10px 0 6px;', 'margin: 4px 0 4px;')

# Mobile post-copy
safe_replace('margin: 0 0 6px;', 'margin: 0 0 4px;')

# Mobile source-row margin-top
safe_replace('padding-top: 4px; margin-top: 3px;', 'padding-top: 4px; margin-top: 2px;')

with open('index.html', 'w') as f:
    f.write(text)
