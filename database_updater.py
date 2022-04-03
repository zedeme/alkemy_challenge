from decouple import config
import logging
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine, text
import os
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Saver():
    # Inserta los datos adentro de las tablas
    def __insert_data(self, tables, engine):
        files = [i.split(".")[0] for i in os.listdir(self.path)]
        for i in range(len(tables)):
            try:
                tables[i].to_sql(files[i], con=engine, if_exists="replace", index=False)
            except Exception as e:
                logger.warning("Error inserting tables." + str(e))

    # Crea las tablas de la base de datos
    def __create_database_tables(self, engine):
        logger.info("Creating tables for database")

        files = [i for i in os.listdir(self.path)]

        try:
            for i in files:
                # Reading sql files
                with open(self.path + i, mode="r") as f:
                    with engine.connect() as eng:
                        s = text(f.read())
                        eng.execute(s)
        except Exception as e:
            logger.warning("Error executing sql scripts." + str(e))
            print(str(e))

        return files
                        

    # Crea la base de datos
    def __create_database(self):
            logger.info("Creating database.")

            engine_url = "postgresql://" + config("USER") + ":" + config("PASSWORD") + "@" + config("HOST") + ":" + config("PORT") + "/" + config("NAME")
            engine = create_engine(engine_url)
            
            try:
                if not database_exists(engine.url):
                    create_database(engine.url)
                    logger.info("Creating database.")
            except Exception as e:
                logger.warning("Error making database." + str(e))
            finally:
                return engine


    def __init__(self, tables):
        self.path = "./sql/"

        logger.info("Starting saving data.")

        engine = self.__create_database()

        self.__create_database_tables(engine)

        self.__insert_data(tables, engine)






