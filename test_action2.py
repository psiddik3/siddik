with open('index.html', 'r') as f:
    text = f.read()

# Job block
old_job = """          <div class="flex items-center justify-between px-0 border-t border-slate-50/50">
            <button class="appreciate-btn flex items-center gap-[4px] text-slate-500 font-medium text-[12.5px] sm:text-[13.5px] hover:bg-slate-50 pl-0 pr-2 py-1 rounded-full transition-colors" data-post-id="${post.id}">
              <i class="${heartClass} text-[13px] sm:text-[14px]"></i> <span>Appreciate</span>
              <span class="appreciate-count text-[12.5px] sm:text-[13.5px] font-bold text-center ml-[1px] ${post.appreciations > 0 ? 'text-slate-500' : 'hidden'}">${post.appreciations > 0 ? post.appreciations : ''}</span>
            </button>
            <button class="comment-trigger-btn flex items-center gap-[4px] text-slate-500 font-medium text-[12.5px] sm:text-[13.5px] hover:bg-slate-50 px-2 py-1 rounded-full transition-colors" data-post-id="${post.id}">
              <i class="far fa-comment text-[13px] sm:text-[14px]"></i> <span>Comment</span>
              <span class="comment-badge text-[12.5px] sm:text-[13.5px] font-bold text-center ml-[1px] ${commentCount > 0 ? 'text-slate-500' : 'hidden'}">${commentCount > 0 ? commentCount : ''}</span>
            </button>
            <button class="share-btn flex items-center gap-[4px] text-slate-500 font-medium text-[12.5px] sm:text-[13.5px] hover:bg-slate-50 pr-0 pl-2 py-1 rounded-full transition-colors" data-post-id="${post.id}">
              <i class="far fa-share-square text-[13px] sm:text-[14px]"></i> <span>Share</span>
            </button>
          </div>"""

new_job = """          <div class="grid grid-cols-3 items-center px-0 border-t border-slate-50/50">
            <button class="appreciate-btn justify-self-start flex items-center gap-[4px] text-slate-500 font-medium text-[12.5px] sm:text-[13.5px] hover:bg-slate-50 pl-0 pr-2 py-1 rounded-full transition-colors" data-post-id="${post.id}">
              <i class="${heartClass} text-[13px] sm:text-[14px]"></i> <span>Appreciate</span>
              <span class="appreciate-count text-[12.5px] sm:text-[13.5px] font-bold text-center ml-[1px] ${post.appreciations > 0 ? 'text-slate-500' : 'hidden'}">${post.appreciations > 0 ? post.appreciations : ''}</span>
            </button>
            <button class="comment-trigger-btn justify-self-center flex items-center gap-[4px] text-slate-500 font-medium text-[12.5px] sm:text-[13.5px] hover:bg-slate-50 px-2 py-1 rounded-full transition-colors" data-post-id="${post.id}">
              <i class="far fa-comment text-[13px] sm:text-[14px]"></i> <span>Comment</span>
              <span class="comment-badge text-[12.5px] sm:text-[13.5px] font-bold text-center ml-[1px] ${commentCount > 0 ? 'text-slate-500' : 'hidden'}">${commentCount > 0 ? commentCount : ''}</span>
            </button>
            <button class="share-btn justify-self-end flex items-center gap-[4px] text-slate-500 font-medium text-[12.5px] sm:text-[13.5px] hover:bg-slate-50 pr-0 pl-2 py-1 rounded-full transition-colors" data-post-id="${post.id}">
              <i class="far fa-share-square text-[13px] sm:text-[14px]"></i> <span>Share</span>
            </button>
          </div>"""
if old_job in text:
    text = text.replace(old_job, new_job)
    print("Replaced job buttons.")

# Standard post block
old_std = """      <div class="flex items-center justify-between px-0 border-t border-slate-50/50">
        <button class="appreciate-btn flex items-center gap-[4px] text-slate-600 font-normal text-[13px] sm:text-[14.5px] hover:bg-slate-50 pl-0 pr-2 py-1 rounded-full transition-colors" data-post-id="${post.id}">
          <i class="${heartClass} text-[13px] sm:text-[14px]"></i> <span>Appreciate</span>
          <span class="appreciate-count text-[13px] sm:text-[14px] font-bold text-center ml-[1px] ${post.appreciations > 0 ? 'text-slate-600' : 'hidden'}">${post.appreciations > 0 ? post.appreciations : ''}</span>
        </button>
        <button class="comment-trigger-btn flex items-center gap-[4px] text-slate-600 font-normal text-[13px] sm:text-[14.5px] hover:bg-slate-50 px-2 py-1 rounded-full transition-colors" data-post-id="${post.id}">
          <i class="far fa-comment text-[13px] sm:text-[14px]"></i> <span>Comment</span>
          <span class="comment-badge text-[13px] sm:text-[14px] font-bold text-center ml-[1px] ${commentCount > 0 ? 'text-slate-600' : 'hidden'}">${commentCount > 0 ? commentCount : ''}</span>
        </button>
        <button class="share-btn flex items-center gap-[4px] text-slate-600 font-normal text-[13px] sm:text-[14.5px] hover:bg-slate-50 pr-0 pl-2 py-1 rounded-full transition-colors" data-post-id="${post.id}">
          <i class="far fa-share-square text-[13px] sm:text-[14px]"></i> <span>Share</span>
        </button>
      </div>"""
new_std = """      <div class="grid grid-cols-3 items-center px-0 border-t border-slate-50/50">
        <button class="appreciate-btn justify-self-start flex items-center gap-[4px] text-slate-600 font-normal text-[13px] sm:text-[14.5px] hover:bg-slate-50 pl-0 pr-2 py-1 rounded-full transition-colors" data-post-id="${post.id}">
          <i class="${heartClass} text-[13px] sm:text-[14px]"></i> <span>Appreciate</span>
          <span class="appreciate-count text-[13px] sm:text-[14px] font-bold text-center ml-[1px] ${post.appreciations > 0 ? 'text-slate-600' : 'hidden'}">${post.appreciations > 0 ? post.appreciations : ''}</span>
        </button>
        <button class="comment-trigger-btn justify-self-center flex items-center gap-[4px] text-slate-600 font-normal text-[13px] sm:text-[14.5px] hover:bg-slate-50 px-2 py-1 rounded-full transition-colors" data-post-id="${post.id}">
          <i class="far fa-comment text-[13px] sm:text-[14px]"></i> <span>Comment</span>
          <span class="comment-badge text-[13px] sm:text-[14px] font-bold text-center ml-[1px] ${commentCount > 0 ? 'text-slate-600' : 'hidden'}">${commentCount > 0 ? commentCount : ''}</span>
        </button>
        <button class="share-btn justify-self-end flex items-center gap-[4px] text-slate-600 font-normal text-[13px] sm:text-[14.5px] hover:bg-slate-50 pr-0 pl-2 py-1 rounded-full transition-colors" data-post-id="${post.id}">
          <i class="far fa-share-square text-[13px] sm:text-[14px]"></i> <span>Share</span>
        </button>
      </div>"""
if old_std in text:
    text = text.replace(old_std, new_std)
    print("Replaced std buttons.")

with open('index.html', 'w') as f:
    f.write(text)
