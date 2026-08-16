import re
with open('index.html', 'r') as f:
    text = f.read()

# Change Community Creator to Community User
text = text.replace("'Community Creator'", "'Community User'")
text = text.replace('"Community Creator"', '"Community User"')

# Increase Avatar initial size (9px -> 13px) in headers
# Job Header
old_job_av = 'text-white font-black text-[9px] sm:text-[13px]'
new_job_av = 'text-white font-black text-[14px] sm:text-[16px]'
text = text.replace(old_job_av, new_job_av)

# Reg Header
old_reg_av = 'text-white flex items-center justify-center font-black text-[9px] sm:text-[13px]'
new_reg_av = 'text-white flex items-center justify-center font-black text-[14px] sm:text-[16px]'
text = text.replace(old_reg_av, new_reg_av)

# Reduce gap between header and content
old_head = 'mb-[10px] sm:mb-[18px]'
new_head = 'mb-[4px] sm:mb-[14px]'
text = text.replace(old_head, new_head)

# Image my-2 to mt-1 mb-1
text = text.replace('my-2 w-[calc(100%+24px)]', 'mt-1 mb-1 sm:my-2 w-[calc(100%+24px)]')

with open('index.html', 'w') as f:
    f.write(text)
