with open('index.html', 'r') as f:
    text = f.read()

old_css = """    :is(#startup-community-feed, .startup-feed-wrapper) .post-cover-img-wrap {
      width: calc(100% + 28px);
      margin-left: -14px;
      margin-right: -14px;
      max-height: none;
      overflow: hidden;
      position: relative;
    }"""

new_css = """    :is(#startup-community-feed, .startup-feed-wrapper) .post-cover-img-wrap {
      max-height: none;
      overflow: hidden;
      position: relative;
    }"""

text = text.replace(old_css, new_css)

with open('index.html', 'w') as f:
    f.write(text)
