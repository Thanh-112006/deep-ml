import numpy as np
from math import sqrt
def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    if norm_type == "l1":
        arr = arr.flatten()
        res = sum(abs(i) for i in arr)
        return float(res)
    elif norm_type == "l2":
        arr = arr.flatten()
        res = sqrt(sum(i*i for i in arr))
        return float(res)
    elif norm_type == "linf":
        arr = arr.flatten()
        res = max(abs(i) for i in arr)
        return float(res)
    elif norm_type == "frobenius":
        res = 0
        if arr.ndim != 2:
            raise ValueError("failed")
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                res += arr[i][j] **2
        return sqrt(res)
    else:
        raise ValueError("failed")





