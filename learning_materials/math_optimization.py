from abc import ABC, abstractmethod

class MathOptimize(ABC):
  @abstractmethod
  def optimize(self):
    pass

class SqrtNewtonRaphson(MathOptimize):
  def optimize(self, value, x0=1, epsilon=1e-6, max_iter=10):
    """
    Returns the approximate value of the square root of the value with the given accuracy epsilon
    and maximum number of iterations max_iter using the Newton-Raphson method
    and initial approximation x0.
    """
    x = x0
    for i in range(max_iter):
        x = (x + value / x) / 2  # calculate next root value
        if abs(x**2 - value) < epsilon:  # check target threshold  
            return x
    return x
