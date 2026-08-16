with open('index.html', 'r') as f:
    text = f.read()

text = text.replace('margin: 16px auto 16px !important;', 'margin: 2px auto 2px !important;')
text = text.replace('style="margin-top: 10px;"', 'style="margin-top: 2px;"')
text = text.replace('margin-bottom: 20px;', 'margin-bottom: 2px;') # generic margin bottoms just in case? Actually maybe better not to touch generic ones unless specified.
with open('index.html', 'w') as f:
    f.write(text)
print("Done!")
