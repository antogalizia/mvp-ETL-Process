import pandas as pd
import os
from Locators import Directories
from Storage import Storage

directory = Directories()
storage = Storage()

class Transformation:

    def cleaning(self):
        month = storage.month
        cwd = directory.project_destiny + f'\{month}'
        os.chdir(cwd)

        df = pd.read_csv('ventas.csv', delimiter=';', encoding='latin-1')

        # I delete irrelevant columns, fill null values and formatting.
        columns_to_remove = [6, 14, 15, 21, 23, 27, 28, 29, 30, 34, 36, 37, 38, 39]
        columns = df.columns[columns_to_remove]
        df = df.drop(columns, axis=1)
        df = df.fillna('None')

        df['Número'] = df['Número'].astype(str)
        df['Piso'] = df['Piso'].astype(str)

        # I concatenate some columns to present the complete address.
        df['Dirección completa'] = df['Dirección'] + ' ' + df['Número'].astype(str) + ' ' + df['Piso'].astype(str)
        df.drop(['Dirección', 'Número', 'Piso'], axis=1, inplace=True)

        df.to_excel('ventas_procesadas.xlsx', index=False, engine='openpyxl')


    def rename(self):
        month_day = storage.current_day.day

        # I rename the file according to the week
        match month_day:
            case 25:
                os.rename("ventas_procesadas.xlsx", "SPW1.xlsx")
            case 14:
                os.rename("ventas_procesadas.xlsx", "SPW2.xlsx")
            case 21:
                os.rename("ventas_procesadas.xlsx", "SPW3.xlsx")
            case 28:
                os.rename("ventas_procesadas.xlsx", "SPW4.xlsx")
            case _:
                os.rename("ventas_procesadas.xlsx", "SR.xlsx")





