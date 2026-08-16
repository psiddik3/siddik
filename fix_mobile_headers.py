with open('index.html', 'r') as f:
    text = f.read()

# Job Post Header Fix
old_job_header = """          <header class="flex items-center gap-[12px] mb-[14px] sm:mb-[18px]">
            <div class="relative w-[38px] h-[38px] sm:w-[44px] sm:h-[44px] rounded-full sm:rounded-full overflow-hidden shrink-0 flex items-center justify-center text-white font-black text-[11px] sm:text-[13px] uppercase tracking-wide bg-gradient-to-br from-[#8b5cf6] to-[#6d28d9]">
              ${profileLogo ? `<img src="${escapeHtml(profileLogo)}" class="absolute inset-0 w-full h-full object-cover" onerror="this.style.display='none';" referrerPolicy="no-referrer">` : ''}
              ${(recruiterName || '?').charAt(0)}
            </div>
            <div class="flex flex-col min-w-0 flex-1">
              <div class="flex items-center gap-1">
                <span class="font-extrabold text-[#111827] text-[15px] truncate leading-tight">${escapeHtml(recruiterName)}</span>
                <i class="fas fa-check-circle text-blue-600 text-[12px] shrink-0"></i>
              </div>
              <div class="flex items-center gap-[8px] text-[11.5px] text-slate-500 font-medium mt-[3px]">
                <span class="bg-slate-100 text-[#111827] px-[8px] py-[3px] rounded-[12px] text-[9px] font-bold uppercase tracking-wide">${escapeHtml(subtitleText)}</span>
                <span>•</span>
                <span>${timeAgo}</span>
              </div>
            </div>
            <button class="w-[32px] h-[32px] rounded-full flex items-center justify-center text-slate-500 hover:bg-slate-100 hover:text-[#111827] transition-colors shrink-0 text-[14px]" type="button" aria-label="More options">
              <svg class="w-4 h-4 fill-current"><use href="#i-more"></use></svg>
            </button>
          </header>"""

new_job_header = """          <header class="flex items-center gap-[8px] sm:gap-[12px] mb-[10px] sm:mb-[18px]">
            <div class="relative w-[28px] h-[28px] sm:w-[44px] sm:h-[44px] rounded-full sm:rounded-full overflow-hidden shrink-0 flex items-center justify-center text-white font-black text-[9px] sm:text-[13px] uppercase tracking-wide bg-gradient-to-br from-[#8b5cf6] to-[#6d28d9]">
              ${profileLogo ? `<img src="${escapeHtml(profileLogo)}" class="absolute inset-0 w-full h-full object-cover" onerror="this.style.display='none';" referrerPolicy="no-referrer">` : ''}
              ${(recruiterName || '?').charAt(0)}
            </div>
            <div class="flex flex-col min-w-0 flex-1">
              <div class="flex items-center gap-1">
                <span class="font-extrabold text-[#111827] text-[13px] sm:text-[15px] truncate leading-tight">${escapeHtml(recruiterName)}</span>
                <i class="fas fa-check-circle text-blue-600 text-[10px] sm:text-[12px] shrink-0"></i>
              </div>
              <div class="flex items-center gap-[6px] sm:gap-[8px] text-[10px] sm:text-[11.5px] text-slate-500 font-medium mt-[2px] sm:mt-[3px]">
                <span class="bg-slate-100 text-[#111827] px-[6px] sm:px-[8px] py-[2px] sm:py-[3px] rounded-[8px] sm:rounded-[12px] text-[8px] sm:text-[9px] font-bold uppercase tracking-wide">${escapeHtml(subtitleText)}</span>
                <span>•</span>
                <span>${timeAgo}</span>
              </div>
            </div>
            <button class="w-[26px] h-[26px] sm:w-[32px] sm:h-[32px] rounded-full flex items-center justify-center text-slate-500 hover:bg-slate-100 hover:text-[#111827] transition-colors shrink-0 text-[12px] sm:text-[14px]" type="button" aria-label="More options">
              <svg class="w-3.5 h-3.5 sm:w-4 sm:h-4 fill-current"><use href="#i-more"></use></svg>
            </button>
          </header>"""

