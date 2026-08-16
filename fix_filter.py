with open('index.html', 'r') as f:
    text = f.read()

old_code = 'document.querySelectorAll(".category-btn").forEach(btn => btn.addEventListener("click", () => window.setStartupFilter(btn.dataset.filter)));'
new_code = 'document.querySelectorAll("#iframe-startups .category-btn").forEach(btn => btn.addEventListener("click", () => { if(btn.dataset.filter) window.setStartupFilter(btn.dataset.filter); }));'

if old_code in text:
    text = text.replace(old_code, new_code)
else:
    print("Old code not found!")

old_set_filter = 'document.querySelectorAll(".category-btn").forEach(btn => btn.classList.toggle("active", btn.dataset.filter === filter));'
new_set_filter = 'document.querySelectorAll("#iframe-startups .category-btn").forEach(btn => btn.classList.toggle("active", btn.dataset.filter === filter));'

if old_set_filter in text:
    text = text.replace(old_set_filter, new_set_filter)
else:
    print("Old set filter not found!")

with open('index.html', 'w') as f:
    f.write(text)
