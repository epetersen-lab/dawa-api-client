# -*- coding: utf-8 -*-

import requests

from .adgangsadresse import AdgangsadresseFlad, AdgangsadresseMini, AdresseQuery
from .exceptions import (
    ApiErrorConnection,
    ApiErrorInternalServer,
    ApiErrorNotFound,
    ApiErrorQueryParameterFormat,
    ApiErrorResourceNotFound,
    ApiErrorUnknown,
)


class ApiErrorResponse:
    def __init__(self, title: str, type_: str, details: str):
        self.title = title
        self.type_ = type_
        self.details = details

    def __str__(self) -> str:
        return f"Title:{self.title}, Type:{self.type_}, Details:{self.details}"

    def __repr__(self) -> str:
        return f'{self.__class__}(title="{self.title}", type_="{self.type_}", details="{self.details}")'

    @classmethod
    def from_response(cls, response: requests.Response) -> "ApiErrorResponse":
        try:
            response_error = response.json()
        except requests.JSONDecodeError:
            response_error = {}
        title = response_error.get("title", "Error")
        type_ = response_error.get("type", "Unknown")
        details = response_error.get(
            "details", f"HTTP Status:{response.status_code}, {response.text}"
        )
        return cls(title=title, type_=type_, details=details)

    def asdict(self) -> dict:
        return {"title": self.title, "type_": self.type_, "details": self.details}


class Client:
    """
    Class for interacting with DAWA - Danmarks Adressers Web API.
    """

    def __init__(self):
        self.base_url = "https://api.dataforsyningen.dk"

    def _request(self, method: str, path: str, **kwargs) -> requests.Response:
        headers = {"Accept": "application/json"}
        response = None
        try:
            response = requests.request(
                method=method, url=self.base_url + path, headers=headers, **kwargs
            )
            response.raise_for_status()
            return response
        except requests.ConnectionError as error:
            raise ApiErrorConnection(str(error)) from error
        except requests.HTTPError as error:
            api_error = ApiErrorResponse.from_response(response)
            if response.status_code == 404:
                if api_error.type_ == "ResourceNotFoundError":
                    raise ApiErrorResourceNotFound(**api_error.asdict()) from error
                else:
                    raise ApiErrorNotFound(str(error)) from error

            elif api_error.type_ == "QueryParameterFormatError":
                raise ApiErrorQueryParameterFormat(**api_error.asdict()) from error
            elif api_error.type_ == "InternalServerError":
                raise ApiErrorInternalServer(**api_error.asdict()) from error
            else:
                raise ApiErrorUnknown(str(error)) from error

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
        """

        return self._request("GET", "/adgangsadresser", params=params)
