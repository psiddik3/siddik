with open('index.html', 'r') as f:
    text = f.read()

text = text.replace(
    '-mx-[14px] sm:-mx-[14px] w-[calc(100%+28px)]',
    '-mx-[12px] sm:-mx-[14px] w-[calc(100%+24px)] sm:w-[calc(100%+28px)]'
)

text = text.replace(
    '-mx-3.5 sm:-mx-[14px] my-2 w-[calc(100%+28px)]',
    '-mx-[12px] sm:-mx-[14px] my-2 w-[calc(100%+24px)] sm:w-[calc(100%+28px)]'
)

with open('index.html', 'w') as f:
    f.write(text)
