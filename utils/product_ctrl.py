# Author: Saul Neri

from colorama import Fore, Back

class Product:
    def __init__(self, product_node):
        self.link = product_node.find(class_="ui-search-link").get("href")
        self.title = product_node.find("h2", {"class":"ui-search-item__title"}).get_text()
        self.price_str = product_node.find("span", {"class":"price-tag-fraction"}).get_text()
        self.price = float(self.price_str.replace(",", ""))
        self.is_best_seller = (product_node.find("div", {"class":"ui-search-item__highlight-label--best_seller"})) != None
        self.is_recommended = (product_node.find("div", {"class":"ui-search-item__highlight-label--meli_choice"})) != None
        self.has_clasification = (product_node.find(class_="ui-search-reviews__ratings")) != None
        self.reviews_available = (product_node.find(class_="ui-search-reviews__amount")) != None
        # califications evaluating
        if self.reviews_available:
            self.reviews = product_node.find(class_="ui-search-reviews__amount").get_text()
        if self.has_clasification:
            self.stars_len = len(product_node.find(class_="ui-search-reviews__ratings").find_all("svg"))
            self.stars = "*" * self.stars_len


def get_product_most_(flag: str, products: list):
    price_list = []
    # price collection
    for product in products:
        price_list.append(product.price)
    # check the falg
    if flag == "cheap":
        required_price = min(price_list)
    elif flag == "expensive":
        required_price = max(price_list)

    # get the cheapest product by price
    for product in products:
        if product.price == required_price:
            print(f"-----[ MOST {flag.upper()} PRODUCT ]-----")
            get_product_info(product)
            break


def get_product_info(product: Product):
    # label highlight
    if product.is_best_seller:
        print(Fore.BLACK+Back.YELLOW+"\t  MAS VENDIDO  "+Fore.RESET+Back.RESET)
    elif product.is_recommended:
        print(Fore.BLACK+Back.WHITE+"\t  RECOMENDADO  "+Fore.RESET+Back.RESET)
    print("Product title: ", Fore.YELLOW+product.title+Fore.RESET)
    print("Price: $ ", Fore.YELLOW+product.price_str+Fore.RESET)
    # review check
    if product.reviews_available:
        print("Reviews:", Fore.YELLOW+product.reviews+Fore.RESET)
    else:
        print("Reviews:", Fore.RED+"Reviews no available..."+Fore.RESET)
    # clasification check
    if product.has_clasification:
        print("Calification:", Fore.YELLOW+product.stars+Fore.RESET)
    else:
        print("Calification:", Fore.RED+"Clasification no available..."+Fore.RESET)
    print("Link:", Fore.GREEN+product.link+Fore.RESET)
    print(30*"-")
    print("\n")


def get_product_(flag: str, products: list):
    if flag == "best-seller":
        for product in products:
            if product.is_best_seller:
                print("-----[ BEST SELLER ]-----")
                get_product_info(product)
    elif flag == "best-recommended":
        for product in products:
            if product.is_recommended:
                print("-----[ BEST RECOMMENDED ]-----")
                get_product_info(product)







