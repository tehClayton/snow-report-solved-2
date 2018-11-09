from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime

Base = declarative_base()

class SkiResort(Base):
	__tablename__='ski_resorts'
	id=Column(Integer, primary_key=True)
	resort_name=Column(String(255))
	open_status=Column(Boolean)
	inches_24_hr=Column(Integer)
	inches_72_hr=Column(Integer)
	open_lifts_pct=Column(Float)
	open_trail_pct=Column(Float)
	scrape_ts=Column(DateTime)
