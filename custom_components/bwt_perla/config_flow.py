"""Config flow for BWT Perla integration."""
import logging

import aiohttp
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_USERNAME, CONF_PASSWORD
from homeassistant.core import callback

from .api import BwtCloudApi, BwtAuthError, BwtConnectionError, BwtApiError
from .const import (
    DOMAIN,
    CONF_SERIAL_NUMBER,
    CONF_DEVICE_NAME,
    CONF_INTERVAL_MAIN,
    CONF_INTERVAL_CONSUMPTION,
    DEFAULT_DEVICE_NAME,
    DEFAULT_INTERVAL_MAIN,
    DEFAULT_INTERVAL_CONSUMPTION,
)

_LOGGER = logging.getLogger(__name__)


class BWTConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for BWT Perla."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        errors = {}

        if user_input is not None:
            if not user_input.get(CONF_USERNAME):
                errors[CONF_USERNAME] = "required"
            if not user_input.get(CONF_PASSWORD):
                errors[CONF_PASSWORD] = "required"
            if not user_input.get(CONF_SERIAL_NUMBER):
                errors[CONF_SERIAL_NUMBER] = "required"

            if not errors:
                # Validate credentials by attempting authentication
                try:
                    session = aiohttp.ClientSession(
                        cookie_jar=aiohttp.CookieJar(unsafe=True)
                    )
                    try:
                        api = BwtCloudApi(
                            session=session,
                            username=user_input[CONF_USERNAME],
                            password=user_input[CONF_PASSWORD],
                            serial_number=user_input[CONF_SERIAL_NUMBER],
                        )
                        await api.authenticate()
                    finally:
                        await session.close()
                except BwtAuthError:
                    errors["base"] = "invalid_auth"
                except BwtConnectionError:
                    errors["base"] = "cannot_connect"
                except BwtApiError:
                    errors["base"] = "unknown"
                except Exception:
                    _LOGGER.exception("Unexpected error during config validation")
                    errors["base"] = "unknown"

            if not errors:
                await self.async_set_unique_id(user_input[CONF_SERIAL_NUMBER])
                self._abort_if_unique_id_configured()

                return self.async_create_entry(
                    title=user_input.get(
                        CONF_DEVICE_NAME, user_input[CONF_SERIAL_NUMBER]
                    ),
                    data=user_input,
                )

        data_schema = vol.Schema(
            {
                vol.Required(CONF_USERNAME): str,
                vol.Required(CONF_PASSWORD): str,
                vol.Required(CONF_SERIAL_NUMBER): str,
                vol.Optional(CONF_DEVICE_NAME, default=DEFAULT_DEVICE_NAME): str,
                vol.Optional(
                    CONF_INTERVAL_MAIN, default=DEFAULT_INTERVAL_MAIN
                ): vol.All(vol.Coerce(int), vol.Range(min=300, max=86400)),
                vol.Optional(
                    CONF_INTERVAL_CONSUMPTION, default=DEFAULT_INTERVAL_CONSUMPTION
                ): vol.All(vol.Coerce(int), vol.Range(min=60, max=3600)),
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return BWTOptionsFlow(config_entry)


class BWTOptionsFlow(config_entries.OptionsFlow):
    """Handle options flow for BWT Perla."""

    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Optional(
                        CONF_INTERVAL_MAIN,
                        default=self.config_entry.options.get(
                            CONF_INTERVAL_MAIN,
                            self.config_entry.data.get(
                                CONF_INTERVAL_MAIN, DEFAULT_INTERVAL_MAIN
                            ),
                        ),
                    ): vol.All(vol.Coerce(int), vol.Range(min=60, max=86400)),
                    vol.Optional(
                        CONF_INTERVAL_CONSUMPTION,
                        default=self.config_entry.options.get(
                            CONF_INTERVAL_CONSUMPTION,
                            self.config_entry.data.get(
                                CONF_INTERVAL_CONSUMPTION,
                                DEFAULT_INTERVAL_CONSUMPTION,
                            ),
                        ),
                    ): vol.All(vol.Coerce(int), vol.Range(min=30, max=3600)),
                }
            ),
        )
