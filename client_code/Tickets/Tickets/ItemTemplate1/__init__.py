from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def detail_button_click(self, **event_args):
    self.visible_switch(self.body_data)
    self.visible_switch(self.comment_area_card)
    self.repeating_panel_1.items = anvil.server.call('get_comments', self.subject_data.text)

  def visible_switch(self, component):
    flg = component.visible
    if flg:
      component.visible = False
    else :
      component.visible = True

  def close_button_click(self, **event_args):
    self.visible_switch(self.comment_area_card)
    self.visible_switch(self.body_data)

