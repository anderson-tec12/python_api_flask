from flask import jsonify, Blueprint, request

# Controllers
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer
from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder

# Repositorios
from src.models.repositories.trips_repositories import TripsRepository
from src.models.repositories.emails_to_invite_reporitory import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository

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