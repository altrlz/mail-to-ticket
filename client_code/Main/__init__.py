from ._anvil_designer import MainTemplate
from anvil import *

from ..Dashboard.Dashboard import Dashboard
from ..Tickets.Tickets import Tickets
from ..Config.Config import Config

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  def reset_links(self, **event_args):
    self.link_dashboard.role = ''
    self.link_tickets.role = ''
    self.link_config.role = ''

  def link_dashboard_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.reset_links()
    self.link_dashboard.role = 'selected'
    
    new_panel = Dashboard()
    
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(new_panel)

  def link_tickets_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.reset_links()
    self.link_tickets.role = 'selected'
    
    new_panel = Tickets()
    
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(new_panel)

  def link_config_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.reset_links()
    self.link_config.role = 'selected'
    
    new_panel = Config()
    
    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(new_panel)




