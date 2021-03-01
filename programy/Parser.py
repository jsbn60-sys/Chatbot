from io import StringIO
import selenium
import time
from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def createFile(Studiengang):
    with open(str(Studiengang)+".aiml", "a+") as file_object:
        file_object.write('<?xml version="1.0" encoding="UTF-8"?>')
        file_object.write('<aiml version="1.0"')

def closeFile(Studiengang):
    with open(str(Studiengang)+".aiml", "a+") as file_object:
        file_object.write('</aiml>')

def writeFile(Studiengang, Modulname,Modulnummer,Modulverantwortliche, Kurzbeschreibung,Aufwand,Voraussetzungen):
    with open(str(Studiengang)+".aiml", "a+") as file_object:
        file_object.write("\n")
        file_object.write("<category>")
        file_object.write("^" + Modulname + "^</pattern>")
        file_object.write("<template>")
        file_object.write("Modulname: " + Modulname)
        file_object.write("   --Modulnummer:" + Modulnummer)
        file_object.write("</template>")
        file_object.write("</category>")
        file_object.write("\n")
        #Verantwortlicher
        file_object.write("<category>")
        file_object.write("<pattern><set>VerantwortlichModul</set>" + Modulnummer + "^</pattern>")
        file_object.write("<template>")
        file_object.write("Modulname: " + Modulname)
        file_object.write(" --Modulverantwortliche/r: " + Modulverantwortliche)
        file_object.write("</template>")
        file_object.write("</category>")
        file_object.write("\n")
        #Kurzbeschreibung
        file_object.write("<category>")
        file_object.write("<pattern><set>KurzbeschreibungModul</set>" + Modulnummer + "^</pattern>")
        file_object.write("<template>")
        file_object.write("Modulname: " + Modulname)
        file_object.write("--Kurzbeschreibung: " + Kurzbeschreibung)
        file_object.write("</template>")
        file_object.write("</category>")
        file_object.write("\n")
        #Aufwand
        file_object.write("<category>")
        file_object.write("<pattern><set>AufwandModul</set>"+Modulnummer+"^</pattern>")
        file_object.write("<template>")
        file_object.write("Modulname: " + Modulname)
        file_object.write("  --Aufwand: " + Aufwand)
        file_object.write("</template>")
        file_object.write("</category>")
        file_object.write("\n")
        #Voraussetzungen
        file_object.write("<category>")
        file_object.write("<pattern><set>VoraussetzungenModul</set>" + Modulnummer + "^</pattern>")
        file_object.write("<template>")
        file_object.write("Modulname: " + Modulname)
        file_object.write("  --Voraussetzungen: " + Voraussetzungen)
        file_object.write("</template>")
        file_object.write("</category>")

#Öffnen der THM-Website und per for-Schleife sämtliche Einträge durchgehen.
def parse1():
    #Website öffnen
    driver = webdriver.Chrome(executable_path=r"C:\Users\RGB\PycharmProjects\TwitchBot\chromedriver.exe")
    driver.get("https://www.thm.de/organizer/modulhandbuecher/fb-06-mni/modulhandbuch-inf-bs-2010.html")
    Studiengang= driver.find_element_by_xpath('//*[@id="main"]/div/div/div/div/div/div/h1').text
    createFile(Studiengang)


    #Anzahl der Module
    for x in range(115):
        element = driver.find_element_by_xpath('//*[@id="Subjects-list"]/tbody/tr[{}]/td[1]/a'.format(x+1)) #Element suchen
        element.click()
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB) #Tab wechslen, da beim Klicken automatisch ein neuer Tab geöffnet wird
        driver.switch_to.window(driver.window_handles[-1])
        Modulname = driver.find_element_by_xpath('//*[@id="main"]/div/div/div/div/div/div/h1').text
        Modulnummer = driver.find_element_by_xpath('//*[@id="j-main-container"]/div[2]/div[2]').text
        Modulverantwortliche = driver.find_element_by_xpath('//*[@id="j-main-container"]/div[3]/div[2]').text
        Kurzbeschreibung = driver.find_element_by_xpath('//*[@id="j-main-container"]/div[5]/div[2]').text
        Aufwand = driver.find_element_by_xpath('//*[@id="j-main-container"]/div[10]').text
        #Fehler abfangen, falls keine Voraussetzungen gegeben sind.
        try:
            Voraussetzungen =driver.find_element_by_xpath('//*[@id="j-main-container"]/div[18]/div[2]').text
        except NoSuchElementException:
            print("Keine Vorraussetzungen")
            Voraussetzungen = "Keine Vorraussetzungen"
        writeFile(Studiengang, Modulname,Modulnummer,Modulverantwortliche,Kurzbeschreibung,Aufwand,Voraussetzungen)
        time.sleep(0)
        driver.close() #Tab schließen
        driver.switch_to.window(driver.window_handles[-1])  #Tab in Main-Tab wechslen.




#Link für Modulhandbuch: https://www.thm.de/organizer/modulhandbuecher/fb-06-mni/modulhandbuch-inf-bs-2010.html

parse1()    #Funktion ausführen.
