from typing import Dict
import uuid

from src.models.repositories.links_repository import LinksRepository

class LinkCreator:
  def __init__(self, link_repository:LinksRepository) -> None:
    self.__link_repository = link_repository
  
  def create(self, link_infos_body, trip_id) -> Dict :
    
    try:
      link_id = str(uuid.uuid4())
      link_infos_with_id = {
        "id":link_id,
        "trip_id":trip_id,
         **link_infos_body,
        }
      self.__link_repository.registry_link(link_infos_with_id)

      return {
        "body":{"linkId":link_id},
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