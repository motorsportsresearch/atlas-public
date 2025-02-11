---
layout: home
title: North American Motorsports Research
ref: home
carousels:
  - images: 
    - image: /assets/atlas.png
    - image: /assets/atlas2.png
    - image: /assets/atlas3.png
    - image: /assets/atlas4.png
    - image: /assets/atlas5.png
    - image: /assets/atlas6.png
    - image: /assets/atlas7.png
---

## Atlas Open Tuning Platform
Atlas is a free and open ECU calibration suite designed for performance tuning modern vehicles. This project started as an effort to better understand the behavior of the 2022 WRX ECU but, as there is a lack of free and maintained tooling for software engineers and auto enthusiasts to gain first-party access to their ECUs, has since pivoted towards adopting a much broader feature set that encourages modern ECU research, recalibration and modification across increasingly diverse make and model lineups.

{% include carousel.html height="50" unit="%" duration="7" number="1" %}

## Latest Project Update

<ul class="post-list">
    {% for post in site.posts limit:1 %}
      <li>
        {% assign date_format = site.cayman-blog.date_format | default: "%b %-d, %Y" %}
        <span class="post-meta">{{ post.date | date: date_format }}</span>
        <h2>
          <a class="post-link" href="{{ post.url | absolute_url }}" title="{{ post.title }}">{{ post.title | escape }}</a>
        </h2>
        {{ post.excerpt | strip_html | truncatewords: 30 }}
      </li>
    {% endfor %}
</ul>

## Features
### Comprehensive Tuning Suite:
* Enables in-depth ECU research and to full recalibration capabilities through an automatic ROM analysis and table match function
* Supports multiple platforms, including Windows, Mac OS X (including M-series), and Linux (including SteamOS and Raspbian), leveraging Java and open-source libraries
* Integrates the Ghidra SRE Framework bundle to analyze tables and emulate ROM machine code

### Versatile Connectivity:
* Supports the Tactrix OpenPort 2.0, OBDLink wireless and wired adapters as well as various ELM327 adapters via direct serial/COM connection with a natively-written driver in Atlas

### Advanced Visualization and Editing:
* Provides 2D and 3D OpenGL visualizations for gauges, tables, and function charts
* Offers a 1-2 dimension table editor with common arithmetic functions for efficient calibration editing
* Includes a live table definition interface to manage project tables and expedite table definition
* Features a value scaling configuration UI to rapidly create new scaling operations as they are identified within ECU logic

### Comprehensive Documentation and Diagnostics:
* Allows customization of memory parameters to notate ECU RAM offsets corresponding to specific metrics (e.g., RPM, Requested Torque, etc.)
* Provides a simple node graph to create and browse documentation of ECU behavior
* Includes gauges and a data logger for calibration diagnostics and troubleshooting, with project configuration and CSV export capabilities

### Streamlined Project Management:
* Offers a composite project system that consolidates all calibrations and ECU configurations in a single file
* Features an intelligent table-matching system to automatically detect new tables and discover existing tables in unknown variants
* Enables a consistent experience across model years and variants with an intelligent calibration cross-application function

## Get Involved
Atlas is in active development. If you're interested in getting involved in the effort to make ECU reverse engineering and recalibrating modern vehicles free and accessible, consider dropping by the Atlas [Discord server](https://discord.gg/{{ site.socials.discord }}){% if site.paypal.donations == true %} or donating today{% endif %}!

{% if site.paypal.donations == true %}
## Donate
  {% include donate.html %}
{% endif %}
