# -*- coding: utf-8 -*-

import unittest
import responses
import dawa_api as dawa


class TestAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.responses = responses.RequestsMock()
        self.responses.start()

        self.client = dawa.Client()

    def tearDown(self) -> None:
        self.addCleanup(self.responses.stop)
        self.addCleanup(self.responses.reset)

    def test_adgangsadresser_mini(self):
        url = f"{self.client.base_url}/adgangsadresser"

        # Empty response (no results from query)
        self.responses.add(method=responses.GET, url=url, body="[]")
        query = dawa.AdresseQuery(vejnavn="Gade", husnr="1")
        resp = self.client.adgangsadresser_mini(adresse_query=query)
        self.assertEqual([], resp)

    def test_adgangsadresser_not_found(self):
        url = f"{self.client.base_url}/adgangsadresser"

        # Empty response (no results from query)
        self.responses.add(method=responses.GET, url=url, body="[]")
        query = dawa.AdresseQuery(vejnavn="Gade", husnr="1")
        resp = self.client.adgangsadresser_mini(query)
        self.assertEqual([], resp)

        # ResourceNotFoundError
        error = r"""{
                    "type": "ResourceNotFoundError",
                    "title": "The resource was not found",
                    "details": {
                        "id": "0254b942-f3ac-4969-a963-d2c4ed9ab943"
                    }
        }"""
        self.responses.add(method=responses.GET, url=url, body=error, status=404)
        with self.assertRaises(dawa.ApiErrorResourceNotFound) as exception_context:
            self.client.adgangsadresser_mini(dawa.AdresseQuery())
        self.assertEqual(exception_context.exception.type_, "ResourceNotFoundError")
        self.assertEqual(
            exception_context.exception.title, "The resource was not found"
        )
        self.assertEqual(
            exception_context.exception.details,
            {"id": "0254b942-f3ac-4969-a963-d2c4ed9ab943"},
        )

    def test_adgangsadresser_query_parameter_format_error(self):
        url = f"{self.client.base_url}/adgangsadresser"

        # Empty response (no results from query)
        self.responses.add(method=responses.GET, url=url, body="[]")
        query = dawa.AdresseQuery(vejnavn="Gade", husnr="1")
        resp = self.client.adgangsadresser_mini(query)
        self.assertEqual([], resp)

        # QueryParameterFormatError
        error = r"""{
                            "type": "QueryParameterFormatError",
                            "title": "One or more query parameters was ill-formed.",
                            "details": [
                                [
                                    "vejpunkt_id",
                                    "String does not match pattern ^([0-9a-fA-F]{8}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{12})$: 2"
                                ]
                            ]
                }"""
        self.responses.add(method=responses.GET, url=url, body=error, status=400)
        with self.assertRaises(dawa.ApiErrorQueryParameterFormat) as exception_context:
            self.client.adgangsadresser_mini(dawa.AdresseQuery())

        self.assertEqual(exception_context.exception.type_, "QueryParameterFormatError")
        self.assertEqual(
            exception_context.exception.title,
            "One or more query parameters was ill-formed.",
        )
        self.assertEqual(
            exception_context.exception.details,
            [
                [
                    "vejpunkt_id",
                    "String does not match pattern ^([0-9a-fA-F]{8}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{4}\\-[0-9a-fA-F]{12})$: 2",
                ]
            ],
        )

    def test_server_error_500(self):
        url = f"{self.client.base_url}/adgangsadresser"
        error = r"""{
                        "type": "InternalServerError",
                        "title": "Something unexpected happened inside the server."
        }"""
        self.responses.add(method=responses.GET, url=url, body=error, status=500)
        with self.assertRaises(dawa.ApiErrorInternalServer) as exception_context:
            self.client.adgangsadresser_mini(dawa.AdresseQuery())

        self.assertEqual(exception_context.exception.type_, "InternalServerError")
        self.assertEqual(
            exception_context.exception.title,
            "Something unexpected happened inside the server.",
        )
        self.assertEqual(
            exception_context.exception.details, f"HTTP Status:500, {error}"
        )

    def test_unknown_error(self):
        url = f"{self.client.base_url}/adgangsadresser"
        error = ""
        self.responses.add(method=responses.GET, url=url, body=error, status=401)
        with self.assertRaises(dawa.ApiErrorUnknown):
            self.client.adgangsadresser_mini(dawa.AdresseQuery())
