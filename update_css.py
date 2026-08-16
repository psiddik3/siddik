with open('index.html', 'r') as f:
    text = f.read()

# Update mobile post-head
old_post_head = """    :is(#startup-community-feed, .startup-feed-wrapper) .post-head {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 14px;
    }"""
new_post_head = """    :is(#startup-community-feed, .startup-feed-wrapper) .post-head {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 4px;
    }"""
text = text.replace(old_post_head, new_post_head)

# Update mobile avatar
old_avatar = """    :is(#startup-community-feed, .startup-feed-wrapper) .avatar {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      aspect-ratio: 1 / 1;
      flex-shrink: 0;
      overflow: hidden;
      background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%);
      color: #ffffff;
      display: grid;
      place-items: center;
      font-size: 11px;"""
new_avatar = """    :is(#startup-community-feed, .startup-feed-wrapper) .avatar {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      aspect-ratio: 1 / 1;
      flex-shrink: 0;
      overflow: hidden;
      background: linear-gradient(135deg, #8b5cf6 0%, #6d28d9 100%);
      color: #ffffff;
      display: grid;
      place-items: center;
      font-size: 14px;"""
text = text.replace(old_avatar, new_avatar)

# Update mobile author-name & post-meta spacing
old_meta = """    :is(#startup-community-feed, .startup-feed-wrapper) .post-meta {
      display: flex;
      align-items: center;
      gap: 6px;
      margin-top: 2px;
    }"""
new_meta = """    :is(#startup-community-feed, .startup-feed-wrapper) .post-meta {
      display: flex;
      align-items: center;
      gap: 4px;
      margin-top: 1px;
    }"""
text = text.replace(old_meta, new_meta)

with open('index.html', 'w') as f:
    f.write(text)
