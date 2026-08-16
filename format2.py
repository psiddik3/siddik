import re
with open('index.html', 'r') as f:
    text = f.read()

# Reduce post-content padding
text = text.replace('<div class="post-content px-0 pt-0.5 pb-1">', '<div class="post-content px-0 pt-0 pb-0.5">')

# Reduce image container margin bottom
text = text.replace('mt-1 mb-1 sm:my-2', 'mt-1 mb-0 sm:my-2')

# In postMarkup (startup page), reduce title/content margins
old_title = """    :is(#startup-community-feed, .startup-feed-wrapper) .post-title {
      font-size: 16px;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.4;
      margin-bottom: 8px;
    }"""
new_title = """    :is(#startup-community-feed, .startup-feed-wrapper) .post-title {
      font-size: 16px;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.4;
      margin-bottom: 4px;
    }"""
text = text.replace(old_title, new_title)

old_copy = """    :is(#startup-community-feed, .startup-feed-wrapper) .post-copy {
      font-size: 14.5px;
      color: #9ca3af;
      line-height: 1.65;
      margin-bottom: 8px;
    }"""
new_copy = """    :is(#startup-community-feed, .startup-feed-wrapper) .post-copy {
      font-size: 14.5px;
      color: #9ca3af;
      line-height: 1.65;
      margin-bottom: 4px;
    }"""
text = text.replace(old_copy, new_copy)

with open('index.html', 'w') as f:
    f.write(text)
