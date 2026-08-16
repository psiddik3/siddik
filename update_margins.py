with open('index.html', 'r') as f:
    text = f.read()

import re
old_title_div = '<div class="mb-3">\n              <h3 class="text-[17px] sm:text-[18px] font-bold text-slate-800 leading-snug mb-0.5">${escapeHtml(job.title)}</h3>'
new_title_div = '<div class="mb-1.5">\n              <h3 class="text-[17px] sm:text-[18px] font-bold text-slate-800 leading-snug mb-0.5">${escapeHtml(job.title)}</h3>'

old_msg_div = '<div class="text-slate-700 text-[14.5px] sm:text-[15px] leading-relaxed mb-3">'
new_msg_div = '<div class="text-slate-700 text-[14.5px] sm:text-[15px] leading-relaxed mb-2">'

old_meta_div = '<div class="flex items-center justify-start gap-3 sm:gap-3 flex-nowrap text-[12px] sm:text-[14.5px] text-slate-500 font-medium py-1.5 px-0 mb-3 w-full max-w-full overflow-x-auto whitespace-nowrap no-scrollbar"'
new_meta_div = '<div class="flex items-center justify-start gap-3 sm:gap-3 flex-nowrap text-[12px] sm:text-[14.5px] text-slate-500 font-medium py-0.5 px-0 mb-1.5 w-full max-w-full overflow-x-auto whitespace-nowrap no-scrollbar"'

text = text.replace(old_title_div, new_title_div)
text = text.replace(old_msg_div, new_msg_div)
text = text.replace(old_meta_div, new_meta_div)

with open('index.html', 'w') as f:
    f.write(text)
