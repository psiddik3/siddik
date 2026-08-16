import re

with open('index.html', 'r') as f:
    text = f.read()

# Desktop .bottom-nav
text = text.replace("padding: 0.35rem 0.4rem;", "padding: 0.31rem 0.4rem;")

# Desktop .nav-item
text = text.replace("padding: 0.45rem 0.1rem;", "padding: 0.40rem 0.1rem;")

# Mobile .bottom-nav
text = text.replace("padding: 0.35rem 0.5rem;", "padding: 0.31rem 0.5rem;")

# Mobile .nav-item
text = text.replace("padding: 0.35rem 0;", "padding: 0.31rem 0;")

with open('index.html', 'w') as f:
    f.write(text)
