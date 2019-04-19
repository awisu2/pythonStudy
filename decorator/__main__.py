from functools import wraps

# normal decotator
def decorator(f):
  @wraps(f)
  def wrapper(*args, **kwargs):
    print('call decotator')
    kwargs['foo'] = 'bar'
    return f(*args, **kwargs)

  return wrapper

# with args decotator
def decorator_with_args(a, *, is_stop=False):
  def decorator(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
      print('call decorator_with_args', a, is_stop)
      if is_stop:
        print('stop on decorator')
        return

      return f(*args, **kwargs)

    return wrapper
  return decorator

@decorator
def sample(foo=None):
  print('sample!', foo)

@decorator_with_args(222)
def sample_with_args():
  print('sample2!')

@decorator
@decorator_with_args(333)
def sample_multi(foo=None):
  print('sample_multi!', foo)

@decorator_with_args(999, is_stop=True)
def sample_stop():
  print('sample_stop!')

def main(z=None):
  sample()
  sample_with_args()
  sample_multi()
  sample_stop()

if __name__ == "__main__":
  main()