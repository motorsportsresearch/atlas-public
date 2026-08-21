import os
import json
import markdown
import requests
from datetime import datetime

# Load environment variables
tag_name = os.getenv('RELEASE_TAG')
published_at = os.getenv('RELEASE_DATE')
body = os.getenv('RELEASE_BODY', '')
assets = json.loads(os.getenv('RELEASE_ASSETS', '[]'))

bc_hash = os.getenv('BC_STORE_HASH')
bc_token = os.getenv('BC_ACCESS_TOKEN')
bc_page_id = os.getenv('BC_PAGE_ID')

# Format release date
date_obj = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")
formatted_date = date_obj.strftime("%d %B %Y")

# Generate download links
downloads_html = "Downloads\n\n"
for asset in assets:
    name = asset.get('name', '')
    url = asset.get('browser_download_url', '')
    downloads_html += f"  {name}\n"
downloads_html += "\n"

# Convert the release body to HTML
notes_html = markdown.markdown(body)

# Construct the final HTML layout
final_html = f"""

    Atlas {tag_name}
    Released {formatted_date}
    
    {downloads_html}
    
    {notes_html}
    
    
    Previous Versions
    Looking for older versions and releases? View all releases on GitHub.

"""

# Push to BigCommerce API
api_url = f"https://api.bigcommerce.com/stores/{bc_hash}/v3/content/pages/{bc_page_id}"
headers = {
    "X-Auth-Token": bc_token,
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.put(api_url, json={"html_body": final_html}, headers=headers)
response.raise_for_status()
print(f"Successfully updated BigCommerce page {bc_page_id} with Atlas {tag_name}")
