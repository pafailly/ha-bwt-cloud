"""Constants for BWT Perla integration."""
from datetime import timedelta

DOMAIN = "bwt_perla"
MANUFACTURER = "BWT"

# Configuration
CONF_SERIAL_NUMBER = "serial_number"
CONF_DEVICE_NAME = "device_name"
CONF_INTERVAL_MAIN = "interval_main"
CONF_INTERVAL_CONSUMPTION = "interval_consumption"

# Defaults
DEFAULT_DEVICE_NAME = "BWT My Perla Optimum"
DEFAULT_INTERVAL_MAIN = 3600  # 1 hour
DEFAULT_INTERVAL_CONSUMPTION = 60  # 1 minute

# Update intervals
UPDATE_INTERVAL_MAIN = timedelta(seconds=3600)
UPDATE_INTERVAL_CONSUMPTION = timedelta(seconds=300)

# API URLs
BWT_BASE_URL = "https://www.bwt-monservice.com"
BWT_LOGIN_URL = f"{BWT_BASE_URL}/login"
BWT_DASHBOARD_URL = f"{BWT_BASE_URL}/dashboard"
BWT_DEVICE_URL = f"{BWT_BASE_URL}/device"
BWT_SUMMARY_URL = f"{BWT_BASE_URL}/ajax/product-summary"
BWT_LOAD_CONSO_URL = f"{BWT_BASE_URL}/_components/DeviceTabs/loadConso"

# Sensor types
SENSOR_TYPES = {
    "salt": {
        "name": "Salt per Regeneration",
        "unit": "g",
        "icon": "mdi:shaker",
        "device_class": "weight",
        "state_class": "measurement",
    },
    "resin_vol": {
        "name": "Resin Volume",
        "unit": "L",
        "icon": "mdi:water",
        "device_class": None,
        "state_class": "measurement",
    },
    "in_hardness": {
        "name": "Inlet Hardness",
        "unit": "°f",
        "icon": "mdi:water-opacity",
        "device_class": None,
        "state_class": "measurement",
    },
    "out_hardness": {
        "name": "Outlet Hardness",
        "unit": "°f",
        "icon": "mdi:water-check",
        "device_class": None,
        "state_class": "measurement",
    },
    "pressure": {
        "name": "Pressure",
        "unit": "bar",
        "icon": "mdi:gauge",
        "device_class": "pressure",
        "state_class": "measurement",
    },
    "wifi_signal": {
        "name": "WiFi Signal",
        "unit": "dBm",
        "icon": "mdi:wifi",
        "device_class": "signal_strength",
        "state_class": "measurement",
    },
    "vol_ok": {
        "name": "Softened Water Volume",
        "unit": "L",
        "icon": "mdi:water-check",
        "device_class": "water",
        "state_class": "total",
    },
    "water_consumption": {
        "name": "Water Consumption",
        "unit": "L",
        "icon": "mdi:water",
        "device_class": "water",
        "state_class": "total_increasing",
    },
    "water_increment": {
        "name": "Water Increment",
        "unit": "L",
        "icon": "mdi:water-plus",
        "device_class": None,
        "state_class": "measurement",
    },
    "regen_count": {
        "name": "Regenerations",
        "unit": "",
        "icon": "mdi:refresh",
        "device_class": None,
        "state_class": "total_increasing",
    },
    "salt_consumption": {
        "name": "Salt Consumption",
        "unit": "g",
        "icon": "mdi:shaker-outline",
        "device_class": "weight",
        "state_class": "total_increasing",
    },
    "last_update": {
        "name": "Last Measurement Date",
        "unit": None,
        "icon": "mdi:calendar-clock",
        "device_class": "timestamp",
        "state_class": None,
    },
    "refresh_date": {
        "name": "Last Data Refresh",
        "unit": None,
        "icon": "mdi:update",
        "device_class": "timestamp",
        "state_class": None,
    },
}

BINARY_SENSOR_TYPES = {
    "online": {
        "name": "Online",
        "device_class": "connectivity",
        "icon": "mdi:lan-connect",
    },
    "standby": {
        "name": "Holiday Mode",
        "device_class": "running",
        "icon": "mdi:power-sleep",
    },
    "salt_alarm": {
        "name": "Salt Alarm",
        "device_class": "problem",
        "icon": "mdi:alert",
    },
    "power_outage": {
        "name": "Power Outage",
        "device_class": "problem",
        "icon": "mdi:power-plug-off",
    },
}
