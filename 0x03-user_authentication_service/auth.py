#!/usr/bin/env python3
"""A module for  authentication-related routines.
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes s password.
    """
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
