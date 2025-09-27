import json
import urllib.error
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


try:
    # Ouvrir l'URL et lire le contenu
    with urllib.request.urlopen(url) as response:
        data = response.read()              # lire les données brutes (bytes)
        text = data.decode("utf-8")         # décoder en texte (chaîne JSON)
        events = json.loads(text)           # convertir en objets Python (liste)

    print("Données récupérées avec succès !")
    print(events[:2])  # afficher seulement les 2 premiers événements pour tester

except urllib.error.HTTPError as e:
    if e.code == 404:
        print("Erreur : utilisateur introuvable")
    else:
        print(f"Erreur HTTP : {e.code}")

except urllib.error.URLError:
    print("Erreur : impossible de se connecter à GitHub")

except json.JSONDecodeError:
    print("Erreur : données JSON invalides")

for event in events:
    event["type"]
    if event["type"]=="PushEvent":
        event["payload"]
        print ("Pushed" {payload}" commits to" {payload} )
    if event["type"] == "IssuesEvent":
       event["payload"]["action"]