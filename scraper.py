import requests as rq
import logging
import argparse
from common import config
from datetime import datetime
from os import path, mkdir, listdir, remove

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Scraper():
    def __init__(self):
        args = self.select_page()
        url = self._get_url(args)

        self._args = args

        self._scrape(url)


    # Revisa los argumentos pasados para scrapear.
    # Las URL estan en config.yaml.
    def select_page(self):
        parser = argparse.ArgumentParser()

        argentina_sites_choices = list(config()["argentina_sites"].keys())

        parser.add_argument("argentina_sites", help="Argentina sites to scrape", type=str, choices=argentina_sites_choices)

        args = parser.parse_args()

        return args

    # Parsea la direccion de los archivos para obtener el nombre que le va a asignar a los csv.
    def _get_file_name(self, url):

        category = url.split("/")[-1].split(".")[0]

        m = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

        month = datetime.now().month

        return datetime.now().strftime(category + "\\%Y-" + m[month - 1] + "\\" + category + "-%d-%m-%Y.csv")

    # Extrae las URL de config.yaml
    def _get_url(self, args):
        host = config()["argentina_sites"][args.argentina_sites]["url"]

        return host


    # Se encarga de relizar las peticiones para descargar los archivos y guardarlos con el nombre de su categoria.
    def _scrape(self, host):

        data_path = "./data/"

        if not path.exists(data_path):
            logger.info("Making the directory to save data.")
            mkdir(data_path)

        for i in listdir("./data/"):
            remove(data_path + i)

        # scraping and saving files
        for i in host:
            
            logger.info("Beginning scraper for: " + i)

            r = rq.get(i, allow_redirects=True)

            if r.status_code > 299 or r.status_code < 200:
                logger.warning("We have bad status, " + str(r.status_code) + ", can't continue with this page.")
                continue

            logger.info("We have a good state, " + str(r.status_code) + ", we can continue.")

            with open(data_path + self._get_file_name(i), mode="wb") as f:
                try:
                    f.write(r.content)
                except Exception as e:
                    logger.warning("We have a problem saving data." + e)
                finally:
                    f.close()





    
