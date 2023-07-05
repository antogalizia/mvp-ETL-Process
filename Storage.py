from datetime import date
import os
import shutil
from Locators import Directories


paths = Directories()

class Storage:
    # I get the current month and day to then move the file to its folder as appropriate
    current_day = date.today()
    month = current_day.strftime("%B")

    # I define the new file path will correspond to the current month
    directory = paths.project_destiny + f'\{month}'

    def store(self):
        route_downloads = Directories.origin
        route_destiny = Directories.project_destiny

        if not os.path.isfile(route_downloads):
            print("File not found")
            exit()

        if os.path.isdir(route_destiny):
            shutil.move(route_downloads, route_destiny)

        os.chdir(paths.project_destiny)

        # I create the directory and move the file into it
        if not os.path.exists(Storage.directory):
            os.makedirs(Storage.month)
            shutil.move(paths.csv_file_path, Storage.directory)

        os.chdir(Storage.directory)
        month_day = Storage.current_day.day

        # I rename the file according to the week
        match month_day:
            case 7:
                os.rename("ventas.csv", "SPW1.csv")
            case 14:
                os.rename("ventas.csv", "SPW2.csv")
            case 21:
                os.rename("ventas.csv", "SPW3.csv")
            case 28:
                os.rename("ventas.csv", "SPW4.csv")
            case _:
                os.rename("ventas.csv", "SR.csv")













