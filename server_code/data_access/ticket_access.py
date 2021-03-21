from datetime import datetime, timedelta

import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def add_ticket(ticket_dict):
  app_tables.tickets.add_row(
    created=datetime.now() + timedelta(hours=9),
    **ticket_dict
  )

@anvil.server.callable
def get_tickets():
  return app_tables.tickets.search()

