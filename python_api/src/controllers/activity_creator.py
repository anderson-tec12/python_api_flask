from typing  import Dict
import uuid


from src.models.repositories.activities_repository import ActivitiesRepository



class ActivityCreator:
  def __init__(self, activities_repository:ActivitiesRepository) -> None:
    self.__activities_repository = activities_repository
  
  def create(self, body, trip_id) -> Dict:
    try:
      id = str(uuid.uuid4())

      activity_info = {
        "id" : id,
        "trip_id" : trip_id,
        "title": body["title"],
        "occurs_at": body["occurs_at"]
      }

      self.__activities_repository.registry_activities(activity_info)

      return {
        "body": {"activityId":id},
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