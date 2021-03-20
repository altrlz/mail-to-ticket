from ._anvil_designer import ConfigTemplate
from anvil import *

class Config(ConfigTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.