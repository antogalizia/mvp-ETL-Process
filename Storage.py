import pandas as pd
from datetime import date
import os
import shutil
from Locators import Transform

paths = Transform()

# I get the current month and day to then move the file to its folder as appropriate
current_day = date.today()
month = current_day.strftime("%B")
month_day = current_day.day


# I define the new file path will correspond to the current month
os.chdir(paths.destiny)
directory = paths.destiny + f"\{month}"

# I create the directory and move the file
if not os.path.exists(directory):
    os.makedirs(month)
    shutil.move(paths.origin, directory)

os.chdir(directory)

match month_day:
    case 3:
        os.rename("ventas.csv", "SPW1.csv")
    case 14:
        os.rename("ventas.csv", "SPW2.csv")
    case 21:
        os.rename("ventas.csv", "SPW3.csv")
    case 28:
        os.rename("ventas.csv", "SPW4.csv")
    case _:
        os.rename("ventas.csv", "SR.csv")