if old_job_header in text:
    text = text.replace(old_job_header, new_job_header)
    print("Job header replaced.")
else:
    print("Job header not found.")

# Regular Post Header Fix
old_reg_header = """      <header class="flex items-center gap-[12px] mb-[14px] sm:mb-[18px]">
        <div class="w-[38px] h-[38px] sm:w-[44px] sm:h-[44px] rounded-full sm:rounded-full text-white flex items-center justify-center font-black text-[11px] sm:text-[13px] uppercase tracking-wide shrink-0 bg-gradient-to-br from-[#8b5cf6] to-[#6d28d9]">
          ${(post.authorName || '?').charAt(0)}
        </div>
        <div class="flex flex-col min-w-0 flex-1">
          <div class="flex items-center gap-1">
            <span class="font-extrabold text-[#111827] text-[15px] truncate leading-tight">${escapeHtml(post.authorName)}</span>
            <i class="fas fa-check-circle text-blue-600 text-[12px] shrink-0"></i>
          </div>
          <div class="flex items-center gap-[8px] text-[11.5px] text-slate-500 font-medium mt-[3px]">
            <span class="bg-slate-100 text-[#111827] px-[8px] py-[3px] rounded-[12px] text-[9px] font-bold uppercase tracking-wide">${escapeHtml(subtitle)}</span>
            <span>•</span>
            <span>${timeAgo}</span>
          </div>
        </div>
        <button class="w-[32px] h-[32px] rounded-full flex items-center justify-center text-slate-500 hover:bg-slate-100 hover:text-[#111827] transition-colors shrink-0 text-[14px]" type="button" aria-label="More options">
          <svg class="w-4 h-4 fill-current"><use href="#i-more"></use></svg>
        </button>
      </header>"""

new_reg_header = """      <header class="flex items-center gap-[8px] sm:gap-[12px] mb-[10px] sm:mb-[18px]">
        <div class="w-[28px] h-[28px] sm:w-[44px] sm:h-[44px] rounded-full sm:rounded-full text-white flex items-center justify-center font-black text-[9px] sm:text-[13px] uppercase tracking-wide shrink-0 bg-gradient-to-br from-[#8b5cf6] to-[#6d28d9]">
          ${(post.authorName || '?').charAt(0)}
        </div>
        <div class="flex flex-col min-w-0 flex-1">
          <div class="flex items-center gap-1">
            <span class="font-extrabold text-[#111827] text-[13px] sm:text-[15px] truncate leading-tight">${escapeHtml(post.authorName)}</span>
            <i class="fas fa-check-circle text-blue-600 text-[10px] sm:text-[12px] shrink-0"></i>
          </div>
          <div class="flex items-center gap-[6px] sm:gap-[8px] text-[10px] sm:text-[11.5px] text-slate-500 font-medium mt-[2px] sm:mt-[3px]">
            <span class="bg-slate-100 text-[#111827] px-[6px] sm:px-[8px] py-[2px] sm:py-[3px] rounded-[8px] sm:rounded-[12px] text-[8px] sm:text-[9px] font-bold uppercase tracking-wide">${escapeHtml(subtitle)}</span>
            <span>•</span>
            <span>${timeAgo}</span>
          </div>
        </div>
        <button class="w-[26px] h-[26px] sm:w-[32px] sm:h-[32px] rounded-full flex items-center justify-center text-slate-500 hover:bg-slate-100 hover:text-[#111827] transition-colors shrink-0 text-[12px] sm:text-[14px]" type="button" aria-label="More options">
          <svg class="w-3.5 h-3.5 sm:w-4 sm:h-4 fill-current"><use href="#i-more"></use></svg>
        </button>
      </header>"""

if old_reg_header in text:
    text = text.replace(old_reg_header, new_reg_header)
    print("Reg header replaced.")
else:
    print("Reg header not found.")

with open('index.html', 'w') as f:
    f.write(text)
