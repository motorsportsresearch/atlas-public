---
layout: page
title: Support
tagline: Detailed adapter and vehicle support information
permalink: /support.html
ref: support
order: 1
---

## Supported Vehicles

If a vehicle is supported, it may not be complete. Please report any missing tables or desired exposed tables to our GitHub project as a new [issue](https://github.com/motorsportsresearch/atlas-public/issues). 

| Make   | Model<br>(Chassis) | Year      | Status |
|--------|--------------------|-----------|--------|
| Subaru | WRX (VB)     | 2024-2025      | ![Supported](https://flat.badgen.net/badge/icon/Supported?label&color=green) |
| Subaru | WRX (VB)     | 2022-2023      | ![Supported](https://flat.badgen.net/badge/icon/Supported?label&color=green) |
| Subaru | WRX (VA)     | 2015-2021 | ![Supported](https://flat.badgen.net/badge/icon/Supported?label&color=green) |
| Subaru | WRX STi (VA) | 2015-2021 | ![In Progress](https://flat.badgen.net/badge/icon/In%20Progress?label&color=blue) |
| Subaru | BRZ (ZD8) | 2021+     | ![In Progress](https://flat.badgen.net/badge/icon/In%20Progress?label&color=blue) |
| Toyota | GR86 (ZN8) | 2021+     | ![In Progress](https://flat.badgen.net/badge/icon/In%20Progress?label&color=blue) |

A more detailed breakdown of supported vehicles by transmission type and domestic market can be found on the [vehicle support documentation page]({{ site.links.atlasdocs }}/page/supported-vehicles).

## Supported Adapters

Atlas supports the following adapters and hardware through custom cross-platform device drivers that are built directly into Atlas. The listed adapters should work out of the box with no additional configuration required.

For the best performance and reliability we reccomend the **Tactrix OpenPort 2.0**.

| Device               | Connection | Datalogging      | Flashing |
|----------------------|------------|------------------|----------|
| [OBDX Pro VX](https://obdxpro.com/product/obdx-pro-vx-obd2-diagnostics-and-tuning/) | Wired/Wireless<br>(Bluetooth 5.0 LE/USB-Micro B) | ![Supported](https://flat.badgen.net/badge/icon/Beta?label&color=yellow)<br>120Hz | ![Supported](https://flat.badgen.net/badge/icon/Beta?label&color=yellow)<br>(Wired: 20-30 seconds<br>Wireless: 60-80 seconds) |
| [Tactrix OpenPort 2.0](https://www.tactrix.com/index.php?page=shop.product_details&flypage=flypage.tpl&product_id=17&category_id=6&option=com_virtuemart&Itemid=53&redirected=1&Itemid=53) | Wired<br>(USB-Mini B) | ![Supported](https://flat.badgen.net/badge/icon/Supported?label&color=green)<br>120Hz | ![Supported](https://flat.badgen.net/badge/icon/Supported?label&color=green)<br>(3-5 Minutes) |
| [OBDLink EX](https://www.obdlink.com/products/obdlink-ex/) | Wired<br>(USB-A) | ![Supported](https://flat.badgen.net/badge/icon/Supported?label&color=green)<br>60Hz | ![Supported](https://flat.badgen.net/badge/icon/Supported?label&color=green)<br>(5-15 Minutes) |
| [OBDLink MX+](https://www.obdlink.com/products/obdlink-mxp/) | Wireless<br>(Bluetooth 3.0) | ![Supported](https://flat.badgen.net/badge/icon/Supported?label&color=green)<br>30Hz | ![Not Recommended](https://flat.badgen.net/badge/icon/Not%20Recommended?label&color=orange) |
| [Veepeak OBDCheck BLE+](https://www.amazon.com/dp/B076XVQMVS) | Wireless<br>(Bluetooth LE) |  ![Supported](https://flat.badgen.net/badge/icon/Supported?label&color=green)<br>20Hz | ![Not Recommended](https://flat.badgen.net/badge/icon/Not%20Recommended?label&color=orange) |

More detailed support information such as operating system compatibility, adapter chipset and connection notes can be found on the [adapter support documentation page]({{ site.links.atlasdocs }}/page/supported-adapters).

NAMR is always interested in expanding support to new adapters and hardware. If you have a device you'd like to see supported and isn't listed here, please check our current [hardware requests](https://github.com/motorsportsresearch/atlas-public/labels/hardware%20request) on GitHub and see if a ticket already exists for the device in question. If one doesn't exist yet, consider opening a new [adapter or hardware request](https://github.com/motorsportsresearch/atlas-public/issues/new?labels=hardware%20request&template=adapter_request.md&title=).

## Issues/Troubleshooting

Atlas is a relatively new software project, and while we strive to provide an easy to use and trouble-free product, errors may still arise. In this event, users are urged to check our currently [known issues](https://github.com/motorsportsresearch/atlas-public/labels/bug). If this is a new issue, please [open a support ticket](https://github.com/motorsportsresearch/atlas-public/issues/new?labels=bug&template=bug_report.md) on our GitHub or drop by the [NAMR Atlas Community on Discord](https://discord.gg/{{ site.socials.discord }}).
