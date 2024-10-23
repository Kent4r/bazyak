import cianparser
from time import sleep
a=0
while a < 54:
    data = cianparser.CianParser(location="Москва").get_flats(deal_type="sale",
                                                              rooms=3,
                                                              with_saving_csv=True,
                                                              with_extra_data=True,
                                                              additional_settings={"start_page":1+a, "end_page":2+a})
    print("----------------------------------------------------")
    print("Waiting 30 sec")
    sleep(30)
    a+=2
