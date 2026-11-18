import re

with open('index.html', 'r') as f:
    text = f.read()

bad = """  jobs = filteredJobs;
  container.innerHTML = jobs.map((j, idx) => {"""

good = """  jobs = filteredJobs;
  let prefixHtml = "";
  if (window.jobsTargetPostId) {
      prefixHtml = `<div class="mb-3 px-1"><button onclick="window.location.hash='jobs'" class="text-white font-semibold text-sm flex items-center gap-2 hover:bg-white/10 px-3 py-1.5 rounded-full transition-colors"><i class="fas fa-arrow-left"></i> Back to feed</button></div>`;
  }
  container.innerHTML = prefixHtml + jobs.map((j, idx) => {"""

if bad in text:
    text = text.replace(bad, good)
else:
    print("BAD NOT FOUND")
    
with open('index.html', 'w') as f:
    f.write(text)

