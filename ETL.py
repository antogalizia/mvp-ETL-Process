from Extract import Actions
from Storage import Storage

storage = Storage()
action = Actions()

def extract():

    action.account()
    action.sales_access()
    storage.store()


extract()


