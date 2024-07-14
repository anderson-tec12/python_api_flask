from typing  import Dict
import uuid


from src.models.repositories.emails_to_invite_reporitory import EmailsToInviteRepository
from src.models.repositories.participants_repository import ParticipantsRepositoty


class ParticipantsCreator:
  def __init__(self, participants_repository:ParticipantsRepositoty, emails_repository:EmailsToInviteRepository) -> None:
    self.__participants_repository = participants_repository
    self.__emails_repository = emails_repository
  
  def create(self, body, trip_id) -> Dict:
    try:
      participant_id = str(uuid.uuid4())
      email_id = str(uuid.uuid4())

      emails_info = {
        "email" : body["email"],
        "id" : email_id,
        "trip_id" : trip_id,
      }

      participant_info = {
        "emails_to_invite_id" : email_id,
        "id" : participant_id,
        "trip_id" : trip_id,
        "name": body["name"]
      }

      self.__emails_repository.registry_email(emails_info)
      self.__participants_repository.register_participants(participant_info)

      return {
        "body": {"participant_id":participant_id},
        "status_code":201
      }

    except Exception as exception:
      return {
        "body":{
          "error":"Bad Request", 
          "message": str(exception)
        },
        "status_code":500
      }