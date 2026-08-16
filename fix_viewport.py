import re

with open('index.html', 'r') as f:
    text = f.read()

# Replace 100vh with 100dvh for iframe-active
text = text.replace("height: 100vh !important;", "height: 100dvh !important;")

# Replace min-height: 100vh with 100dvh
text = text.replace("min-height: 100vh;", "min-height: 100dvh;")

# Also for jobs-page-wrapper
text = text.replace("min-height:100%;", "min-height:100dvh;")

with open('index.html', 'w') as f:
    f.write(text)
