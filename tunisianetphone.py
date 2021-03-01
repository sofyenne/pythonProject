
def scrap_tunisia_net_tel():
    url = "https://www.tunisianet.com.tn/596-smartphone-mobile-4g-tunisie"
    produits = []
    currentpage = 1
    nombre_produit = 1
    index = 0
    while nombre_produit > index:
        from bs4 import BeautifulSoup as bs
        import requests
        r = requests.get(url)
        soup = bs(r.content)
        bloc = soup.find_all("div", attrs={"class": "products product-thumbs row wb-product-list"})
        for i in bloc:
            prod = i.find_all("div", attrs={"class": "item-product col-xs-12"})

            for item in prod:
                produit = {}

                lien = item.article.div.div.a["href"].strip()

                image = item.article.div.div.a.img["src"].strip()

                nom = item.find("h2", attrs={"class": "h3 product-title"}).text

                site_officiel="tunisia_net"

                marque= item.find("div" , attrs={"class" : "product-manufacturer"}).a.img["alt"].strip()
                marque = marque.upper()

                description = item.find("div", attrs={"class": "listds"}).a.p
                x = str(description).removeprefix("<p>").removesuffix("</p>")
                etat = item.find("div", attrs={"id": "stock_availability"}).text.strip()

                categorie = "smartphone"

                prix = item.find("span", attrs={"class": "price"}).text
                prix = prix[:-7]
                if len(prix) >= 4:
                    prix = prix.replace(prix[1], "")

                ref = item.find("span", attrs={"class": "product-reference"}).text
                ref = ref[1:-1]

                index = index + 1
                produit['nom'] = nom
                produit['image'] = image
                produit['prix'] = prix
                produit['description'] = x
                produit['etat'] = etat
                produit['marque'] = marque
                produit['lien'] = lien
                produit['site_officiel'] = site_officiel
                produit['categorie'] = categorie
                produit['reference'] = ref
                produits.append(produit)
        currentpage = currentpage + 1
        curr = str(currentpage)
        bloc2 = soup.find("section", attrs={"id": "products"})
        element = bloc2.find("div",
                             attrs={
                                 "class": "col-md-4 col-lg-4 col-xl-4 hidden-lg-down total-products text-xs-right"}).p.text

        y = element.replace(" ", "-")

        z = y.removeprefix("Il-y-a-").removesuffix("-produits.")

        b = int(z)

        url = "https://www.tunisianet.com.tn/596-smartphone-mobile-4g-tunisie?page="+curr
        print(url)
        nombre_produit = b
        print(b)
        print(index)

    return produits





