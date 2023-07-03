import os
import shutil
from Localizadores import Transform

# storage() is a function that takes the sales.csv file and moves it to the root directory of my project
def storage():
    route_downloads = Transform.origin
    route_destiny = Transform.destiny

    if not os.path.isfile(route_downloads):
        print("File not found")
        exit()

    if os.path.isdir(route_destiny):
        shutil.move(route_downloads, route_destiny)


storage()





