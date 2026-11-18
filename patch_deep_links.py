import re

with open('index.html', 'r') as f:
    text = f.read()

# 1. Update handleRouting to set target IDs and re-render
routing_patch = """    if (hash.startsWith('community-')) {
      specificTargetId = hash;
      hash = 'community';
    } else if (hash.startsWith('job-')) {
      specificTargetId = hash;
      hash = 'jobs';
    } else if (hash.startsWith('startup-')) {
      specificTargetId = hash;
      hash = 'startups';
    } else if (!validNavs.includes(hash)) {
      isPostRoute = true;
      targetPostId = hash;
      hash = 'home';
    }"""
    
new_routing_patch = """    window.communityTargetPostId = null;
    window.jobsTargetPostId = null;
    window.startupTargetPostId = null;

    if (hash.startsWith('community-')) {
      specificTargetId = hash;
      hash = 'community';
      window.communityTargetPostId = specificTargetId.replace('community-', '');
    } else if (hash.startsWith('job-')) {
      specificTargetId = hash;
      hash = 'jobs';
      window.jobsTargetPostId = specificTargetId.replace('job-', '');
    } else if (hash.startsWith('startup-')) {
      specificTargetId = hash;
      hash = 'startups';
      window.startupTargetPostId = specificTargetId.replace('startup-', '');
    } else if (!validNavs.includes(hash) && hash) {
      isPostRoute = true;
      targetPostId = hash;
      hash = 'home';
    }"""

if routing_patch in text:
    text = text.replace(routing_patch, new_routing_patch)
else:
    print("ROUTING PATCH NOT FOUND")

# 2. Prevent automatic scroll-into-view if it's already filtered
scroll_patch = """      if (hash === 'community') {
        iframeCommunity.classList.add('active');
        if (specificTargetId) {
          const commId = specificTargetId.replace('community-', '');
          setTimeout(() => {
            const el = iframeCommunity.querySelector(`[data-id="${commId}"]`);
            if (el) {
              el.scrollIntoView({ behavior: 'smooth', block: 'center' });
              el.style.boxShadow = '0 0 0 3px #8b5cf6';
              setTimeout(() => { el.style.boxShadow = ''; }, 2000);
            }
          }, 350);
        }
      } else if (hash === 'jobs') {
        iframeJobs.classList.add('active');
        if (specificTargetId) {
          const jobId = specificTargetId.replace('job-', '');
          setTimeout(() => {
            if (typeof window.openViewModalById === 'function') {
              window.openViewModalById(jobId);
            }
          }, 400);
        }
      } else if (hash === 'startups') {
        iframeStartups.classList.add('active');
        if (specificTargetId) {
          const startupId = specificTargetId.replace('startup-', '');
          setTimeout(() => {
            const el = document.querySelector(`#adminPosts [data-id="${startupId}"]`);
            if (el) {
              el.scrollIntoView({ behavior: 'smooth', block: 'center' });
              el.style.boxShadow = '0 0 0 3px #8b5cf6';
              setTimeout(() => { el.style.boxShadow = ''; }, 2000);
            }
          }, 400);
        }
      }"""

new_scroll_patch = """      if (hash === 'community') {
        iframeCommunity.classList.add('active');
        if (typeof window.renderDiscussions === 'function') window.renderDiscussions();
      } else if (hash === 'jobs') {
        iframeJobs.classList.add('active');
        if (typeof window.renderJobs === 'function' && window.jobs) window.renderJobs(window.jobs);
      } else if (hash === 'startups') {
        iframeStartups.classList.add('active');
        if (typeof window.applyFilters === 'function') window.applyFilters();
      }"""
      
# Wait, let's keep the scroll logic for alerts, but the target ID is set now. So it's fine.
if scroll_patch in text:
    text = text.replace(scroll_patch, new_scroll_patch)
else:
    print("SCROLL PATCH NOT FOUND")


# 3. Modify renderDiscussions for Community
comm_patch = """        let filtered = discussions.filter(d => {
            const categoryMatch = selectedCategory === "All" || d.category === selectedCategory;
            const searchMatch = d.question.toLowerCase().includes(search);
            return categoryMatch && searchMatch;
        });"""
