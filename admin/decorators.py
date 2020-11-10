from functools import wraps
from flask import redirect, session


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            return redirect('/entrar')
        return f(*args, **kwargs)
    return decorated_function
