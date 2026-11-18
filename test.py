import re

with open('index.html', 'r') as f:
    text = f.read()

print("FOUND renderDiscussions:", "renderDiscussions()" in text)
