with open('index.html', 'r') as f:
    text = f.read()

# I will replace `    const feedContainer = document.getElementById('feedContainer');`
# with a setTimeout wrapper that closes before `    const nav = document.querySelector('.bottom-nav');`
# Actually, wait, `nav` is used right after. Let's wrap everything after nav update.

old_block = """    const feedContainer = document.getElementById('feedContainer');
    const iframeCommunity = document.getElementById('iframe-community');
    const iframeJobs = document.getElementById('iframe-jobs');
    const iframeStartups = document.getElementById('iframe-startups');
    const postCreator = document.getElementById('postCreationCard');
    const headerContainer = document.querySelector('.header-container');

    // Hide all modules
    feedContainer.style.display = 'none';"""

new_block = """    setTimeout(() => {
    const feedContainer = document.getElementById('feedContainer');
    const iframeCommunity = document.getElementById('iframe-community');
    const iframeJobs = document.getElementById('iframe-jobs');
    const iframeStartups = document.getElementById('iframe-startups');
    const postCreator = document.getElementById('postCreationCard');
    const headerContainer = document.querySelector('.header-container');

    // Hide all modules
    feedContainer.style.display = 'none';"""

text = text.replace(old_block, new_block)

old_end = """        }
      }
    }

    const nav = document.querySelector('.bottom-nav');"""

new_end = """        }
      }
    }
    }, 0);

    const nav = document.querySelector('.bottom-nav');"""

text = text.replace(old_end, new_end)

with open('index.html', 'w') as f:
    f.write(text)
