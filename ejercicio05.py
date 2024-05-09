import requests

with open("frases.csv", "r", encoding="utf8") as archivo:
    frases = archivo.readlines()

for linea in frases:
    #print(linea)
    r = requests.get("http://127.0.0.1:8080/prediccion/'%s'" % linea)
    print(f'La frase:{linea} es: {r.json()['prediction']}')
