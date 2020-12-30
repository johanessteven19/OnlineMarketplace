from functools import wraps

from django.core.exceptions import ValidationError
from django.core.handlers.wsgi import WSGIRequest
from django.db import connection


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def authenticated(permissions=''):
    """ Decorator factory. Also act as jwt_required left with no params"""

    def variable_injector(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            if not isinstance(permissions, str):
                raise SyntaxError
            else:
                params = permissions

            for request in args:
                if isinstance(request, WSGIRequest):
                    credentials = request.session.get('credentials')

                    cursor = connection.cursor()
                    cursor.execute('SELECT password '
                                   'FROM EVENT.USER '
                                   'WHERE email = %(email)s '
                                   'LIMIT 1', {'email': credentials.get('email')})
                    result = dictfetchall(cursor)

                    if credentials.get('password') != result[0].get('password'):
                        raise ValidationError("Password doesn't match")

                    if params.lower() == 'organizer':
                        cursor.execute('SELECT * '
                                       'FROM EVENT.organizer '
                                       'WHERE email = %(email)s '
                                       'LIMIT 1', {'email': credentials.get('email')})

                        result = dictfetchall(cursor)
                        if result[0]:
                            return func(*args, **kwargs)
                        else:
                            raise ValidationError('USER IS FORBIDDEN')
                    elif not params:
                        return func(*args, **kwargs)

                    raise ValidationError('USER IS FORBIDDEN')
            raise SyntaxError
        return decorator
    return variable_injector
