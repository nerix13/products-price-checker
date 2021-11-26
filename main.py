from utils.product_ctrl import *

from bs4 import BeautifulSoup
from colorama import Fore
import urllib3
import sys

http = urllib3.PoolManager()

if __name__ == '__main__':
    search = sys.argv[1].replace(" ", "-")
    print("Searching results of "+search+"...")
    r = http.request("GET", f"https://listado.mercadolibre.com.mx/{search}#D[A:{search}]")

    if (r.status == 200):
        soup = BeautifulSoup(r.data, 'html.parser')
        products = soup.find('ol', {'class':'ui-search-layout'}) # product list
        results = 0 # products found
        product_list = []
        for product in products.findChildren("li", recursive=False):
            p = Product(product)
            # print all products
            if sys.argv[2] == "-a" or sys.argv[2] == "--show-all":
                print("-"*30)
                get_product_info(p)
            product_list.append(p)
            results += 1

        # parameter options
        if (sys.argv[2] == "--get-cheapest"):
            get_product_most_("cheap", product_list)
        elif (sys.argv[2] == "--get-most-expensive"):
            get_product_most_("expensive", product_list)
        elif sys.argv[2] == "-a" or "--show-all":
            print("Total result found:", Fore.GREEN, results, Fore.RESET, "products\n")
        elif sys.argv[2] == "--best-seller":
            get_product_('best-seller', product_list)
        elif sys.argv[2] == "--best-recommended":
            get_product_('best-recommended', product_list)
    else:
        print(Fore.RED+"[x] Cann't connect to https://listado.mercadolibre.com.mx"+Fore.RESET)



