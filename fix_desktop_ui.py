import re

with open('index.html', 'r') as f:
    text = f.read()

# Fix desktop buttons gap
old_buttons = 'class="grid grid-cols-3 items-center px-0 border-t border-slate-50/50"'
new_buttons = 'class="grid grid-cols-3 sm:flex sm:justify-start sm:gap-8 items-center px-0 border-t border-slate-50/50"'
text = text.replace(old_buttons, new_buttons)

# Fix background on desktop for subtitle (badge)
old_subtitle_span = 'class="bg-transparent sm:bg-slate-100 text-slate-500 sm:text-[#111827] px-0 sm:px-[8px] py-0 sm:py-[3px] rounded-none sm:rounded-[12px] text-[11px] sm:text-[9px] font-medium sm:font-bold capitalize sm:uppercase tracking-normal sm:tracking-wide"'
# User said: "remove it... Make it as the desktop version in Community Creator." 
# I will just remove the background and make it look like the mobile version (no background, normal text) across both desktop and mobile.
new_subtitle_span = 'class="bg-transparent text-slate-500 px-0 py-0 rounded-none text-[11px] sm:text-[11px] font-medium sm:font-medium capitalize tracking-normal"'
text = text.replace(old_subtitle_span, new_subtitle_span)

# Fix Community Creator -> Community User
text = text.replace("subtitle = 'Creator';", "subtitle = 'Community User';")
text = text.replace("subtitle = 'Community Member';", "subtitle = 'Community User';")
text = text.replace("subtitle = 'Community User'", "subtitle = 'Community User'")

with open('index.html', 'w') as f:
    f.write(text)
