import re
with open('index.html', 'r') as f:
    text = f.read()

text = text.replace('#startup-community-feed, .startup-feed-wrapper', ':is(#startup-community-feed, .startup-feed-wrapper)')

with open('index.html', 'w') as f:
    f.write(text)
