import time
from typing import Callable

class TestBase:
  """
  Base utilities for algorithm testing.
  Not a replacement for pytest — a discipline layer.
  """

  def measure_time(self, func: Callable, *args, **kwargs) -> float:
    """
    Measure execution time of a function.
    Args:
      func: Function to be measured
      *args: Positional arguments for the function
      **kwargs: Keyword arguments for the function
    Returns:
      Execution time in seconds
    """
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    
    return end_time - start_time

