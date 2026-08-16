import re

with open('index.html', 'r') as f:
    text = f.read()

# Remove padding from #feedContainer
text = re.sub(r'(#feedContainer \{.*?)padding-bottom: max\(80px, calc\(80px \+ env\(safe-area-inset-bottom\)\)\); ', r'\1', text)

with open('index.html', 'w') as f:
    f.write(text)
