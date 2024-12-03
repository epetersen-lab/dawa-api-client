# -*- coding: utf-8 -*-

import json


class ApiError(Exception):
    """
    An exception occurred while handling the request.
    """

    def __init__(self, api_problem=None):
        """Initialize ApiError with information given from the remote API."""
        problem = json.loads(api_problem)
        self.type = problem.get("type")
        self.title = problem.get("title")
        self.details = problem.get("details")
