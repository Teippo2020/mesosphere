import inspect

def _get_fields(cls):
  """
    Gets the fields from a class.
    
    Args:
      cls (Schema class): The class from which the fileds will be retrieved
    Returns:
      tuple (of tuples): A tuple with the fields retrieved.
  """

  _fields = inspect.getmembers(cls, lambda f:not(inspect.isroutine(f)))
  fields = tuple(
    filter(
      lambda f: not(f[0].startswith("__") or f[0].endswith("__")),
      _fields
   )
  )
  return fields





class Schema(object):
  """
    Class used to deal with the validation of the fields.
  """

  __fields = () # Stores the fields to be used later

  def __init__(self, *args, **kwargs):
      super(Schema, self).__init__(*args, **kwargs)

      self.__fields = _get_fields(self);


