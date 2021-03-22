from ._anvil_designer import MainTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import plotly.graph_objects as go

from ..Dashboard.Dashboard import Dashboard
from ..Tickets.Tickets import Tickets
from ..Config.Config import Config
from ..Timerecode.Timerecode import Timerecode

class Main(MainTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
  def reset_links(self, **event_args):
    self.link_dashboard.role = ''
    self.link_tickets.role = ''
    self.link_config.role = ''
    self.link_timerecode.role = ''
    
  def link_click(self, link, new_panel):
    self.reset_links()
    link.role = 'selected'

    get_open_form().content_panel.clear()
    get_open_form().content_panel.add_component(new_panel,full_width_row=True)

  def link_dashboard_click(self, **event_args):
    self.link_click(self.link_dashboard, Dashboard())

  def link_tickets_click(self, **event_args):
    self.link_click(self.link_tickets, Tickets())

  def link_timerecode_click(self, **event_args):
    self.link_click(self.link_timerecode, Timerecode())
    
  def link_config_click(self, **event_args):
    self.link_click(self.link_config, Config())    

  def content_panel_show(self, **event_args):
    self.link_dashboard_click(**event_args)

