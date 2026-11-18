import fs from 'fs';

const html = fs.readFileSync('index.html', 'utf8');
const lines = html.split('\n');

lines.forEach((line, i) => {
  if (line.includes('Spread') || line.includes('spread-') || line.includes('brand') || line.includes('logo')) {
    if (line.includes('One') || line.includes('h1') || line.includes('h2') || line.includes('header') || line.includes('font-extrabold') || line.includes('logo')) {
      console.log(`${i + 1}: ${line.trim().slice(0, 120)}`);
    }
  }
});
