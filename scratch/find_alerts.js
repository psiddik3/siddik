import fs from 'fs';

const html = fs.readFileSync('index.html', 'utf8');
const lines = html.split('\n');

lines.forEach((line, i) => {
  if (line.includes('alertsContainer') || line.includes('iframe-alerts') || (line.includes('alerts') && line.includes('<div') && line.includes('id='))) {
    console.log(`${i + 1}: ${line.trim()}`);
  }
});
