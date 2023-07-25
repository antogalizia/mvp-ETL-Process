from Extraction import Extraction
from Storage import Storage
from Transformation import Transformation

storage = Storage()
extraction = Extraction()
transformation = Transformation()

def etl():

    extraction.account()
    extraction.sales_access()
    storage.store()
    transformation.cleaning()
    transformation.rename()


etl()






