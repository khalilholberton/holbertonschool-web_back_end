#!/usr/bin/env python3
"""
This module manage the API authentication
"""
from typing import List, TypeVar
from flask import request


class Auth():
    """
    class to manage the API authentication.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ def require_auth
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path.endswith("/"):
            pass
        else:
            path = path + "/"
        if excluded_paths[-1] != "/":
            excluded_paths += "/"
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ def authorization_header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ def current_user
        """
        return None
