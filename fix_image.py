with open('index.html', 'r') as f:
    text = f.read()

old_css = """    .post-cover-img-wrap {
      width: 100% !important;
      margin: 12px 0 !important;
      padding: 0 !important;
      border-radius: 12px !important;
      overflow: hidden;
    }"""

new_css = """    .post-cover-img-wrap {
      width: 100%;
      margin-top: 12px !important;
      margin-bottom: 12px !important;
      margin-left: 0;
      margin-right: 0;
      padding: 0 !important;
      border-radius: 0 !important;
      overflow: hidden;
    }"""

text = text.replace(old_css, new_css)

with open('index.html', 'w') as f:
    f.write(text)
