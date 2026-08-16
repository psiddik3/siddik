with open('index.html', 'r') as f:
    text = f.read()

old_markup = """            <div class="post-meta">
              <span>${formatTime(post.createdAt)}</span>
              <span>•</span>
              <span class="category-badge-meta">${escapeHtml(categoryLabel)}</span>
            </div>"""

new_markup = """            <div class="post-meta">
              <span class="category-badge-meta">${escapeHtml(categoryLabel)}</span>
              <span>•</span>
              <span>${formatTime(post.createdAt)}</span>
            </div>"""

if old_markup in text:
    text = text.replace(old_markup, new_markup)
    print("postMarkup subtitle replaced.")
else:
    print("postMarkup subtitle NOT found.")

with open('index.html', 'w') as f:
    f.write(text)
