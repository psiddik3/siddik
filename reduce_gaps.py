with open('index.html', 'r') as f:
    text = f.read()

# 1. Update CSS margin-bottoms for post cards
text = text.replace('margin-bottom: 12px !important;', 'margin-bottom: 3px !important;')
text = text.replace('margin-bottom: 10px !important;', 'margin-bottom: 2px !important;')

# 2. Update gaps between major sections:
# Header
text = text.replace('mb-1.5 sm:mb-2', 'mb-[3px] sm:mb-[3px]')
# Post Creation Card
text = text.replace('id="postCreationCard" class="bg-white rounded-[16px] shadow-[0_4px_24px_rgba(0,0,0,0.03)] border border-slate-100 p-1.5 sm:p-2 mb-1.5"', 'id="postCreationCard" class="bg-white rounded-[16px] shadow-[0_4px_24px_rgba(0,0,0,0.03)] border border-slate-100 p-1.5 sm:p-2 mb-[3px]"')
# New Post Banner
text = text.replace('id="newPostBanner" class="bg-white rounded-[16px] shadow-[0_4px_24px_rgba(0,0,0,0.03)] border border-slate-100 px-3 py-2 sm:px-4 sm:py-2.5 mb-1.5 flex items-center shadow-sm cursor-pointer hover:bg-slate-50 transition-colors"', 'id="newPostBanner" class="bg-white rounded-[16px] shadow-[0_4px_24px_rgba(0,0,0,0.03)] border border-slate-100 px-3 py-2 sm:px-4 sm:py-2.5 mb-[3px] flex items-center shadow-sm cursor-pointer hover:bg-slate-50 transition-colors"')

# 3. Post Markup mb-1.5
text = text.replace('<article class="post-card bg-white rounded-[16px] sm:rounded-[20px] mb-1.5 border border-slate-100 shadow-[0_4px_24px_rgba(0,0,0,0.03)] overflow-hidden"', '<article class="post-card bg-white rounded-[16px] sm:rounded-[20px] mb-[3px] border border-slate-100 shadow-[0_4px_24px_rgba(0,0,0,0.03)] overflow-hidden"')

with open('index.html', 'w') as f:
    f.write(text)
print("Done!")
