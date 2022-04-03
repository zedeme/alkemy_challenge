import pandas as pd
import os
from common import config_data
import logging
import numpy as np
from static_tables import create_tables
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Cleaner():

    # Se encarga de mandar el dataframe al script no reutilizable static_data.py para obtener las tablas.
    def _to_table(self, df):
        return create_tables(df)

    # Toma las columnas a reemplazar de data_config.yaml
    # Limpia el nombre de las columnas de todos los df
    def _clean_columns(self, df):
        logger.info("Cleaning columns of data.")
        df = df.rename(columns=self.__config["columns"]["replaces"])

        return df
            
    # Toma ciertos valores de las filas y los reemplaza por los que estan en config_data.yaml 
    def _clean_rows(self, df):
        logger.info("Cleaning rows of data.")
        try:
            for i, (k, v) in enumerate(self.__config["rows"].items()):
                df[k] = df[k].replace(v["replaces"])
        except Exception as e:
            logger.warning("Error cleaning the rows of data. " + str(e))
        
        logger.info("Detecting the null values.")

        try:
            for i in df.columns:
                df[i] = df[i].apply(lambda x: np.nan if x == "None" else x)
        except Exception as e:
            logger.warning("Error detecting None values.")

        return df

    # Obtiene la informacion, la limpia, la guarda 
    def get_data(self):

        logger.info("Getting data.")

        path = "./data/"

        try:
            files = [i for i in os.listdir(path)]

            if files == []:
                raise FileNotFoundError

            df = pd.DataFrame()

            for file in files:
              df_t = pd.read_csv(path + file)

              df_t["category"] = file.split("\\")[0] # Create better category's column
              df_t["date_update"] = datetime.now()

              df_t.columns = df_t.columns.str.lower()

              df = pd.concat([df_t, df])
        except Exception as e:
            logger.warning("Error getting the data.")
            return

        return df


    def __init__(self):
        self.__config = config_data()["data_dictionary"]
        df = self.get_data()

        df_r = self._clean_rows(df)
        
        df_c = self._clean_columns(df_r)

        tables = self._to_table(df_c)

        self._tables = tables

if __name__ == "__main__":
    Cleaner()