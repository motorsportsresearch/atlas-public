---
layout: page
title: FAQ
tagline: Frequently Asked Questions
permalink: /faq.html
ref: faq
order: 2
---

### Where can I download Atlas?
* Atlas can be [downloaded]({{ '/download.html' | absolute_url }}) from our website!

### Is Atlas Beta? How safe is it to use?
* Atlas is **fully released** and is no longer in beta with hundreds or even thousands of successful reflashes completed across supported vehicles.
* Atlas sports a unique brick protection feature that helps to protect your ECU against the need to be removed from your vehicle for repair. During your first flash, and before your tune itself is sent to the vehicle, brick protection is automatically installed to your ECU.

### I'm a professional tuner ("Protuner"), can I use Atlas?
* Yes, but keep in mind Atlas is free for **personal, non-commercial** use. You can use Atlas to tune your own vehicle, but for a commercial license and tune locking/intellectual property protection, please contact us.

### I'm an individual and I want to tune my car, can I use Atlas?
* Atlas is available to our community for personal, non-commercial use. We want you to enjoy tuning your own car or help a friend tune theirs. {% if site.square.donations == true %} We do accept [donations](https://square.link/u/{{ site.square.link }}) though. {% endif %}

### How can I get involved?
* NAMR has a thriving [Discord community](https://discord.gg/{{ site.socials.discord }}). Join the fun today!

### Who makes Atlas? What is the motivation?
* North American Motorsports Research (NAMR) designs and develops the Atlas software. We are comprised of a group of enthusiast VA and VB WRX owners.
* Atlas is made out of a passion for all things Subaru and a desire to push the knowlege and capabilities of the Subaru direct injection platforms forward in a more community-oriented way.

### What does Atlas run on?
* Atlas is a Java based, multiplatform application, for Microsoft Windows, Apple Mac OS X and various flavors of Linux including SteamOS, Arch and Debian. 

### Does Atlas support the VA WRX or STI? (2015-2021)
* Yes! Although Atlas originally began as a tool intended to support the VB (2022+) chassis WRX, it’s scope has recently expanded and development is currently in progress for the FA20 powered VA chassis (2015-2021) WRX. More information can be found on our [support page]({{ '/support.html' | absolute_url }}). 

### Is Atlas open source?
* Atlas is free for personal use, but it is not open source. To meet increasingly stringent emissions regulations, we unfortunately had to move from an open-source model to a free, closed-source model.

### What do I need to connect Atlas to my car?
* Atlas fully supports the Tactrix OpenPort 2.0 and STN based adapters such as the OBDLink EX with a built-in driver. With some restrictions, ELM327 based devices support datalogging. More information and a detailed list of supported devices can be found on our [support page]({{ '/support.html' | absolute_url }}). 

### Can I download, modify, or log my third-party tune?
* Atlas does not and will not support any ECU calibration (tune) loaded via a COBB AccessPort or other third-party accessory.
* Proprietary devices such as the COBB AccessPort cannot be used with Atlas to flash new calibrations, change maps, view gauges, or datalog.
* If you want to use Atlas on a vehicle married to an AccessPort, you’ll need to unmarry the AccessPort and revert to your stock calibration in order to begin using Atlas.

### Can I turn off my check engine light with Atlas?
* Suppression of non-emissions related diagnostic trouble codes is fully supported. Disabling or tampering with emissions related systems (to include DTCs) is explicitly not supported. Please see our [emissions statement]({{ '/emissions.html' | absolute_url }}) for more information.
