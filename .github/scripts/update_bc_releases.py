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

# Inject the button CSS
html_output = """


"""

for release in releases:
    if release.get('draft'):
        continue

    tag_name = release.get('name', release.get('tag_name'))
    published_at = release.get('published_at')
    prerelease = " (pre-release)" if release.get('prerelease') else ""
    
    date_obj = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")
    formatted_date = date_obj.strftime("%d %B %Y")

    html_output += f"Atlas {tag_name}{prerelease}\n"
    html_output += f"Released {formatted_date}\n"

    apps_html = ""
    defs_html = ""

    for asset in release.get('assets', []):
        name = asset.get('name', '')
        url = asset.get('browser_download_url', '')

        if name in app_labels:
            apps_html += f"  {app_labels[name]}\n"
        elif name in def_labels:
            defs_html += f"  {def_labels[name]}\n"

    if apps_html:
        html_output += "Downloads\n\n" + apps_html + "\n"
        
    if defs_html:
        html_output += "Definitions\n\n" + defs_html + "\n"

    notes_html = markdown.markdown(release.get('body', ''))
    html_output += f"Release Notes\n{notes_html}\n\n"

html_output += """
Notice
The software available on this page is provided for archival and troubleshooting purposes only. Users are strongly encouraged to use the latest version of the software whenever possible to ensure optimal performance and security.

"""

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
