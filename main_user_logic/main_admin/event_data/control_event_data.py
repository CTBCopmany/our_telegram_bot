from sqlalchemy import create_engine
from config import event_data_url, path
import os


class EventData:
    def __init__(self):
        # connect data
        self.engine = create_engine(event_data_url)

        # create table
        self.engine.execute("""CREATE TABLE IF NOT EXISTS event_data
        (
        id SERIAL PRIMARY KEY,
        text VARCHAR(500),
        img VARCHAR(255)
        )""")

    def add_event(self, text: str, img: str) -> None:
        self.engine.execute("""INSERT INTO event_data(text, img)
                                VALUES('{text}',
                                       '{img}')""".format(text=text,
                                                          img=img))

    def delete_event(self, event_id: int) -> None:
        self.engine.execute("""DELETE FROM event_data 
                               WHERE id = {event_id}""".format(event_id=event_id))

    def get_all_event(self) -> list:
        return self.engine.execute("""SELECT * FROM event_data""").fetchall()
