from typing import Dict, Tuple, List
from sqlite3 import Connection

class ParticipantsRepositoty:
  def __init__(self, conn:Connection) -> None:
    self.__conn = conn
  
  def register_participants(self, participants_info:Dict) -> None:
    cursor = self.__conn.cursor()

    cursor.execute(
      '''
        INSERT INTO participants
          (id, trip_id,emails_to_invite_id, name)
        VALUES
          (?,?,?,?)
      ''',(
        participants_info["id"],
        participants_info["trip_id"],
        participants_info["emails_to_invite_id"],
        participants_info["name"],      
      )
    )

    self.__conn.commit()
  
  def find_participants_from_trip(self, trip_id:str) -> List[Tuple]:
    cursor = self.__conn.cursor()
    cursor.execute(
      '''
        SELECT p.id, p.name, p.is_confirmed, e.mail 
        FROM participants as p 
        JOIN emails_to_invite as e ON e.id = p.emails_to_invite_id 
        WHERE trip_id = ?
      ''',(trip_id,)
    )

    links = cursor.fetchall()
    return links
  
  def update_participant_status(self, participant_id:str) -> None:
    cursor = self.__conn.cursor()
    cursor.execute(
      '''
        UPDATE participants
          SET is_confirmed = 1
        WHERE
          id = ?
      ''', (participant_id,)
    )
    self.__conn.commit()