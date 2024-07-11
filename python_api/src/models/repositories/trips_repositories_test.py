import pytest
import uuid
from datetime import datetime, timedelta

from .trips_repositories import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

print(db_connection_handler)
db_connection_handler.connect()
trip_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com o bando")
def test_create_trip():
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)


  trips_infos ={
    "id": trip_id, 
    "destination": "Bahia",
    "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
    "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=10),
    "owner_name": "Osvaldo",
    "owner_email":"osvaldo@gmail.com"
  }

  trips_repository.crate_trip(trips_infos)

@pytest.mark.skip(reason="interacao com o bando")
def test_find_trip_by_id():
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)
  trip = trips_repository.find_trip_by_id(trip_id)
  print()
  print()
  print(trip)

@pytest.mark.skip(reason="interacao com o bando")
def test_update_trip_status():
  conn = db_connection_handler.get_connection()
  trips_repository = TripsRepository(conn)
  trip = trips_repository.update_trip_status(trip_id)