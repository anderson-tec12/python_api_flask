import sqlite3
from sqlite3 import Connection

class DbConnectionHandler:

  #Start da class
  def __init__(self) ->  None:
    self.__connection_string = "storage.db"
    self.__conn = None
  
  # Metodo para conectar ao banco
  def connect(self) -> None:
    conn = sqlite3.connect(self.__connection_string, check_same_thread=False) # Conexão com o banco de dados
    self.__conn = conn
  
  # Metodo para obter a conexão
  def get_connection(self) -> Connection:
    return self.__conn


# Garantindo que o projeto todo use apenas 1 conexão com o banco 
db_connection_handler = DbConnectionHandler() # Importando essa variavel e não a classe em si