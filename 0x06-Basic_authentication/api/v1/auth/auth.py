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
        return False

    def authorization_header(self, request=None) -> str:
        """ def authorization_header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ def current_user
        """
        return None
