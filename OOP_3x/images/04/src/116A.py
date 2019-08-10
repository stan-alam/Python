class Inventory:
  def lock(self, item_type):
    """select a type of item. This method will lock the currently selected item as to prevent race conditions...preventing the selling of the same item to more than one person at a time"""
    pass

  def unlock(self, item_type):
    """Release the given type so other's have    access to it"""
    pass

  def purchase(self, item_type):
    """if the item is NOT locked, raise an exception. If the item_type does not exist, raise an exception. If the item is currently out of stock, raise an exception. If the item is available, subtract one item and return the number of items left."""
    pass
