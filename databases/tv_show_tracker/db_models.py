from sqlalchemy import Column, Integer, String, Text, ForeignKey, UniqueConstraint, TIMESTAMP
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Show(Base):
    __tablename__ = "shows"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    genre = Column(String(100), nullable=True)
    duration = Column(Integer, nullable=True)

    __table_args__ = (UniqueConstraint("title", "duration", name="shows_title_duration_key"),)

    schedules = relationship("Schedule", back_populates="show")


# Define the Channels model
class Channel(Base):
    __tablename__ = "channels"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    network = Column(String(255), nullable=True)
    country = Column(String(100), nullable=True)

    schedules = relationship("Schedule", back_populates="channel")


# Define the Schedule model
class Schedule(Base):
    __tablename__ = "schedule"
    id = Column(Integer, primary_key=True, index=True)
    channel_id = Column(Integer, ForeignKey("channels.id", ondelete="CASCADE"), nullable=True)
    show_id = Column(Integer, ForeignKey("shows.id", ondelete="CASCADE"), nullable=True)
    start_time = Column(TIMESTAMP, nullable=False)
    end_time = Column(TIMESTAMP, nullable=True)
    episode_title = Column(String(255), nullable=True)
    season = Column(Integer, nullable=True)
    episode = Column(Integer, nullable=True)

    __table_args__ = (UniqueConstraint("channel_id", "start_time", name="schedule_channel_id_start_time_key"),)

    show = relationship("Show", back_populates="schedules")
    channel = relationship("Channel", back_populates="schedules")
