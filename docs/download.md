---
layout: page
title: Download
tagline: Latest releases and resources
permalink: /download.html
ref: download
---

{%- assign releases = site.github.releases | where: "draft", false | sort: "published_at" | reverse -%}

{% for release in releases limit:1 %}

## Atlas {{ release.name }} {% if release.prerelease -%}(pre-release){%- endif %}
Released <time datetime="{{ release.published_at | date_to_xmlschema }}">{{ release.published_at | date_to_string }}</time>
### Downloads
{% for asset in release.assets %} {% if asset.name == "Atlas_Linux.AppImage" %} <a href="{{ asset.browser_download_url }}" class="btn">Linux (.AppImage)</a> {% endif %} {% if asset.name == "Atlas_MacOS.pkg" %} <a href="{{ asset.browser_download_url }}" class="btn">MacOS (.pkg)</a> {% endif %} {% if asset.name == "Atlas_Windows_x64.exe" %} <a href="{{ asset.browser_download_url }}" class="btn">Windows (.exe)</a> {% endif %} {% endfor %}
### Definitions
{% for asset in release.assets %}
{% if asset.name == "Definitions-USDM_VA_MT.atlas" %}
<a href="{{ asset.browser_download_url }}" class="btn">USDM VA WRX</a>
{% endif %}
{% if asset.name == "Definitions-USDM_VB_MT.atlas" %}
<a href="{{ asset.browser_download_url }}" class="btn">USDM VB WRX</a>
{% endif %}
{% endfor %}
### Release Notes
{{ release.body }}

{% endfor %}

## [Previous Versions]({{ '/releases.html' | absolute_url }})
Looking for [older versions and releases?]({{ '/releases.html' | absolute_url }})


