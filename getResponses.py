# Required modules
import math
import os
import random
import re
import sys


def is_valid_csrf(csrf_token):
    return len(csrf_token) >= 8 and csrf_token.isalnum()

def get_responses(valid_auth_tokens, requests):
    valid_tokens_set = set(valid_auth_tokens)
    responses = []

    for request_type, url in requests:
        parts = url.split('?')[1].split('&')  # Split URL to get parameters
        params = {k: v for k, v in (part.split('=') for part in parts)}

        # Validate authentication token
        if 'token' not in params or params['token'] not in valid_tokens_set:
            responses.append("INVALID")
            continue

        # For POST requests, validate CSRF token
        if request_type == "POST":
            if 'csrf_token' not in params or not is_valid_csrf(params['csrf_token']):
                responses.append("INVALID")
                continue

        # Exclude token and csrf_token from parameters to be returned
        params.pop('token', None)
        params.pop('csrf_token', None)
        responses.append("VALID," + ','.join([f"{k}={v}" for k, v in params.items()]))

    return responses
