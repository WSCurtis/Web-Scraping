from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/msi-geforce-rtx-3080-ti-rtx-3080-ti-gaming-x-trio-12g/p/N82E16814137650?Description=3080%20geforce%20rtx%20ti%2012gb%20gddr6x%20pci%20express%204.0&cm_re=3080_geforce%20rtx%20ti%2012gb%20gddr6x%20pci%20express%204.0-_-14-137-650-_-Product&quicklink=true"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)