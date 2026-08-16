from bs4 import BeautifulSoup

with open('index.html', 'r') as f:
    soup = BeautifulSoup(f, 'html.parser')

body = soup.body
# The prompt says: div:nth-of-type(4) > div:nth-of-type(8) > div:nth-of-type(1)
# That means 4th div child of body -> 8th div child -> 1st div child.

try:
    div1 = soup.select_one('body > div:nth-of-type(4) > div:nth-of-type(8) > div:nth-of-type(1)')
    if div1:
        print("Found:", div1.name, div1.get('class', []), div1.get('id', ''))
    else:
        # Maybe it's just div:nth-of-type(4) without body >
        div2 = soup.select_one('div:nth-of-type(4) > div:nth-of-type(8) > div:nth-of-type(1)')
        if div2:
            print("Found (no body>):", div2.name, div2.get('class', []), div2.get('id', ''))
        else:
            print("Not found either.")
except Exception as e:
    print("Error:", e)
