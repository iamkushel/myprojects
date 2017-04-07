import random
import urllib.request

def download_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + '.jpg'
    urllib.request.urlretrieve(url,full_name)


download_image('https://media.licdn.com/mpr/mpr/shrinknp_400_400/AAEAAQAAAAAAAAfYAAAAJDBmYmJjYzhiLTRiYzEtNDE4Mi05ZTA1LWQ5YmYzM2M0M2Y3Mg.jpg')
