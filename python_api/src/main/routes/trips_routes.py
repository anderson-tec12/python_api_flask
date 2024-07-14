from flask import jsonify, Blueprint, request

# Controllers
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer
from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder
from src.controllers.participant_creator import ParticipantsCreator
from src.controllers.activity_creator import ActivityCreator
from src.controllers.participant_confirmer import ParticipantsConfirmer
from src.controllers.participants_finder import ParticipantFinder
from src.controllers.activity_finder import ActivityFinder

# Repositorios
from src.models.repositories.trips_repositories import TripsRepository
from src.models.repositories.emails_to_invite_reporitory import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.activities_repository import ActivitiesRepository
from src.models.repositories.participants_repository import ParticipantsRepositoty

# Importanto o gerente de conexoes
from src.models.settings.db_connection_handler import db_connection_handler

trips_routes_bp = Blueprint("trip_routes", __name__)

@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():

  conn = db_connection_handler.get_connection()

  trips_repository = TripsRepository(conn)
  emails_repository = EmailsToInviteRepository(conn)

  controller = TripCreator(trips_repository, emails_repository)

  response = controller.create(request.json) #reqest json é os dados enviados

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])
def find_trip(tripId):

  conn = db_connection_handler.get_connection()

  trips_repository = TripsRepository(conn)
 
  controller = TripFinder(trips_repository)

  response = controller.find_trips_details(tripId)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/confirm/<tripId>", methods=["GET"])
def confirm_trip(tripId):

  conn = db_connection_handler.get_connection()

  trips_repository = TripsRepository(conn)
 
  controller = TripConfirmer(trips_repository)

  response = controller.confirm(tripId)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/link", methods=["POST"])
def create_trip_link(tripId):

  conn = db_connection_handler.get_connection()

  trips_repository = LinksRepository(conn)
 
  controller = LinkCreator(trips_repository)

  response = controller.create(request.json, tripId)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/link", methods=["GET"])
def find_links(tripId):

  conn = db_connection_handler.get_connection()

  link_repository = LinksRepository(conn)
 
  controller = LinkFinder(link_repository)

  response = controller.find(tripId)

  return jsonify(response["body"]), response["status_code"]
  
@trips_routes_bp.route("/trips/<tripId>/invites", methods=["POST"])
def invite_to_trip(tripId):

  conn = db_connection_handler.get_connection()

  participant_repository = ParticipantsRepositoty(conn)
  emails_repository = EmailsToInviteRepository(conn)
 
  controller = ParticipantsCreator(participant_repository, emails_repository)

  response = controller.create(request.json, tripId)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/activities", methods=["POST"])
def activities(tripId):

  conn = db_connection_handler.get_connection()

  activity_repository = ActivitiesRepository(conn)
  
  controller = ActivityCreator(activity_repository)

  response = controller.create(request.json, tripId)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/activities", methods=["GET"])
def find_activities(tripId):

  conn = db_connection_handler.get_connection()

  repository = ActivitiesRepository(conn)
 
  controller = ActivityFinder(repository)

  response = controller.find_from_trip(tripId)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/invites", methods=["GET"])
def find_participants(tripId):

  conn = db_connection_handler.get_connection()

  repository = ParticipantsRepositoty(conn)
 
  controller = ParticipantFinder(repository)

  response = controller.find_participants_from_trips(tripId)

  return jsonify(response["body"]), response["status_code"]

@trips_routes_bp.route("/trips/<tripId>/invites/confirmer", methods=["PATCH"])
def confirmed_participants(tripId):

  print(tripId)

  conn = db_connection_handler.get_connection()

  repository = ParticipantsRepositoty(conn)
 
  controller = ParticipantsConfirmer(repository)

  response = controller.confirm(tripId)

  return jsonify(response["body"]), response["status_code"]