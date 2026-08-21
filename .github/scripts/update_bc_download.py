import os
import sys
import json
import markdown
import requests
from datetime import datetime

# Load environment variables
tag_name = os.getenv('RELEASE_TAG')
published_at = os.getenv('RELEASE_DATE')
body = os.getenv('RELEASE_BODY', '')
assets_raw = os.getenv('RELEASE_ASSETS')

bc_hash = os.getenv('BC_STORE_HASH')
bc_token = os.getenv('BC_ACCESS_TOKEN')
bc_page_id = os.getenv('BC_PAGE_ID')

# If triggered manually, event data is empty. Fetch latest release from API.
if not tag_name:
    print("Manual trigger detected. Fetching the latest release...")
    repo = os.getenv('GITHUB_REPOSITORY', 'motorsportsresearch/atlas-public')
    
    # Call GitHub REST API for the latest release
    gh_response = requests.get(f"https://api.github.com/repos/{repo}/releases/latest")
    gh_response.raise_for_status()
    release_data = gh_response.json()
    
    tag_name = release_data.get('tag_name')
    published_at = release_data.get('published_at')
    body = release_data.get('body', '')
    assets = release_data.get('assets', [])
else:
    # Triggered by a new release event, parse the assets JSON
    assets = json.loads(assets_raw if assets_raw and assets_raw != 'null' else '[]')

# Format the release date
date_obj = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")
formatted_date = date_obj.strftime("%d %B %Y")


# Generate download links from release artifacts 
downloads_html = "<h3>Downloads</h3>\n<p>\n"
for asset in assets:
    name = asset.get('name', '')
    url = asset.get('browser_download_url', '')
    downloads_html += f"  <a href='{url}' class='btn'>{name}</a>\n"
downloads_html += "</p>\n"

# Convert the release body to HTML
notes_html = markdown.markdown(body)

# Construct the final HTML layout 
final_html = f"""
<style>
    .namr-download-container .btn {{
        display: inline-block;
        margin-bottom: 1rem;
        color: rgba(255, 255, 255, 0.7);
        background-color: rgba(255, 255, 255, 0.08);
        border-color: rgba(255, 255, 255, 0.2);
        border-style: solid;
        border-width: 1px;
        border-radius: 0.3rem;
        transition: color 0.2s, background-color 0.2s, border-color 0.2s;
        padding: 0.75rem 1rem;
        text-decoration: none;
        margin-right: 0.5rem;
    }}
    
    .namr-download-container .btn:hover {{
        color: rgba(255, 255, 255, 0.8);
        text-decoration: none;
        background-color: rgba(255, 255, 255, 0.2);
        border-color: rgba(255, 255, 255, 0.3);
    }}
</style>

<div class="namr-download-container">
    <h2>Atlas {tag_name}</h2>
    <p>Released {formatted_date}</p>
    
    {downloads_html}
    
    {notes_html}
    
    <hr>
    <h3>Previous Versions</h3>
    <p>Looking for older versions and releases? <a href="https://github.com/motorsportsresearch/atlas-public/releases">View all releases on GitHub</a>.</p>
</div>
"""

# Push to BigCommerce API
api_url = f"https://api.bigcommerce.com/stores/{bc_hash}/v3/content/pages/{bc_page_id}"
headers = {
    "X-Auth-Token": bc_token,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.put(api_url, json={"body": final_html}, headers=headers)
response.raise_for_status()
print(f"Successfully updated BigCommerce page {bc_page_id} with Atlas {tag_name}")
