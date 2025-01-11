---
layout: page
title: Download
tagline: Latest releases and resources
permalink: /download.html
ref: download
---

{%- assign releases = site.github.releases | where: "draft", false | sort: "tag_name" | reverse -%}

{% for release in releases limit:5 %}

# [Atlas {{ release.name }}]({{ release.html_url }}) {% if release.prerelease -%}(pre-release){%- endif %}
Released <time datetime="{{ release.published_at | date_to_xmlschema }}">{{ release.published_at | date_to_string }}</time>

{{ release.body }}
## Downloads
<a href="{{ release.assets[2].browser_download_url }}/" class="btn">Windows (.exe)</a>
<a href="{{ release.assets[1].browser_download_url }}/" class="btn">MacOS (.pkg)</a>
<a href="{{ release.assets[0].browser_download_url }}/" class="btn">Linux (.AppImage)</a>
## Definitions
<a href="{{ release.assets[0].browser_download_url }}/" class="btn">USDM VB WRX</a>

{% endfor %}

Looking for [older versions and releases?]({{ '/releases.html' | absolute_url }})


