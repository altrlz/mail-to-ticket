from ._anvil_designer import MainTemplate
from anvil import *

from ..Dashboard.Dashboard import Dashboard
from ..Tickets.Tickets import Tickets
from ..Config.Config import Config

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.link_dashboard.tag.form_to_open = Dashboard()
    self.link_tickets.tag.form_to_open = Tickets()
    self.link_config.tag.form_to_open = Config()

    # Any code you write here will run when the form opens.
    
  def nav_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    form_to_open = event_args['sender'].tag.form_to_open
    
    self.content_panel.clear()
    self.content_panel.add_component(form_to_open)

