with open('index.html', 'r') as f:
    text = f.read()
if "rgba(255, 255, 255, 0.85)" in text:
    print("background is right")
if "color: #000;" in text:
    print("active color is right")
