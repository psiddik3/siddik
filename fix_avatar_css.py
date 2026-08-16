with open('index.html', 'r') as f:
    text = f.read()

# Replace "uppercase" in avatar classes
old_job_av = 'text-white font-black text-[14px] sm:text-[16px] uppercase tracking-wide'
new_job_av = 'text-white font-black text-[14px] sm:text-[16px] tracking-wide'
text = text.replace(old_job_av, new_job_av)

old_reg_av = 'text-white flex items-center justify-center font-black text-[14px] sm:text-[16px] uppercase tracking-wide'
new_reg_av = 'text-white flex items-center justify-center font-black text-[14px] sm:text-[16px] tracking-wide'
text = text.replace(old_reg_av, new_reg_av)

# Also fix the charAt(0) lowercasing for good measure
text = text.replace("${(post.authorName || '?').charAt(0)}", "${(post.authorName || '?').charAt(0).toLowerCase()}")
text = text.replace("${(recruiterName || '?').charAt(0)}", "${(recruiterName || '?').charAt(0).toLowerCase()}")

# What about the startup page avatar?
# <span class="avatar" style="--avatar:#8b5cf6">SP</span> -> It doesn't have an uppercase class, but SP is hardcoded uppercase. Since it's Spred One, we leave it.

with open('index.html', 'w') as f:
    f.write(text)
