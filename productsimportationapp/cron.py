from datetime import datetime
from productsimportationapp.models import ProductsImportationHistory
import requests
import gzip
import shutil
import psutil
import os
from time import time


def import_data_from_web() -> None:
    url = 'https://challenges.coode.sh/food/data/json/index.txt'
    url_download = 'https://challenges.coode.sh/food/data/json/'
    begin_time = time()

    try:
        request_list = requests.get(url=url)
    except:
        return None

    if request_list.status_code == 200:
        products_list = request_list.text.split()

        if len(products_list) > 0:
            try:
                request_download_list = requests.get(url=url_download + products_list[0], stream=True)
            except:
                return None

            if request_download_list.status_code == 200:

                try:
                    with open(products_list[0], 'wb') as f:
                        f.write(request_download_list.raw.read())  # products_01.json.gz

                        for i in os.listdir():
                            if i.endswith('.json.gz'):
                                filename = i

                        with gzip.open(filename, 'rb') as f_in:
                            updated_filename = filename.replace('.gz', '')
                            with open(updated_filename, 'wb') as f_out:
                                shutil.copyfileobj(f_in, f_out)

                        end_time = time()
                        tdelta = begin_time - end_time

                        # Saving to db
                        now = datetime.now()
                        info = ''
                        info += f' Total: {psutil.virtual_memory()._asdict()["total"]}'
                        info += f' Available: {psutil.virtual_memory()._asdict()["available"]}'
                        info += f' Percent: {psutil.virtual_memory()._asdict()["percent"]}'
                        info += f' Used: {psutil.virtual_memory()._asdict()["used"]}'
                        info += f' Free: {psutil.virtual_memory()._asdict()["free"]}'

                        ProductsImportationHistory.objects.create(
                            is_connection_good=True,
                            last_time_cron_ran=now,
                            time_online=tdelta,
                            memory_usage=info
                        )

                except:
                    return None

    return None
