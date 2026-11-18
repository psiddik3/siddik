import fs from 'fs';

const html = fs.readFileSync('index.html', 'utf8');

// 1. Home header
const homeHeaderMatch = html.match(/<div class="header-container[\s\S]*?<\/div>\s*<\/div>\s*<!-- Search Bar -->/);
if (homeHeaderMatch) console.log('HOME LOGO BLOCK:\n', homeHeaderMatch[0]);

// 2. Community header
const commTopMatch = html.match(/<div class="community-top">[\s\S]*?<\/div>/);
if (commTopMatch) console.log('COMMUNITY LOGO BLOCK:\n', commTopMatch[0]);

// 3. Jobs header
const jobsTopMatch = html.match(/<div style="display: flex; justify-content: space-between; align-items: center; width: 100%; margin-bottom: 2px;">[\s\S]*?<\/div>/);
if (jobsTopMatch) console.log('JOBS LOGO BLOCK:\n', jobsTopMatch[0]);

// 4. Startups header
const startupsTopMatch = html.match(/<header class="topbar">[\s\S]*?<div class="search-wrap"/);
if (startupsTopMatch) console.log('STARTUPS LOGO BLOCK:\n', startupsTopMatch[0]);
