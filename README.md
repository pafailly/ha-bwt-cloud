# BWT Perla - Home Assistant Integration

Custom component for Home Assistant that integrates BWT water softeners (My Perla Optimum) via the [BWT Mon Service](https://www.bwt-monservice.com) cloud API.

## Features

- Cloud polling of device data (no local API available)
- Async HTTP via `aiohttp` (no event loop blocking)
- Credential validation during setup
- Two-tier update intervals: frequent consumption data, less frequent device data
- Automatic session management with re-authentication

### Sensors

| Sensor | Unit | Description |
|--------|------|-------------|
| Water Consumption | L | Daily water consumption (total increasing) |
| Water Increment | L | Water since last update |
| Salt per Regeneration | g | Salt used per regeneration cycle |
| Salt Consumption | g | Total salt consumption (total increasing) |
| Regeneration Count | — | Number of regenerations (total increasing) |
| Softened Water Volume | L | Total softened water volume |
| Inlet Hardness | °f | Water hardness at inlet |
| Outlet Hardness | °f | Water hardness at outlet |
| Pressure | bar | Water network pressure |
| Resin Volume | L | Resin volume |
| WiFi Signal | dBm | Device WiFi signal strength |
| Last Measurement Date | — | Timestamp of last measurement |
| Last Data Refresh | — | Timestamp of last cloud data refresh |

### Binary Sensors

| Sensor | Description |
|--------|-------------|
| Online | Device connectivity status |
| Standby | Holiday/vacation mode |
| Salt Alarm | Low salt warning |
| Power Outage | Power outage detected |

## Installation

1. Copy `custom_components/bwt_perla/` to your Home Assistant `custom_components/` directory
2. Restart Home Assistant
3. Go to **Settings > Devices & Services > Add Integration**
4. Search for **BWT Perla**
5. Enter your bwt-monservice.com credentials and device serial number

## Configuration

| Field | Description | Default |
|-------|-------------|---------|
| Username | BWT Mon Service email | — |
| Password | BWT Mon Service password | — |
| Serial Number | Device serial (e.g. `J7FB-D9CK`) | — |
| Device Name | Display name in HA | BWT My Perla Optimum |
| Main Interval | Device data refresh (seconds) | 3600 |
| Consumption Interval | Consumption data refresh (seconds) | 60 |

Update intervals can be adjusted later via the integration's options flow.

## Credits

Based on [bwthaf](https://github.com/Maypeur/bwthaf) by Maypeur, rewritten with async HTTP, separated API client, and credential validation.
