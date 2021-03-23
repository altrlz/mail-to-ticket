from datetime import datetime, timedelta

from ._anvil_designer import TicketsTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Tickets(TicketsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.refresh_tickets()

  def refresh_tickets(self):
    self.repeating_panel_1.items = anvil.server.call('get_tickets')
    
  def add_ticket_click(self, **event_args):
    ticket_dict = {
      "subject":"test2",
      "sendername":"testuser2",
      "senderEmailAddress":"testuser2@example.com",
      "receivedtime": datetime.now(),
      "body":"test2 comment"
    }
    
    
    anvil.server.call('add_ticket', ticket_dict)
    self.refresh_tickets()
    



