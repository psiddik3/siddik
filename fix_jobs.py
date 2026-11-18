import re

with open('index.html', 'r') as f:
    text = f.read()

bad_jobs_patch = """  if (window.jobsTargetPostId) {
      container.innerHTML = `<div class="mb-3 px-1"><button onclick="window.location.hash='jobs'" class="text-white font-semibold text-sm flex items-center gap-2 hover:bg-white/10 px-3 py-1.5 rounded-full transition-colors"><i class="fas fa-arrow-left"></i> Back to feed</button></div>`;
      if (!filteredJobs.length) {
          container.innerHTML += `<div class="empty-state">✨ Job not found.</div>`;
          return;
      }
  } else {
      if(!filteredJobs.length){
        container.innerHTML = `<div class="empty-state">✨ No matching jobs. Adjust filters.</div>`;
        return;
      }
      container.innerHTML = "";
  }
  jobs = filteredJobs;
  container.innerHTML = jobs.map((j, idx) => {"""

good_jobs_patch = """  let outHtml = "";
  if (window.jobsTargetPostId) {
      outHtml = `<div class="mb-3 px-1"><button onclick="window.location.hash='jobs'" class="text-white font-semibold text-sm flex items-center gap-2 hover:bg-white/10 px-3 py-1.5 rounded-full transition-colors"><i class="fas fa-arrow-left"></i> Back to feed</button></div>`;
      if (!filteredJobs.length) {
          outHtml += `<div class="empty-state">✨ Job not found.</div>`;
          container.innerHTML = outHtml;
          return;
      }
  } else {
      if(!filteredJobs.length){
        container.innerHTML = `<div class="empty-state">✨ No matching jobs. Adjust filters.</div>`;
        return;
      }
  }
  jobs = filteredJobs;
  container.innerHTML = outHtml + jobs.map((j, idx) => {"""

if bad_jobs_patch in text:
    text = text.replace(bad_jobs_patch, good_jobs_patch)
else:
    print("BAD JOBS PATCH NOT FOUND")
    
with open('index.html', 'w') as f:
    f.write(text)

