import re

with open('index.html', 'r') as f:
    text = f.read()

# Remove overflow-x-hidden from body class
text = text.replace('class="bg-[#f4f6fa] text-slate-800 font-sans antialiased overflow-x-hidden"', 'class="bg-[#f4f6fa] text-slate-800 font-sans antialiased"')

with open('index.html', 'w') as f:
    f.write(text)
