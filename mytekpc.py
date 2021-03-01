import urllib.request as ulib
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
def get_html(source):
    with ulib.urlopen(source) as u:
        return u.read()
def scrap_mytek_pc():

 url = "https://www.mytek.tn/informatique/ordinateurs-portables/pc-portable.html"
 index = 0
 nombre_produit=1
 currentpage = 1
 produits = []
 from bs4 import BeautifulSoup as bs

 print(nombre_produit)
 while   index <=nombre_produit:

    
    
    page = get_html(url)
    soup = bs(page)
    blocpagination = soup.find("p" ,  attrs={"id" :"toolbar-amount"}).text.strip()
    nbprod = blocpagination[19:]
    nombre_produit = int(nbprod)
    

    bloc = soup.find_all("ol", attrs={"class": "products list items product-items"})

    for produitlist in bloc:
        produit = produitlist.find_all("li")
        for item in produit:
            produit = {}
            image = item.div.div.a.span.span.img["src"].strip()
            
            name = item.find("strong" , attrs={"class" : "product name product-item-name"}).a.text
            
            lien = item.div.div.a["href"].strip()
            
            categorie = "PcPortable"
            
            prix = item.find("span" , attrs={ "class" : "price"}).text.strip()
            prix = int(prix[:-4])

            site_officiel="mytek"

            etat = "disponible"
            
            marque=""
            marques = ["ACER" , "DELL" , "ASUS" , "LENOVO" ,"VEGA" , "HP" , "MSI" , "VERSUS"]
            for im in marques :
                if(im in name):
                    marque = im
                    break

            
            refernece = item.find("div" , attrs={"class" : "product-item-inner"}).div.div.form["data-product-sku"]
            
            index = index + 1

            produit['nom'] = name
            produit['image']= image
            produit['prix']=prix
            produit['description']= ""
            produit['etat']=etat
            produit['marque']=marque
            produit['lien']=lien
            produit['site_officiel']=site_officiel
            produit['categorie'] = categorie
            produit['reference'] = refernece
            produits.append(produit)
              
    print(nombre_produit)  
    print(index)
         
    currentpage =currentpage +1
    curr = str(currentpage)
    url="https://www.mytek.tn/informatique/ordinateurs-portables/pc-portable.html?p="+curr
    print(url)
        

 return produits
       
        
    


