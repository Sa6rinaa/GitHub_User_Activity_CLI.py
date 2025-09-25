import json
import sys #(pour récupérer les arguments)
import urllib.request #(pour faire la requête HTTP)

user=input("Saisir le nom d'utilisateur : ")

if user =="":
    print("Erreur")
    exit()
else :
    print("Valide")

base_url = "https://api.github.com/users/"
url = base_url + user + "/events"
print(url) 


