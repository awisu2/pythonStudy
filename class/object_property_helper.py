from functools import wraps

def set_property(self, name, value=None, *, is_read=True, is_write=True):
  """
  プロパティをセット
  """
  # set origin property
  property_name = f'__{name}'
  setattr(self, property_name, value)

  # set getter, setter
  getter = (lambda _: getattr(self, property_name)) if is_read else None
  setter = (lambda _, v: setattr(self, property_name, v)) if is_write else None
  setattr(self.__class__, name, property(getter, setter))

def set_property_decorator(name, value=None, **kwargs):
  """
  プロパティをセットするデコレータ
  """
  def _decorator(f):
    @wraps(f)
    def _wrapper(self, *_args, **_kwargs):
      set_property(self, name, value, **kwargs)
      return f(self, *_args, **_kwargs)

    return _wrapper
  return _decorator

