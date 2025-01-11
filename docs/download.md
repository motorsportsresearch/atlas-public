---
layout: page
title: Download
tagline: Latest releases and resources
permalink: /download.html
ref: download
---

{%- assign releases = site.github.releases | where: "draft", false | sort: "tag_name" | reverse -%}

# Releases

{% for release in releases limit:5 %}

## [{{ release.name }}]({{ release.html_url }}) {% if release.prerelease -%}(pre-release){%- endif %}

Released <time datetime="{{ release.published_at | date_to_xmlschema }}">{{ release.published_at | date_to_string }}</time>
{% unless release.tag_name == "v0.0.1" -%}
([compare changes to previous release]({{ site.github.repository_url }}/compare/{{ releases[forloop.index].tag_name }}...{{ release.tag_name }}#files_bucket "Compare changes between release versions {{ releases[forloop.index].tag_name }} and {{ release.tag_name }}"))
{%- endunless %}

{{ release.body }}

## Software
<a href="{{ release.assets[2].browser_download_url }}/" class="btn">Windows (.exe)</a>
<a href="{{ release.assets[1].browser_download_url }}/" class="btn">MacOS (.pkg)</a>
<a href="{{ release.assets[0].browser_download_url }}/" class="btn">Linux (.AppImage)</a>
## Definitions
<a href="{{ release.assets[0].browser_download_url }}/" class="btn">USDM VB WRX</a>

{% endfor %}




