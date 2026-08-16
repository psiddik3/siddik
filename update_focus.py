with open('index.html', 'r') as f:
    text = f.read()

new_rule = """
div:nth-of-type(4) > div#feedContainer:nth-of-type(4) > article:nth-of-type(1) > div:nth-of-type(1) > div:nth-of-type(1) {
  width: 325px !important;
}
"""

style_end_idx = text.rfind('</style>')
if style_end_idx != -1:
    text = text[:style_end_idx] + new_rule + text[style_end_idx:]

with open('index.html', 'w') as f:
    f.write(text)
