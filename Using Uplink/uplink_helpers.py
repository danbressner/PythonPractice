"""Helper method so we don't have to call raise_for_status() everywhere"""

import uplink


@uplink.response_handler
def raise_for_status(response):
    response.raise_for_status()
    return response