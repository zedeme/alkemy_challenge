from common import config_data
from datetime import datetime

# Codigo no reutilizable en la creacion de tablas
def create_tables(df):
    config = config_data()["data_dictionary"]["columns"]["make_tables"]
    tables = {}

    tables[0] = df[config["first_table"]]

    tables[1] = df[config["second_table"]].groupby(['category', 'provincia'])['fuente'].count()

    tables[2] = df[df["category"] == "cine"][config["third_table"]].groupby(['provincia'])[['pantallas','espacio_incaa', 'butacas']].sum()

    return tables

    

    

