with open('index.html', 'r') as f:
    text = f.read()

# 1. Padding Fix (Standardize to mb-[3px])
text = text.replace('mb-[3px] sm:mb-[3px]', 'mb-[3px] sm:mb-[3px]') # keep header container
# It's already mb-[3px]
# Filters padding
text = text.replace('style="margin-top: 2px;"', '')
text = text.replace('margin-bottom: 2px !important;', 'margin-bottom: 3px !important;')
text = text.replace('margin: 0 auto 2px auto;', 'margin: 0 auto 3px auto;')

# 2. Lowercase Username Fix
old_name_save = """      if (savedName) {
        setStoredAuthorName(savedName);
        setStoredCommenterName(savedName);"""
new_name_save = """      if (savedName) {
        savedName = savedName.toLowerCase();
        setStoredAuthorName(savedName);
        setStoredCommenterName(savedName);"""
if old_name_save in text:
    text = text.replace(old_name_save, new_name_save)
    print("Name save fixed!")

# 3. Mobile Header Badge & Time Spacing Fix
# Job header
old_job_subtitle = """              <div class="flex items-center gap-[6px] sm:gap-[8px] text-[10px] sm:text-[11.5px] text-slate-500 font-medium mt-[2px] sm:mt-[3px]">
                <span class="bg-slate-100 text-[#111827] px-[6px] sm:px-[8px] py-[2px] sm:py-[3px] rounded-[8px] sm:rounded-[12px] text-[8px] sm:text-[9px] font-bold uppercase tracking-wide">${escapeHtml(subtitleText)}</span>
                <span>•</span>
                <span>${timeAgo}</span>
              </div>"""

new_job_subtitle = """              <div class="flex items-center gap-[3px] sm:gap-[8px] text-[11px] sm:text-[11.5px] text-slate-500 font-medium mt-[1px] sm:mt-[3px]">
                <span class="bg-transparent sm:bg-slate-100 text-slate-500 sm:text-[#111827] px-0 sm:px-[8px] py-0 sm:py-[3px] rounded-none sm:rounded-[12px] text-[11px] sm:text-[9px] font-medium sm:font-bold capitalize sm:uppercase tracking-normal sm:tracking-wide">${escapeHtml(subtitleText)}</span>
                <span class="text-[9px] sm:text-[11.5px]">•</span>
                <span class="text-[10px] sm:text-[11.5px]">${timeAgo}</span>
              </div>"""

# Reg header
old_reg_subtitle = """          <div class="flex items-center gap-[6px] sm:gap-[8px] text-[10px] sm:text-[11.5px] text-slate-500 font-medium mt-[2px] sm:mt-[3px]">
            <span class="bg-slate-100 text-[#111827] px-[6px] sm:px-[8px] py-[2px] sm:py-[3px] rounded-[8px] sm:rounded-[12px] text-[8px] sm:text-[9px] font-bold uppercase tracking-wide">${escapeHtml(subtitle)}</span>
            <span>•</span>
            <span>${timeAgo}</span>
          </div>"""

new_reg_subtitle = """          <div class="flex items-center gap-[3px] sm:gap-[8px] text-[11px] sm:text-[11.5px] text-slate-500 font-medium mt-[1px] sm:mt-[3px]">
            <span class="bg-transparent sm:bg-slate-100 text-slate-500 sm:text-[#111827] px-0 sm:px-[8px] py-0 sm:py-[3px] rounded-none sm:rounded-[12px] text-[11px] sm:text-[9px] font-medium sm:font-bold capitalize sm:uppercase tracking-normal sm:tracking-wide">${escapeHtml(subtitle)}</span>
            <span class="text-[9px] sm:text-[11.5px]">•</span>
            <span class="text-[10px] sm:text-[11.5px]">${timeAgo}</span>
          </div>"""

if old_job_subtitle in text:
    text = text.replace(old_job_subtitle, new_job_subtitle)
    print("Job subtitle fixed!")
if old_reg_subtitle in text:
    text = text.replace(old_reg_subtitle, new_reg_subtitle)
    print("Reg subtitle fixed!")

with open('index.html', 'w') as f:
    f.write(text)
