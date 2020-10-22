from datetime import datetime, timedelta


def get_date(request):
    date = datetime.today() + timedelta(hours=2)
    return {'date': date}
