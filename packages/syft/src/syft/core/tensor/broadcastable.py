# stdlib
from typing import Sequence


def is_broadcastable(shape1: Sequence, shape2: Sequence) -> bool:
    """Helper function to determine if Tensor Operations can be broadcast
    inputs:
    shape1, shape 2: shapes of numpy arrays/syft tensors

    outputs:
    True or False
    """
    for a, b in zip(shape1[::-1], shape2[::-1]):
        if a == 1 or b == 1 or a == b:
            pass
        else:
            return False
    return True


# def is_mat_multiplicable(shape1: Sequence, shape2: Sequence) -> bool:
#     if len(shape1) >= 2:
#         if shape1[-1] == shape2[-2]:
#             return True
#         return False
#     else:
#         if shape1[0] == shape2[-2]:
#             return True
#         return False
