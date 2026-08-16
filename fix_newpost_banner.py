with open('index.html', 'r') as f:
    text = f.read()

old_str = 'id="newPostBanner" class="bg-white rounded-[16px] shadow-[0_4px_24px_rgba(0,0,0,0.03)] border border-slate-100 py-2.5 px-3 mb-2 flex items-center justify-between cursor-pointer hover:bg-slate-50 transition-colors"'
new_str = 'id="newPostBanner" class="bg-white rounded-[16px] shadow-[0_4px_24px_rgba(0,0,0,0.03)] border border-slate-100 py-2.5 px-3 mb-[3px] flex items-center justify-between cursor-pointer hover:bg-slate-50 transition-colors"'

if old_str in text:
    text = text.replace(old_str, new_str)
    print("newPostBanner fixed!")
else:
    print("newPostBanner string not found!")

with open('index.html', 'w') as f:
    f.write(text)
