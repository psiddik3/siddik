with open('index.html', 'r') as f:
    text = f.read()

old_job_header = """          <div class="flex items-center justify-between px-1 sm:px-1.5 -mx-1 sm:-mx-1.5 pt-1.5 sm:pt-2 pb-0 sm:pb-0.5">
            <div class="flex items-center gap-2 min-w-0 -translate-x-[2.5%]">
              <div class="relative w-8 h-8 md:w-9 md:h-9 rounded-full overflow-hidden flex-shrink-0 flex items-center justify-center">
                ${profileLogo ? `<img src="${escapeHtml(profileLogo)}" class="absolute inset-0 w-full h-full object-cover" onerror="this.style.display='none';" referrerPolicy="no-referrer">` : ''}
                <div class="w-full h-full rounded-full flex items-center justify-center text-white font-bold text-sm md:text-base leading-none" style="background-color: ${avatarBg};">${(recruiterName || '?').charAt(0).toUpperCase()}</div>
              </div>
              <div class="flex flex-col min-w-0 flex-1 pr-2">
                <div class="font-bold text-[#111827] text-[13.5px] sm:text-[14.5px] flex items-center gap-1 leading-tight mb-0.5">
                  <span class="break-words" style="display:-webkit-box;-webkit-line-clamp:1;-webkit-box-orient:vertical;overflow:hidden; padding-right: 4px;">${escapeHtml(recruiterName)}</span>
                  <i class="fas fa-check-circle text-blue-600 text-[11px] sm:text-[12px] flex-shrink-0"></i>
                </div>
                <div class="text-[11px] sm:text-[11.5px] text-slate-500 font-medium leading-tight truncate">
                  ${subtitleText}
                </div>
              </div>
            </div>
            <button class="text-slate-400 hover:text-slate-600 p-1.5 transition-colors flex-shrink-0 -mt-1"><i class="fas fa-ellipsis-v text-sm"></i></button>
          </div>"""

new_job_header = """          <header class="flex items-center gap-[12px] mb-[14px] sm:mb-[18px] px-3 sm:px-5 pt-4 sm:pt-5">
            <div class="relative w-[38px] h-[38px] sm:w-[44px] sm:h-[44px] rounded-full sm:rounded-[10px] overflow-hidden shrink-0 flex items-center justify-center text-white font-black text-[11px] sm:text-[13px] uppercase tracking-wide bg-gradient-to-br from-[#8b5cf6] to-[#6d28d9]">
              ${profileLogo ? `<img src="${escapeHtml(profileLogo)}" class="absolute inset-0 w-full h-full object-cover" onerror="this.style.display='none';" referrerPolicy="no-referrer">` : ''}
              ${(recruiterName || '?').charAt(0)}
            </div>
            <div class="flex flex-col min-w-0 flex-1">
              <div class="flex items-center gap-1">
                <span class="font-extrabold text-[#111827] text-[15px] truncate leading-tight">${escapeHtml(recruiterName)}</span>
                <i class="fas fa-check-circle text-blue-600 text-[12px] shrink-0"></i>
              </div>
              <div class="flex items-center gap-[8px] text-[11.5px] text-slate-500 font-medium mt-[3px]">
                <span>${timeAgo}</span>
                <span>•</span>
                <span class="bg-slate-100 text-[#111827] px-[8px] py-[3px] rounded-[12px] text-[9px] font-bold uppercase tracking-wide">${escapeHtml(subtitleText)}</span>
              </div>
            </div>
            <button class="w-[32px] h-[32px] rounded-full flex items-center justify-center text-slate-500 hover:bg-slate-100 hover:text-[#111827] transition-colors shrink-0 text-[14px]" type="button" aria-label="More options">
              <svg class="w-4 h-4 fill-current"><use href="#i-more"></use></svg>
            </button>
          </header>"""


old_regular_header = """      <div class="flex items-center justify-between px-1 sm:px-1.5 -mx-1 sm:-mx-1.5 pt-1.5 sm:pt-2 pb-0 sm:pb-0.5">
        <div class="flex items-center gap-2 min-w-0 -translate-x-[2.5%]">
          <div class="w-8 h-8 md:w-9 md:h-9 rounded-full flex items-center justify-center text-white font-bold text-sm md:text-base flex-shrink-0 leading-none" style="background-color: ${avatarBg};">${(post.authorName || '?').charAt(0).toUpperCase()}</div>
          <div class="flex flex-col min-w-0 flex-1 pr-2">
            <div class="font-bold text-[#111827] text-[12px] sm:text-[13.5px] flex items-center gap-1 leading-tight mb-0.5">
              <span class="break-words" style="display:-webkit-box;-webkit-line-clamp:1;-webkit-box-orient:vertical;overflow:hidden; padding-right: 4px;">${escapeHtml(post.authorName)}</span>
              <i class="fas fa-check-circle text-blue-600 text-[11px] sm:text-[12px] flex-shrink-0"></i>
            </div>
            <div class="text-[10px] sm:text-[11px] text-slate-500 font-medium leading-tight truncate">
              ${escapeHtml(subtitle)} &bull; <span class="text-slate-400 font-normal whitespace-nowrap">${timeAgo}</span>
            </div>
          </div>
        </div>
        <button class="text-slate-500 hover:text-slate-800 p-2 transition-colors flex-shrink-0 -mt-2"><i class="fas fa-ellipsis-v text-lg"></i></button>
      </div>"""

new_regular_header = """      <header class="flex items-center gap-[12px] mb-[14px] sm:mb-[18px] px-3 sm:px-5 pt-4 sm:pt-5">
        <div class="w-[38px] h-[38px] sm:w-[44px] sm:h-[44px] rounded-full sm:rounded-[10px] text-white flex items-center justify-center font-black text-[11px] sm:text-[13px] uppercase tracking-wide shrink-0 bg-gradient-to-br from-[#8b5cf6] to-[#6d28d9]">
          ${(post.authorName || '?').charAt(0)}
        </div>
        <div class="flex flex-col min-w-0 flex-1">
          <div class="flex items-center gap-1">
            <span class="font-extrabold text-[#111827] text-[15px] truncate leading-tight">${escapeHtml(post.authorName)}</span>
            <i class="fas fa-check-circle text-blue-600 text-[12px] shrink-0"></i>
          </div>
          <div class="flex items-center gap-[8px] text-[11.5px] text-slate-500 font-medium mt-[3px]">
            <span>${timeAgo}</span>
            <span>•</span>
            <span class="bg-slate-100 text-[#111827] px-[8px] py-[3px] rounded-[12px] text-[9px] font-bold uppercase tracking-wide">${escapeHtml(subtitle)}</span>
          </div>
        </div>
        <button class="w-[32px] h-[32px] rounded-full flex items-center justify-center text-slate-500 hover:bg-slate-100 hover:text-[#111827] transition-colors shrink-0 text-[14px]" type="button" aria-label="More options">
          <svg class="w-4 h-4 fill-current"><use href="#i-more"></use></svg>
        </button>
      </header>"""

if old_job_header in text:
    text = text.replace(old_job_header, new_job_header)
    print("Job header replaced.")
else:
    print("Job header NOT found.")

if old_regular_header in text:
    text = text.replace(old_regular_header, new_regular_header)
    print("Regular header replaced.")
else:
    print("Regular header NOT found.")

with open('index.html', 'w') as f:
    f.write(text)
