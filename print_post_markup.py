with open('index.html', 'r') as f:
    text = f.read()

start = text.find('function postMarkup')
end = text.find('</article>`;', start)
print(text[start:end+12])
