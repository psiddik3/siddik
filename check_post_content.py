with open('index.html', 'r') as f:
    text = f.read()

start = text.find('return `<article class="post-card bg-white')
end = text.find('      <div class="comments-section', start)

print(text[start:end])
