import re

with open('index.html', 'r') as f:
    text = f.read()

# Replace top: 0; left: 0; right: 0; bottom: 0; with top: 0; left: 0; right: 0; height: 100dvh;
text = text.replace("top: 0; left: 0; right: 0; bottom: 0;", "top: 0; left: 0; right: 0; height: 100dvh;")

# Add background to html
text = text.replace("body { background: #f4f6fa;", "html { background-color: #f4f6fa; }\n    body { background: #f4f6fa;")

with open('index.html', 'w') as f:
    f.write(text)
