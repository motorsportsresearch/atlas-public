# Atlas

Atlas is a free and open ECU calibration suite designed for performance tuning and reverse-engineering of modern vehicles. This project started as an effort to better understand the behavior of the 2022 WRX ECU but, as there is a lack of free and maintained tooling for software engineers and auto enthusiasts to gain first-party access to their ECUs, has since pivoted towards adopting a much broader feature set that encourages modern ECU research, recalibration and modification across increasingly diverse make and model lineups.

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
