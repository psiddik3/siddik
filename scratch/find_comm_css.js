import fs from 'fs';

const html = fs.readFileSync('index.html', 'utf8');
const lines = html.split('\n');

lines.forEach((line, i) => {
  if (line.includes('.community-page') || line.includes('.community-unified-box') || line.includes('community-container') || line.includes('#discussionsList')) {
    console.log(`${i + 1}: ${line.trim().slice(0, 120)}`);
  }
});
