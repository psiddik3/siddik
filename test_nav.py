with open('index.html', 'r') as f:
    text = f.read()

if "rgba(255, 255, 255, 0.75)" in text:
    print("background is glossy white")
if "flex: 1 1 0px" in text:
    print("flex is correct")
