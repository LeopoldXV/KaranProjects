from time import sleep

from requests_html import HTMLSession

ATOMIC_CLOCK_URL = 'https://clock.zone/europe/'
UPDATE_FREQUENCY = 10  # in seconds


def scrape_time(clock_url_with_city):
    session = HTMLSession()
    response = session.get(clock_url_with_city)
    response.html.render()  # Execute JavaScript

    clock = response.html.find("div.clock-inner", first=True)
    pure_clock = clock.text.split('In the moment')[0].strip()
    clock_tooltip = clock.text.split('In the moment')[1]

    return pure_clock


def main(city='zagreb'):
    city = city.lower()
    if not city:
        print('Please enter a city name')
        return
    clock_url_with_city = ATOMIC_CLOCK_URL + city
    while True:
        atomic_time = scrape_time(clock_url_with_city)
        print(f'Atomic time is {atomic_time}, refreshing every {UPDATE_FREQUENCY} seconds.')
        sleep(10)


if __name__ == "__main__":
    main(input('Which city do you want atomic clock for? '))
