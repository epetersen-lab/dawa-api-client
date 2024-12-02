# -*- coding: utf-8 -*-

import requests

from .adgangsadresse import AdgangsadresseFlad, AdgangsadresseMini, AdresseQuery
from .exceptions import ApiError


class DAWA:
    """
    Class for interacting with DAWA - Danmarks Adressers Web API.
    """

    def __init__(self):
        self.base_url = "https://api.dataforsyningen.dk"

    def adgangsadresser_mini(
        self, adresse_query: AdresseQuery
    ) -> list[AdgangsadresseMini]:
        """
        Contructs a request to the adgangsadresser endpoint with parameters defined in the Query object.
        The 'struktur' parameter is set to 'mini'.

        Parameters
        ----------
        query : AdresseQuery object

        Returns:
        --------
            AdgangsadresseMini object
        """

        adresse_query.struktur = "mini"
        response = self.adgangsadresser(adresse_query.as_params())
        return AdgangsadresseMini.schema().load(response.json(), many=True)

    def adgangsadresser_flad(
        self, adresse_query: AdresseQuery
    ) -> list[AdgangsadresseFlad]:
        """
        Contructs a request to the adgangsadresser endpoint with parameters defined in the Query object.
        The 'struktur' parameter is set to 'flad'.

        Parameters
        ----------
        query : AdresseQuery object

        Returns:
        --------
            AdgangsadresseFlad object
        """

        adresse_query.struktur = "flad"
        response = self.adgangsadresser(adresse_query.as_params())
        return AdgangsadresseFlad.schema().load(response.json(), many=True)

    def adgangsadresser(self, params) -> requests.Response:
        """
        Constructs a request to the adgangsadresser endpoint.

        Parameters
        ----------
        params :
            Dictionary, list of tuples, bytes, or file-like object to send in the body of the Request.
            See DAWA API documentation for possibil parameters.

        Returns
        -------
            A requests.Response object.

        Raises
        ------
        ApiError
            If remote service reports an error.
        """

        try:
            headers = {"Accept": "application/json"}
            response = requests.get(
                f"{self.base_url}/adgangsadresser", headers=headers, params=params
            )
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            raise ApiError(response.content) from e
