from functools import wraps
import time

def timer(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    start_time = time.time()
    returned = func(*args, **kwargs)
    end_time = time.time()
    duration = (end_time - start_time)
    duration_ms = duration * 1000
    duration_s = duration_ms/1000
    duration_m = duration_s / 60


    print('"{0}" function has taken {1} ms'.format(func.__name__, duration_ms))
    print('"{0}" function has taken {1} seconds'.format(func.__name__, duration_s))
    print('"{0}" function has taken {1} minutes'.format(func.__name__, duration_m))

    return returned
  return wrapper