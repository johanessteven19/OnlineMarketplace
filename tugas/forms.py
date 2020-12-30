from django import forms

##Create your forms here
from django.core.exceptions import ValidationError
from django.db import connection

from tugas.datalayer import dictfetchall

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)

    def clean(self):
        data = self.cleaned_data

        email = data.get("email")
        password = data.get("password")
        cursor = connection.cursor()
        cursor.execute('SELECT password '
                       'FROM EVENT.USER '
                       'WHERE email = %(email)s '
                       'LIMIT 1', {'email': email})
        result = dictfetchall(cursor)

        if password != result[0].get('password'):
            raise ValidationError("Password doesn't match")

        return data

