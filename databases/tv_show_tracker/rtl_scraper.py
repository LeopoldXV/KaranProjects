import datetime

from requests_html import HTMLSession
from bs4 import BeautifulSoup

TODAY = datetime.datetime.now().date()
SOURCE_URL = 'https://www.rtl.hr/tv-raspored/dan/'
SOURCE_URL_RTL = 'https://www.rtl.hr/tv-raspored/kanal/rtl'
# per-day content is divided into morning, noon and evening, per slide (=channel)
MORNING = 'epg_morning-'
NOON = 'epg_noon-'
EVENING = 'epg_evening-'
RTL_SLIDE = 'slide01'  # on site slide01 is the first one - RTL base channel


def scrape_rtl_show_on_date(show_name='Gospodin Savršeni', date=TODAY):
    morning_rtl, noon_rtl, evening_rtl = get_full_day_timetable_rtl(date)
    time_name_tuples = find_show_times_in_timetable(show_name, morning_rtl, noon_rtl, evening_rtl)

    return time_name_tuples


def find_show_times_in_timetable(show_name, morning_rtl, noon_rtl, evening_rtl):
    res = []
    res.extend(find_show_in_segment(show_name, morning_rtl))
    res.extend(find_show_in_segment(show_name, noon_rtl))
    res.extend(find_show_in_segment(show_name, evening_rtl, evening=True))

    return res


def find_show_in_segment(show_name, segment, evening=False):
    res = []
    for content in segment[0].contents:
        time = ''
        name = ''
        for data in content.contents:
            if data.name == 'label':
                time = data.contents[0]
            if data.name == 'h1':
                name = data.contents[0]
        if evening and time and time.split(':')[0][0] == '0':
            # hack to let know that this is next-day time
            time = '-' + time
        if show_name in name:
            res.append((time, name))

    return res


def get_full_day_timetable_rtl(date):
    scrape_url = f'{SOURCE_URL}{date}'
    session = HTMLSession()
    response = session.get(scrape_url)
    response.html.render(timeout=30)
    soup = BeautifulSoup(response.html.html, 'html.parser')

    # content is in 'li' HTML containers
    return (soup.find_all('li', attrs={'id': MORNING + RTL_SLIDE}),
            soup.find_all('li', attrs={'id': NOON + RTL_SLIDE}),
            soup.find_all('li', attrs={'id': EVENING + RTL_SLIDE}))


if __name__ == "__main__":
    scrape_rtl_show_on_date()
