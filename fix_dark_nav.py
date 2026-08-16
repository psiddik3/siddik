with open('index.html', 'r') as f:
    text = f.read()

# remove or replace dark mode overrides for bottom-nav to preserve the new glassmorphism

old_dark_nav = "    html.dark .bottom-nav { background: rgba(13, 13, 13, 0.95); border-color: #262626; border-top: 1px solid #262626; }"
new_dark_nav = "    /* html.dark .bottom-nav overridden by global glassmorphism */"
text = text.replace(old_dark_nav, new_dark_nav)

old_dark_item = "    html.dark .bottom-nav .nav-item { color: #f5f5f5; }"
new_dark_item = "    /* html.dark .bottom-nav .nav-item overridden */"
text = text.replace(old_dark_item, new_dark_item)

old_dark_active = "    html.dark .bottom-nav .nav-item.active, html.dark .bottom-nav .nav-item.active i { color: #0095f6; }"
new_dark_active = "    /* html.dark active item overridden */"
text = text.replace(old_dark_active, new_dark_active)

with open('index.html', 'w') as f:
    f.write(text)
