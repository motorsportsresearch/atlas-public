---
layout: page
title: Download
tagline: Software Downloads
permalink: /download.html
ref: download
---

{%- assign releases = site.github.releases | where: "draft", false | sort: "tag_name" | reverse -%}

## Atlas

Use the following links to download the latest edition of the Atlas software package.

<a href="{{ site.github.winexe_url }}" class="btn">Download for Windows (.exe)</a>
<a href="{{ site.github.macpkg_url }}" class="btn">Download for MacOS (.pkg)</a>
<a href="{{ site.github.linux_url }}" class="btn">Download for Linux (.AppImage)</a>
<a href="{{ site.github.other_url }}" class="btn">Download (Other Platforms)</a>

## Definitions

<a href="{{ site.github.vb_defs_url }}" class="btn">Definitions (USDM VB WRX)</a>

{% for release in releases limit:5 %}

## [{{ release.name }}]({{ release.html_url }}) {% if release.prerelease -%}(pre-release){%- endif %}

Released <time datetime="{{ release.published_at | date_to_xmlschema }}">{{ release.published_at | date_to_string }}</time>
{% unless release.tag_name == "v0.0.1" -%}
([compare changes to previous release]({{ site.github.repository_url }}/compare/{{ releases[forloop.index].tag_name }}...{{ release.tag_name }}#files_bucket "Compare changes between release versions {{ releases[forloop.index].tag_name }} and {{ release.tag_name }}"))
{%- endunless %}

{{ release.body }}

{% endfor %}
