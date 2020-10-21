from flask import jsonify


def generic_error_message(error_code, error_message):
    payload = jsonify(dict(message=error_message, success=False))
    return payload, error_code
