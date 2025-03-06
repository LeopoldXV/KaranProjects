from datetime import timedelta, datetime
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.dialects.postgresql import insert

from databases.tv_show_tracker.db_models import Show, Channel, Schedule

DB_NAME = 'tv_shows'
DB_USER = 'supcom'
DB_PASSWORD = ''
DB_HOST = 'localhost'
DB_PORT = '5432'


def store_in_db(data, date, channel):
    # we need date because data tuples only have times
    # convert tuples to (datetime, show name)
    engine = get_engine()
    connection = engine.connect()

    for time, name in data:
        # N.B.: treat data with minus prefix as next day date (hack from scraper)
        actual_date = date + timedelta(days=1) if '-' in time else date
        time_obj = datetime.strptime(time.strip('-'), "%H:%M").time()
        datetime_obj = datetime.combine(actual_date, time_obj)
        # TODO: make a DB (model?) object out of datetime_obj, name and channel and store (it/them since it's FK?)
        statement = insert(Show).values(title=name, description='2 lika i 20 likuša', genre='drama',
                                        duration=80).on_conflict_do_nothing(index_elements=["title", "duration"])
        connection.execute(statement)
        connection.commit()

        statement = insert(Channel).values(name=channel, network=channel, country='Croatia').on_conflict_do_nothing(
            index_elements=["name"])
        connection.execute(statement)
        connection.commit()

        channel_id = get_channel_id(channel, connection)
        show_id = get_show_id(name, connection)

        statement = (insert(Schedule).values(channel_id=channel_id,
                                            show_id=show_id,
                                            start_time=datetime_obj,
                                            end_time=datetime_obj,
                                            episode_title='',
                                            season=-1,
                                            episode=-1)
                     .on_conflict_do_nothing(index_elements=["channel_id", "start_time"]))
        connection.execute(statement)

    connection.commit()


def get_channel_id(channel, connection):
    query = select(Channel).where(Channel.name == channel)
    return connection.execute(query).fetchone()[0]


def get_show_id(name, connection):
    query = select(Show).where(Show.title == name)
    return connection.execute(query).fetchone()[0]


def get_engine():
    return create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')


def filter_upcoming(show_name, time_delta):
    pass


if __name__ == "__main__":
    pass