new_comm_patch = """        let filtered = discussions.filter(d => {
            if (window.communityTargetPostId) return d.id === window.communityTargetPostId;
            const categoryMatch = selectedCategory === "All" || d.category === selectedCategory;
            const searchMatch = d.question.toLowerCase().includes(search);
            return categoryMatch && searchMatch;
        });
        
        if (window.communityTargetPostId) {
            feed.innerHTML = `<div class="mb-3 px-1"><button onclick="window.location.hash='community'" class="text-slate-600 font-semibold text-sm flex items-center gap-2 hover:bg-slate-50 px-3 py-1.5 rounded-full transition-colors"><i class="fas fa-arrow-left"></i> Back to feed</button></div>`;
            if (filtered.length === 0) {
                feed.innerHTML += `<div class="bg-white rounded-xl p-5 text-center text-slate-500">Discussion not found.</div>`;
                return;
            }
        }"""
if comm_patch in text:
    text = text.replace(comm_patch, new_comm_patch)
else:
    print("COMM PATCH NOT FOUND")


# 4. Modify renderJobs for Jobs
jobs_patch = """function renderJobs(jobs){
  document.getElementById('resultCount').textContent = jobs.length;
  if(!jobs.length){
    document.getElementById('job-list').innerHTML = `<div class="empty-state">✨ No matching jobs. Adjust filters.</div>`;
    return;
  }
  const container = document.getElementById('job-list');"""
new_jobs_patch = """function renderJobs(jobs){
  let filteredJobs = jobs;
  if (window.jobsTargetPostId) {
      filteredJobs = jobs.filter(j => j.id === window.jobsTargetPostId);
  }
  document.getElementById('resultCount').textContent = filteredJobs.length;
  const container = document.getElementById('job-list');
  
  if (window.jobsTargetPostId) {
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
"""
if jobs_patch in text:
    text = text.replace(jobs_patch, new_jobs_patch)
else:
    print("JOBS PATCH NOT FOUND")

# 5. Modify applyFilters for Startups
startup_patch = """function applyFilters() {
    const query = searchInput.value.trim().toLowerCase();
    let visible = 0;
    document.querySelectorAll("#adminPosts .post-card").forEach(card => {"""
new_startup_patch = """function applyFilters() {
    const query = searchInput.value.trim().toLowerCase();
    let visible = 0;
    
    // Check if we need to add a back button for Startups
    let backBtn = document.getElementById('startupBackBtn');
    if (!backBtn) {
        backBtn = document.createElement('div');
        backBtn.id = 'startupBackBtn';
        backBtn.innerHTML = `<button onclick="window.location.hash='startups'" class="text-slate-600 dark:text-slate-300 font-semibold text-sm flex items-center gap-2 hover:bg-slate-50 dark:hover:bg-slate-800 px-3 py-1.5 rounded-full transition-colors mb-4"><i class="fas fa-arrow-left"></i> Back to feed</button>`;
        const adminPosts = document.getElementById('adminPosts');
        adminPosts.parentNode.insertBefore(backBtn, adminPosts);
    }
    backBtn.style.display = window.startupTargetPostId ? 'block' : 'none';

    document.querySelectorAll("#adminPosts .post-card").forEach(card => {
      if (window.startupTargetPostId) {
          const show = card.dataset.id === window.startupTargetPostId;
          card.classList.toggle("hidden", !show);
          if (show) visible++;
          return;
      }
"""
if startup_patch in text:
    text = text.replace(startup_patch, new_startup_patch)
else:
    print("STARTUP PATCH NOT FOUND")


# 6. Expose render functions to window if not already exposed
expose_patch = """  function renderDiscussions() {"""
new_expose_patch = """  window.renderDiscussions = renderDiscussions;
  function renderDiscussions() {"""
if expose_patch in text:
    text = text.replace(expose_patch, new_expose_patch)

expose_patch2 = """  function renderJobs(jobs){"""
new_expose_patch2 = """  window.renderJobs = renderJobs;
  function renderJobs(jobs){"""
# I already replaced renderJobs(jobs){ above, so let's do it differently.
# I'll just append it to the end of script.

# And make applyFilters global
expose_patch3 = """  function applyFilters() {"""
new_expose_patch3 = """  window.applyFilters = applyFilters;
  function applyFilters() {"""
if expose_patch3 in text:
    text = text.replace(expose_patch3, new_expose_patch3)
else:
    # it was replaced
    text = text.replace("function applyFilters() {\n    const query", "window.applyFilters = applyFilters;\nfunction applyFilters() {\n    const query")


with open('index.html', 'w') as f:
    f.write(text)
print("PATCH DONE")
