# -*- coding: utf-8 -*-

import requests
from .exceptions import ApiError


class DAWA:
    """
    Class for interacting with DAWA - Danmarks Adressers Web API.
    """

    def __init__(self):
        self.base_url = "https://api.dataforsyningen.dk"

    def _request(self, method="GET", endpoint="", headers=None, params=None):
        """
        Sends requests to the remote API.

        Parameters
        ----------
        method : str
            Method for the request ``GET``.
        endpoint : str
            Endpoint for the request.
        headers :
            Dictionary of HTTP Headers to send with the request.
        params :
            Dictionary, list of tuples or bytes to send.

        Returns
        -------
        Response of the request.
        """

        headers = {"Accept": "application/json"}
        if method == "GET":
            return requests.get(
                f"{self.base_url}/{endpoint}", headers=headers, params=params
            )
        return None

    def adgangsadresser(self, **kwargs):
        """
        Constructs a request to the adgangsadresser endpoint.

        Parameters
        ----------
        kwargs :
            Keyword arguments to be used as parameters in the request.
            Look at the API documentation for possibilities.

        Returns
        -------
            A JSON serializable Python object.

        Raises
        ------
        ApiError
            If remote service reports an error.
        """

        try:
            response = self._request("GET", "adgangsadresser", params=kwargs)
            response.raise_for_status()
        except requests.exceptions.RequestException:
            raise ApiError(response.content) from None
        return response.json()
