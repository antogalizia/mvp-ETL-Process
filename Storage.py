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
        route_downloads = paths.origin
        route_destiny = paths.project_destiny

        if not os.path.isfile(route_downloads):
            print("File not found")
            exit()

        if os.path.isdir(route_destiny):
            shutil.move(route_downloads, route_destiny)

        os.chdir(route_destiny)

        # I create the directory and move the file into it
        if not os.path.exists(Storage.directory):
            os.makedirs(Storage.month)
            shutil.move(paths.csv_file_path, Storage.directory)
















