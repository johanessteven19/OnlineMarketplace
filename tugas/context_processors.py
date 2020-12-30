def datent(request):
    import datetime
    return {
        'date': datetime.datetime.now()
    }