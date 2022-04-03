from scraper import Scraper
from data_cleaner import Cleaner
from database_updater import Saver
import logging
from decouple import config


if __name__ == "__main__":
    s = Scraper()
    c = Cleaner()

    # Revisa si se pidio scraper todos los datos.
    if s._args.argentina_sites != "all":
        logging.warning("If you dont select all, it will dont be save in database.")
    if s._args.argentina_sites == "all":
        Saver(c._tables)
    
    
    

