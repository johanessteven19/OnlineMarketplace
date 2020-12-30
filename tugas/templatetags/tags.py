from django import template
from django.db import connection

from tugas.datalayer import dictfetchall

register = template.Library()


@register.simple_tag(takes_context=True)
def is_authenticated(context):
    request = context['request']
    credentials = request.session.get('credentials')
    if not credentials:
        return False

    cursor = connection.cursor()
    cursor.execute('SELECT password '
                   'FROM EVENT.USER '
                   'WHERE email = %(email)s '
                   'LIMIT 1', {'email': credentials.get('email')})
    result = dictfetchall(cursor)

    if credentials.get('password') != result[0].get('password'):
        return False

    return True

