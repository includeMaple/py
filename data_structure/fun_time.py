import time

def func_time(func):
  def wrapper(*args, **kwargs):
    tstart = time.time()
    result = func(*args, **kwargs)
    tend = time.time()
    logStr = '%s function use time: %s secs.' % (str(func.__name__), str(tend - tstart))
    print(logStr)
    return result

  return wrapper
