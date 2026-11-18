import fs from 'fs';

const html = fs.readFileSync('index.html', 'utf8');
const lines = html.split('\n');

lines.forEach((line, i) => {
  if (line.includes('header') || line.includes('topbar') || line.includes('brand') || line.includes('Spred') || line.includes('Spread')) {
    if (line.includes('class=') || line.includes('id=') || line.includes('<h1') || line.includes('<div')) {
      console.log(`${i + 1}: ${line.trim()}`);
    }
  }
});
