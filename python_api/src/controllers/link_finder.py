from typing import Dict
import uuid

from src.models.repositories.links_repository import LinksRepository

class LinkFinder:
  def __init__(self, link_repository:LinksRepository) -> None:
    self.__link_repository = link_repository
  
  def find(self, trip_id) -> Dict :
    
    try:
      
      links = self.__link_repository.find_links_from_trip(trip_id)

      return {
        "body":{"links":links},
        "status_code":200
      }
    
    except Exception as exception:
        return {
          "body":{
            "error":"Bad Request", 
            "message": str(exception)
          },
          "status_code":500
        }