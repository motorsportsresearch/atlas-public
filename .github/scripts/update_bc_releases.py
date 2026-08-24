import os
import requests
import markdown
from datetime import datetime

bc_hash = os.getenv('BC_STORE_HASH')
bc_token = os.getenv('BC_ACCESS_TOKEN')
bc_page_id = os.getenv('BC_RELEASES_PAGE_ID')
repo = os.getenv('GITHUB_REPOSITORY', 'motorsportsresearch/atlas-public')

# Fetch all releases from GitHub API
gh_response = requests.get(f"https://api.github.com/repos/{repo}/releases")
gh_response.raise_for_status()
releases = gh_response.json()

app_labels = {
    "Atlas_Windows_x64.exe": "Windows (x64)",
    "Atlas_MacOS.dmg": "MacOS",
    "Atlas_MacOS.pkg": "MacOS",
    "Atlas_MacOS_arm64.dmg": "MacOS (arm64)",
    "Atlas_MacOS_x64.dmg": "MacOS (x64)",
    "Atlas_Linux_amd64.AppImage": "Linux (amd64)",
    "Atlas_Linux_arm64.tar.gz": "Linux (arm64)",
    "Atlas_Linux_armv6hf.tar.gz": "Linux (armv6hf)",
    "Atlas_Linux_arm64.AppImage": "Linux (arm64)",
    "Atlas_Linux_armv6hf.AppImage": "Linux (armv6hf)",
    "Atlas_Linux.AppImage": "Linux (amd64)"
}

def_labels = {
    "Definitions-VA_WRX_MT.atlas": "VA WRX MT",
    "Definitions-VB_WRX_MT.atlas": "VB WRX MT",
    "Definitions-USDM_VA_MT.atlas": "USDM VA WRX",
    "Definitions-USDM_VB_MT.atlas": "USDM VB WRX"
}

# Inject the button CSS and Notice
html_output = """
<style>
    .namr-download-container .btn {
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
    }
    .namr-download-container .btn:hover {
        color: rgba(255, 255, 255, 0.8);
        text-decoration: none;
        background-color: rgba(255, 255, 255, 0.2);
        border-color: rgba(255, 255, 255, 0.3);
    }
</style>
<div class="namr-download-container">
    <h2>Notice</h2>
    <p>The software available on this page is provided for archival and troubleshooting purposes only. Users are strongly encouraged to use the latest version of the software whenever possible to ensure optimal performance and security.</p>
    <hr>
"""

for release in releases:
    if release.get('draft'):
        continue

    tag_name = release.get('name', release.get('tag_name'))
    published_at = release.get('published_at')
    prerelease = " (pre-release)" if release.get('prerelease') else ""
    
    date_obj = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")
    formatted_date = date_obj.strftime("%d %B %Y")

    html_output += f"<h2>Atlas {tag_name}{prerelease}</h2>\n"
    html_output += f"<p>Released {formatted_date}</p>\n"

    apps_html = ""
    defs_html = ""

    for asset in release.get('assets', []):
        name = asset.get('name', '')
        url = asset.get('browser_download_url', '')

        if name in app_labels:
            apps_html += f"  <a href='{url}' class='btn'>{app_labels[name]}</a>\n"
        elif name in def_labels:
            defs_html += f"  <a href='{url}' class='btn'>{def_labels[name]}</a>\n"

    if apps_html:
        html_output += "<h3>Downloads</h3>\n<p>\n" + apps_html + "</p>\n"
        
    if defs_html:
        html_output += "<h3>Definitions</h3>\n<p>\n" + defs_html + "</p>\n"

    notes_html = markdown.markdown(
        release.get('body', ''), 
        extensions=['extra', 'nl2br', 'sane_lists']
    )

    html_output += f"<h3>Release Notes</h3>\n{notes_html}\n<hr>\n"

html_output += "</div>"

# Push to BigCommerce
api_url = f"https://api.bigcommerce.com/stores/{bc_hash}/v3/content/pages/{bc_page_id}"
headers = {
    "X-Auth-Token": bc_token,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.put(api_url, json={"name": "Past Releases", "type": "page", "body": html_output}, headers=headers)
response.raise_for_status()
print("Successfully updated the Past Releases page.")
