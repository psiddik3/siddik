with open('index.html', 'r') as f:
    text = f.read()

start = text.find('function generatePostHTML(post) {')
end = text.find('      <div class="comments-section', start)

print(text[start:end])
