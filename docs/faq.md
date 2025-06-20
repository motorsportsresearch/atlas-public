---
layout: page
title: FAQ
tagline: Frequently Asked Questions
permalink: /faq.html
ref: faq
order: 2
---

### Where can I download Atlas?
* Atlas is in open beta and can be [downloaded]({{ '/download.html' | absolute_url }}) from our website!

### How can I get involved?
* NAMR has a thriving [Discord community](https://discord.gg/{{ site.socials.discord }}). Join the fun today!

### How much does Atlas cost?
* Atlas is free for personal and non-commercial use! {% if site.square.donations == true %} (We do accept [donations](https://square.link/u/{{ site.square.link }}) though.) {% endif %}

### What does Atlas run on?
* Atlas is a Java based, multiplatform application, for Microsoft Windows, Apple Mac OS X and various flavors of Linux including SteamOS, Arch and Debian. 

### Does Atlas support the VA WRX or STI? (2015-2021)
* Yes! Although Atlas originally began as a tool intended to support the VB (2022+) chassis WRX, it’s scope has recently expanded and development is currently in progress for the FA20 powered VA chassis (2015-2021) WRX. More information can be found on our [support page]({{ '/support.html' | absolute_url }}). 

### Is Atlas open source?
* Atlas is free for personal use, but it is not open source. To meet increasingly stringent emissions regulations, we unfortunately had to move from an open-source model to a free, closed-source model.

### What do I need to connect Atlas to my car?
* Atlas fully supports the Tactrix OpenPort 2.0 and STN based adapters such as the OBDLink MX+ with a built-in application driver. With some restrictions, ELM327 based devices also support flashing and datalogging. More information and a detailed list of supported devices can be found on our [support page]({{ '/support.html' | absolute_url }}). 

### Can I use an ELM327 adapter with Atlas?
* ELM327 based devices with firmware version 2.1 or greater are supported in Atlas with a built-in driver. Flashing via this method takes significantly longer than others. (30-60 minutes as opposed to 3-5 minutes via a Tactrix OpenPort 2.0)

### Can I download and modify my OTS or ProTune?
* Atlas does not and will not support any ECU calibration (tune) loaded via a Cobb AccessPort or other third-party accessory. If you want to use Atlas on a vehicle paired to an AccessPort, you’ll need to unpair the AccessPort and revert to your stock calibration in order to begin using Atlas.

### Can I use my existing AccessPort with Atlas?
* Due to the security features implemented on the device, a Cobb AccessPort cannot be used in conjunction with Atlas to flash new calibrations, change maps, view gauges or datalog.

### Can I turn off my check engine light with Atlas?
* Suppression of non-emissions related diagnostic trouble codes is fully supported. Disabling or tampering with emissions related systems (to include DTCs) is explicitly not supported. Please see our [emissions statement]({{ '/emissions.html' | absolute_url }}) for more information.
