import datetime
from datetime import timedelta

from databases.tv_show_tracker.rtl_scraper import scrape_rtl_show_on_date
from database_layer import store_in_db, filter_upcoming
from notifier import send_email


def main():
    date = datetime.datetime.today().date()
    show_name = 'Gospodin Savršeni'
    # maybe in future when we have multiple channel scrapers, but also for DB
    channel = 'RTL'
    data = scrape_rtl_show_on_date(show_name, date)
    upcoming_delta = timedelta(minutes=30)
    if data:
        store_in_db(data, date, channel)
        upcoming = filter_upcoming(show_name, upcoming_delta)
        if upcoming:
            send_email(upcoming)


if __name__ == "__main__":
    main()
