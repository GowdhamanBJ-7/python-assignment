import os
from datetime import datetime


# Complete the time_delta function below.
def time_delta(t1, t2):
    # Define the datetime format (including timezone %z)
    fmt = "%a %d %b %Y %H:%M:%S %z"

    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)

    # Calculate absolute time difference in seconds
    diff = abs(int((dt1 - dt2).total_seconds()))
    return str(diff)

