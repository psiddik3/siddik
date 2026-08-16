with open('index.html', 'r') as f:
    text = f.read()

text = text.replace(
    '<header class="flex items-center gap-[12px] mb-[14px] sm:mb-[18px] px-3 sm:px-5 pt-4 sm:pt-5">',
    '<header class="flex items-center gap-[12px] mb-[14px] sm:mb-[18px]">'
)

with open('index.html', 'w') as f:
    f.write(text)
