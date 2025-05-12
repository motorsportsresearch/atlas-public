# Atlas

Atlas is a revolutionary, free ECU calibration suite designed for high-end, professional performance tuning of modern vehicles currently supporting the VA (2015-2021) and VB (2022+) Subaru WRX. With Atlas, North American Motorsports Research is rasing the bar by providing cutting-edge features for the Subaru hobbyist community and protuning communities.

![Atlas 2024.1](https://github.com/atlas-tuning/atlas-public/blob/main/java/screenshots/atlas_new1.png?raw=true "Atlas 2025.2 running on MacOS")

## Links
### [Homepage](https://motorsportsresearch.org)
#### [News](https://motorsportsresearch.org/news)
Latest project updates and news
#### [Support Info](https://motorsportsresearch.org/support)
Detailed vehicle and adapter support information
#### [FAQ](https://motorsportsresearch.org/faq)
Frequenty asked questions and general information
#### [Emissions](https://motorsportsresearch.org/emissions)
Our position on tuning and emissions regulation compliance
#### [Discord](https://motorsportsresearch.org/discord)
Join our Discord community!

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
Atlas is in active development. If you're interested in getting involved in the effort to make ECU reverse engineering and recalibrating modern vehicles free and accessible, consider dropping by the Atlas [Discord server](https://motorsportsresearch.org/discord)!
 
## Emissions
North American Motorsports Research does not and will not condone, support, or facilitate the removal or bypass of any regulated emissions component of a target vehicle. This includes, but is not limited to, components, subsystems and design elements such as:

> - Emissions Related Diagnostic Trouble Codes (DTCs)
> - Exhaust Gas Recirculation (EGR) Systems
> - Tumble Generator Valves (TGVs)
> - Three-way Catalysts (TWCs)
> - Oxygen (O2) Sensors
> - Exhaust Gas Temperature (EGT) Sensors
> - Evaporative Emission System

For more detailed information regarding our position on emissions and tuning, please review our [emissions statement](https://motorsportsresearch.org/emissions).

[![Build Nightly Release](https://github.com/motorsportsresearch/atlas/actions/workflows/nightlybuild.yml/badge.svg?branch=main)](https://github.com/motorsportsresearch/atlas/actions/workflows/nightlybuild.yml)
