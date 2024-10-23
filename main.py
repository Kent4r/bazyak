import cianparser
from time import sleep
a=6
while a < 54:
    data = cianparser.CianParser(location="Москва").get_flats(deal_type="sale",
                                                              rooms=4,
                                                              with_saving_csv=True,
                                                              with_extra_data=True,
                                                              additional_settings={"start_page":1+a, "end_page":2+a})
    print("----------------------------------------------------")
    print("Waiting 120 sec")
    sleep(120)
    a+=2
