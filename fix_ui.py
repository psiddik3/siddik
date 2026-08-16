import re

with open('index.html', 'r') as f:
    text = f.read()

# Fix 1: sm:rounded-[10px] to sm:rounded-full
text = text.replace('sm:rounded-[10px]', 'sm:rounded-full')

# Fix 2: Role and date order in generatePostHTML (Job post)
job_subtitle_old = """              <div class="flex items-center gap-[8px] text-[11.5px] text-slate-500 font-medium mt-[3px]">
                <span>${timeAgo}</span>
                <span>•</span>
                <span class="bg-slate-100 text-[#111827] px-[8px] py-[3px] rounded-[12px] text-[9px] font-bold uppercase tracking-wide">${escapeHtml(subtitleText)}</span>
              </div>"""

job_subtitle_new = """              <div class="flex items-center gap-[8px] text-[11.5px] text-slate-500 font-medium mt-[3px]">
                <span class="bg-slate-100 text-[#111827] px-[8px] py-[3px] rounded-[12px] text-[9px] font-bold uppercase tracking-wide">${escapeHtml(subtitleText)}</span>
                <span>•</span>
                <span>${timeAgo}</span>
              </div>"""

if job_subtitle_old in text:
    text = text.replace(job_subtitle_old, job_subtitle_new)
    print("Job subtitle replaced.")
else:
    print("Job subtitle NOT found.")

# Fix 3: Role and date order in generatePostHTML (Regular post)
reg_subtitle_old = """          <div class="flex items-center gap-[8px] text-[11.5px] text-slate-500 font-medium mt-[3px]">
            <span>${timeAgo}</span>
            <span>•</span>
            <span class="bg-slate-100 text-[#111827] px-[8px] py-[3px] rounded-[12px] text-[9px] font-bold uppercase tracking-wide">${escapeHtml(subtitle)}</span>
          </div>"""

reg_subtitle_new = """          <div class="flex items-center gap-[8px] text-[11.5px] text-slate-500 font-medium mt-[3px]">
            <span class="bg-slate-100 text-[#111827] px-[8px] py-[3px] rounded-[12px] text-[9px] font-bold uppercase tracking-wide">${escapeHtml(subtitle)}</span>
            <span>•</span>
            <span>${timeAgo}</span>
          </div>"""

if reg_subtitle_old in text:
    text = text.replace(reg_subtitle_old, reg_subtitle_new)
    print("Regular subtitle replaced.")
else:
    print("Regular subtitle NOT found.")

# Fix 4: avatar border-radius in media query
text = re.sub(
    r'(:is\(#startup-community-feed, \.startup-feed-wrapper\) \.avatar \{\s*width: 44px;\s*height: 44px;\s*)border-radius: 10px;',
    r'\1border-radius: 50%;',
    text
)

with open('index.html', 'w') as f:
    f.write(text)
