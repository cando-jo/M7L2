#pgzero
import random

# Pencerenin Çizimi
hucre = Actor("sınır")
hucre1 = Actor("zemin")
hucre2 = Actor("çatlak")
hucre3 = Actor("kemikler")
ekran_g = 9 # Ekranın enindeki hücre sayısı
ekran_y = 10 # Ekranın boyundaki hücre sayısı
WIDTH = hucre.width * ekran_g
HEIGHT = hucre.height * ekran_y
dusmanlar, kalpler, kiliclar = [], [], []

for i in range(5):
    x = random.randint(2, 7) * 50
    y = random.randint(2, 7) * 50
    dusman = Actor("düşman", topleft = (x, y))
    dusmanlar.append(dusman)
    dusman.saldiri = random.randint(5, 10)
    dusman.saglik = random.randint(10, 20)
    dusman.bonus = random.randint(0, 2)
    
TITLE = "Zindanlar" # Oyunun Adı
FPS = 30 # Saniyedeki Kare Sayısı
haritam = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 1, 1, 2, 1, 3, 1, 1, 0], 
          [0, 1, 1, 1, 2, 1, 1, 1, 0], 
          [0, 1, 3, 2, 1, 1, 3, 1, 0], 
          [0, 1, 1, 1, 1, 3, 1, 1, 0], 
          [0, 1, 1, 3, 1, 1, 2, 1, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1]] # Hücüm Gücü ve Sağlık bilgisi

# Başrol Karakteri
karakter = Actor('karakter')
karakter.health = 100
karakter.attack = 5
karakter.top = hucre.height
karakter.left = hucre.width

def carpismalar(eski_pos):

    dusman_sira = karakter.collidelist(dusmanlar)
    if dusman_sira != -1:
        karakter.pos = eski_pos
        dusman = dusmanlar[dusman_sira]
        dusman.saglik -= karakter.attack
        karakter.health -= dusman.saldiri
        if (dusman.saglik <= 0):
            if dusman.bonus == 1:
                kalp = Actor('kalp', (dusman.x, dusman.y))
                kalpler.append(kalp)
            elif dusman.bonus == 2:
                kilic = Actor('kılıç', (dusman.x, dusman.y))
                kiliclar.append(kilic)
                
            dusmanlar.pop(dusman_sira)
            
        if karakter.health <= 0:
            exit()

    
def harita_cizim():
    for i in range(len(haritam)):
        for j in range(len(haritam[0])):
            if haritam[i][j] == 0:
                hucre.left = hucre.width*j
                hucre.top = hucre.height*i
                hucre.draw()
            elif haritam[i][j] == 1:
                hucre1.left = hucre.width*j
                hucre1.top = hucre.height*i
                hucre1.draw()
            elif haritam[i][j] == 2:
                hucre2.left = hucre.width*j
                hucre2.top = hucre.height*i
                hucre2.draw()  
            elif haritam[i][j] == 3:
                hucre3.left = hucre.width*j
                hucre3.top = hucre.height*i
                hucre3.draw() 

def draw():
    screen.fill("#2f3542")
    harita_cizim()
    for i in range(len(dusmanlar)):
        dusmanlar[i].draw()

    for i in range(len(kalpler)):
        kalpler[i].draw()

    for i in range(len(kiliclar)):
        kiliclar[i].draw()
        
    karakter.draw()
    screen.draw.text("Sağlık:", center=(35, 475), color = 'white', fontsize = 20)
    screen.draw.text(karakter.health, center=(85, 475), color = 'white', fontsize = 20)
    screen.draw.text("Hücum:", center=(375, 475), color = 'white', fontsize = 20)
    screen.draw.text(karakter.attack, center=(425, 475), color = 'white', fontsize = 20)

def on_key_down(key):
    eski_pos = karakter.pos
    if keyboard.right and karakter.x + hucre.width < WIDTH - hucre.width:
        karakter.x += hucre.width
        karakter.image = 'karakter'
    elif keyboard.left and karakter.x - hucre.width > hucre.width:
        karakter.x -= hucre.width
        karakter.image = 'sol'
    elif keyboard.down and karakter.y + hucre.height < HEIGHT - hucre.height*2:
        karakter.y += hucre.height
    elif keyboard.up and karakter.y - hucre.height > hucre.height:
        karakter.y -= hucre.height

    carpismalar(eski_pos)
