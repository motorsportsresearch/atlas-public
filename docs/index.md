---
layout: home
title: North American Motorsports Research
ref: home
carousels:
  - images: 
    - image: /assets/atlas_new1.png
    - image: /assets/atlas_new2.png
    - image: /assets/atlas_new3.png
    - image: /assets/atlas_new4.png
    - image: /assets/atlas_new5.png
    - image: /assets/atlas_new6.png
    - image: /assets/atlas_new7.png
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
* Supports multiple platforms, including Windows, Mac OS X (including M-series), and Linux (including SteamOS and Raspbian), leveraging Java and open-source libraries
* Enables tuners to create new logic for the ECU with the Atlas custom feature designer, a visual logic node graph that instantly compiles new custom logic for your tune

### Versatile Connectivity:
* Supports the Tactrix OpenPort 2.0, OBDLink wireless and wired adapters as well as various ELM327 adapters via direct serial/COM connection with a natively-written driver in Atlas
* Protects your ECU with custom brick protection that far exceeds OEM recovery capabilities, making your tunes more dependable
* Provides ultra-quick flashing with an entirely custom flash routine, sporting compression and advanced map delta checking

### Advanced Visualization and Editing:
* Enables comfortable night-time tuning with a carefully crafted dark mode interface
* Provides modern, battery-efficient 2D and 3D visualizations for gauges, tables, and function charts
* Offers a 2-3 dimension table editor with sophisticated, re-imagined interactions for fast and efficient map editing
* Features a carefully tailored plotting and visualization system to quickly interpret valuable datalogs

### Comprehensive Documentation and Diagnostics:
* Allows customization of memory parameters to notate ECU RAM offsets corresponding to specific metrics (e.g., RPM, Requested Torque, etc.)
* Provides a simple node graph to create and browse documentation of ECU behavior
* Includes gauges and a data logger for calibration diagnostics and troubleshooting, with project configuration and CSV export capabilities

### Streamlined Project Management:
* Offers a composite project system that consolidates all calibrations and ECU configurations in a single file
* Enables a consistent experience across model years and variants with an intelligent calibration cross-application function
* Supports our hobbyist community by enabling rapid import and export of Atlas custom features and tables ("Atlas Mods")

### Engineered with Love:
* Atlas is developed by a team of tuners, enthusiasts, and motorsports hobbyists like you that put our community first.

## Get Involved
Come see what the Subaru WRX community, professional and hobbyist alike, has been raving over!

Atlas is in active development. If you're interested in getting involved in the effort to make ECU reverse engineering and recalibrating modern vehicles free and accessible, consider dropping by the Atlas [Discord server](https://discord.gg/{{ site.socials.discord }}){% if site.paypal.donations == true %} or donating today{% endif %}!

{% if site.paypal.donations == true %}
## Donate
  {% include donate.html %}
{% endif %}
