from abc import ABC, abstractmethod
from typing import Any

class AlgorithmBase(ABC):

  @abstractmethod
  def run(self, input_data: Any) -> Any:
    """
    Execute the algorithm.
    Args:
      input_data: Structured input for the algorithm
    Returns:
      Algorithm output
    """
    pass

  @abstractmethod
  def complexity(self) -> str:
    """
    Returns time and space complexity as a string.
    Example: "Time: O(n log n), Space: O(n)"
    """
    pass