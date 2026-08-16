import re

with open('index.html', 'r') as f:
    text = f.read()

# 1. Lowercase in save
text = text.replace('localStorage.setItem(STORAGE_GLOBAL_USERNAME, name.trim());', 'localStorage.setItem(STORAGE_GLOBAL_USERNAME, name.trim().toLowerCase());')

# 2. Lowercase in get
text = text.replace("function getStoredAuthorName() { return localStorage.getItem(STORAGE_GLOBAL_USERNAME) || ''; }", "function getStoredAuthorName() { return (localStorage.getItem(STORAGE_GLOBAL_USERNAME) || '').toLowerCase(); }")
text = text.replace("function getStoredCommenterName() { return localStorage.getItem(STORAGE_GLOBAL_USERNAME) || ''; }", "function getStoredCommenterName() { return (localStorage.getItem(STORAGE_GLOBAL_USERNAME) || '').toLowerCase(); }")

# 3. Lowercase in post author
text = text.replace('${escapeHtml(post.authorName)}', "${escapeHtml(String(post.authorName || '').toLowerCase())}")

# 4. Lowercase in recruiter name
text = text.replace('${escapeHtml(recruiterName)}', "${escapeHtml(String(recruiterName || '').toLowerCase())}")

# 5. Lowercase in comments c.name
text = text.replace('${escapeHtml(c.name)}', "${escapeHtml(String(c.name || '').toLowerCase())}")

# 6. Lowercase in community replies d.name
text = text.replace('${escapeHtml(d.name)}', "${escapeHtml(String(d.name || '').toLowerCase())}")

# 7. Lowercase postAuthorNameDisplay (the "You" text replacement)
old_name_display = "nameDisplay.innerText = name || 'You';"
new_name_display = "nameDisplay.innerText = (name || 'you').toLowerCase();"
text = text.replace(old_name_display, new_name_display)

text = text.replace('<span id="postAuthorNameDisplay" class="font-bold" style="padding-right: 4px;">You</span>', '<span id="postAuthorNameDisplay" class="font-bold" style="padding-right: 4px;">you</span>')

with open('index.html', 'w') as f:
    f.write(text)
