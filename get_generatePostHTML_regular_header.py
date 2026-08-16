with open('index.html', 'r') as f:
    text = f.read()

start = text.find('return `<article class="post-card bg-white', text.find('return `<article class="post-card bg-white')+1)
end = text.find('      <div class="post-content px-0 pt-0.5 pb-1">', start)

print(text[start:end])
