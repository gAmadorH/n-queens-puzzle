from functools import wraps
import time

def timer(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    start_time = time.time()
    returned = func(*args, **kwargs)
    end_time = time.time()
    duration_ms = (end_time - start_time) * 1000

    print('"{0}" function has taken {1} ms'.format(func.__name__, duration_ms))
    return returned
  return wrapper