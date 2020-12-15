from config.configuration import conn 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_trailer(title):  
    """ Con esta función obtenemos el trailer de una película de la página de IMDb
        arg: 
            title : Título de la película
        return:
            url: url donde esta almacenadoel trailer
    """  
    driver = webdriver.Chrome("./chromedriver")

    driver.get("https://www.imdb.com/")

    label_search = driver.find_elements_by_css_selector("div form div div input")[1]
    label_search.click()

    #Tengo el cursos en label de buscar
    label_search.send_keys(title)
    label_search.send_keys(Keys.RETURN)

    # Ya tengo estoy dentro de las películas
    film = driver.find_elements_by_css_selector("td a")

    #La primera peli es la correcta y clicamos en ella
    film[0].click()

    #Buscamos el trailer
    trailer  = driver.find_elements_by_css_selector("div.slate")
    try:
        trailer[0].click()
        # Obtenemos la url del trailer
        url = driver.current_url
    except:
        url = 'Trailer not found'
    driver.close()
   
    

    return url