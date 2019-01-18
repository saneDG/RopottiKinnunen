# Ropotti Kinnunen created by Santeri Pigg 09/2018
# Ropotti Kinnunen on ropotti joka kertoo Kinnusista sekä kunnasta itsestään täyttä factaa.

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from urllib.request import Request, urlopen
from lxml import html
import random
import datetime
import youtube_dl
import requests

Client = discord.Client()
client = commands.Bot(command_prefix = '!')

print("alku")


# KOMMENTTI MIIKALLE!!! #

# 1. Lataa Python: https://www.python.org/ftp/python/3.3.7/Python-3.3.7.tgz.asc Ohjeet asennukseen: https://realpython.com/installing-python/
# 2. Avaa cmd -> kirjoita cmd konsoliin:
#   2.1 python3 -m pip install -U discord.py[voice] -> ENTER
#   2.2 py -m pip install urllib -> ENTER
#   2.3 pip install asyncio -> ENTER
#   2.4 pip install lxml -> ENTER
#   2.5 python -m pip install -U youtube_dl -> ENTER
#   2.6 lataa youtube_dl: https://ffmpeg.zeranoe.com/builds/win64/static/ffmpeg-20181218-3a36b0c-win64-static.zip -> nimeä ladattu kansio "ffmpeg" -> siirrä nimetty kansio C: aseman juureen
#       tutoriaali asennukseen: https://youtu.be/MbhXIddT2YY?t=101 

# Kun asennukset on hoidettu niin botin pitäisi toimia

# Allaolevaan muuttujaan (luukkuauki = ...) tulee linkki 
# esim luukkuauki = ..., "linkki" + "_tekstiä", "21" + "21", ...] 
# muista välilyönti ennen tekstiä! 
# älä muokkaa mielellään muuta koodia 
luukkuauki = ['null', 'https://i.ytimg.com/vi/e2K2mMRJVtY/maxresdefault.jpg' + " Niilopukki!", 'https://cdn.ksml.fi/incoming/90sndt-KINNULAA.jpg/ALTERNATES/FREE_1140/KINNULAA.jpg' + " Vanha tuttu Juha Urpilainen luonnollisessa ympäristössään eli viemässä kinnusten rahoja", "https://i.ylilauta.org/ba/86a014ea.jpg" + " Norttimies", "https://www.kansanuutiset.fi/images/2002941-759x500.jpg" + " Kulttuuria Kinnulasta", "https://www.stara.fi/wp-content/uploads/2015/03/poliisiauto08032015.jpg" + " Poliisit Kinnulassa",  "http://i2.wp.com/listverse.com/wp-content/uploads/2009/11/simo_hayha-s585x360-11707.jpg" + " __**Simo Häyhä**__" + " Tämän päivän luukku on siitä erityinen että tänään on Suomen itsenäisyyspäivä. Erityisen päivästä tekee myös se, kun **1. menet ensin äänikanavalle** -> **2. kirjoita chattiin** ***'hyvää itsenäisyyspäivää!'*** saat ennenkuulumattoman itsenäisyyspäivän kokemuksen!", "https://i.4pcdn.org/sp/1463511420482.png" + " Bulju", "https://fi-seiska-cdn-pro.seiska.fi/files/styles/article_page_image_770px_wide/s3/2018-12/pk_keke_ilman_paitaa_lehtikuva.jpg?itok=sKg8afPT" + " Keke Rosberg", "https://www.punanaamio.fi/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/2/5/25912-koira-naamiaisasu.jpg" + " pehmeä koira naamiais asu", "https://t.ylilauta.org/6d/4617086f.jpg" + " allu", "11" + "11", "https://gyazo.com/13d6187970c26723f6dcd6c8fb3b79f8" + " Etelän matkailija Miika Kinnuen", "https://gyazo.com/3108f6529950d9293cd5a2239f00b1a9" + " Mäk Elmeri69 sekä Mr. Worldwide aka Märkä Siili", "https://gyazo.com/88065a351d1b3aa18c9aed9e1238c548" + " Janin teltta", "https://gyazo.com/43e23176a615ec5dda3f4c22e0d128d4" + " Miika kinnunen", "https://gyazo.com/d5c869d3f7fd888a877514ac5927caae" + " Urbaania menoa ja meininkiä kinnulan teollisuusalueelta", "https://media.riemurasia.net/albumit/mmedia/fq/524/trwd/139511/1115862124.jpg" + " Joulupukki pajalla valmistautumassa aattoon", "https://1drv.ms/u/s!ArvOpRSpS8mq5jfTGYGPkMzttRmm" + " Vihainen mies", "Moti meni" + "", "20" + "20", "21" + "21", "22" + "22", "23" + "23", "24" + "24"]

@client.event
async def on_ready():
    print("Ropotti on linjoilla")
    # client.loop.run_until_complete(client.logout())

players = {}

@client.event
async def on_message(message):
    # komento käyttäjältä botille

    if message.content == "tämä riittää":
        server = message.server
        voice_client = client.voice_client_in(server)
        await voice_client.disconnect()

    if message.content == "hyvää itsenäisyyspäivää!":
        channel = message.author.voice.voice_channel
        await client.join_voice_channel(channel)
        server = message.server
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player("https://youtu.be/4DUpIhG0VsE")
        players[server.id] = player
        player.start()
        await client.send_message(message.channel, "```" + "Olen juuri liittynyt äänikanavalle Suomen itsenäisyyden kunniaksi. Tule kuuntelemaan kanssani isänmaallista musiikkia. Hyvää itsenäisyyspäivää kaikille kinnusille! Saat musiikin suljettua kirjoittamalla tekstikenttään 'tämä riittää'" + "```")
        await client.send_message(message.channel, "http://bestanimations.com/Flags/Europe/Western/Scandinavia/finland/finland-flag-waving-animated-gif-3.gif")

    if message.content == "mikä röyhkeys!!":
        channel = message.author.voice.voice_channel
        await client.join_voice_channel(channel)
        server = message.server
        voice_client = client.voice_client_in(server)
        player = await voice_client.create_ytdl_player("https://youtu.be/nO7yRpwNiqg")
        players[server.id] = player
        player.start()

    if message.content == "!ilimojapielly":
        url = "http://www.motot.net/saa/ennuste/Kinnula/"
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
        req = Request(url, headers=header)
        openlink = urlopen(req)
        parsed_page = html.parse(openlink)
        openlink.close()
        extracted_paragragraphs1 = parsed_page.xpath("//span[@class='lampotilaKorkein']")
        plain_paragraphs = []
        easy_to_read = []

        for every_coded_paragraph in extracted_paragragraphs1:
            decode_paragraph = every_coded_paragraph.text_content()
            plain_paragraphs.append(decode_paragraph)
            easy_to_read = '  ►'.join(plain_paragraphs)

        await client.send_message(message.channel, "Seuraavan viien päivän seä Kinnulassa: " + "``` ►" + easy_to_read + "```")
        print(easy_to_read)

    if message.content == "onko polliisit kinnulassa?":
        alueMissa = ['Muholassa ', 'Hiilingillä ', 'Leean rillillä ', 'Teollisuus alueella ', 'Kylällä ', 'Sellinsuoralla ', 'Perhon tiellä ', 'Kangaskylällä ', 'Kinnuskeskuksella ', 'Uimalaitoksella ', 'Lukkarin rannassa ']
        poliisiMika = ['siviili auto ', 'pillit päällä ', 'rososta kuulustelevat ', 'ojjaan ajovat ', 'pyssyt paukkuen ']
        alueMinne = ['muholaan päin menossa ', 'hiilingille menossa ', 'perhoon päin menossa ', 'ajavat ', 'lintassa männöö ', ' ', ' ', ' ', ' ']
        loppu = ['varmaa leksaa toas hakevat :joy:', ':joy: ', ':joy: ', ':joy: ', ':joy: ', ':joy: ', '', ':joy: ']
        await client.send_message(message.channel, "ON! " + (random.choice(alueMissa)) + (random.choice(poliisiMika)) + (random.choice(alueMinne)) + (random.choice(loppu)))
        print("Kytät!")

    if message.content == "!toikkane":
        await client.send_message(message.channel, "https://youtu.be/KrVC5dm5fFc?t=45")
        print("Toikkanen kuittaa")

    if message.content == "kuka vei kinnusten rahat?":
        await client.send_message(message.channel, "Minä. T. Juha Urpilainen")
        await client.send_message(message.channel, "https://www.suomenmaa.fi/image-3.179688.22e38ea0e3?size=1024")
        print("Juha Urpilainen Huutaa")

    if message.content == "!kinnulafakt":
        fakta = ['Kinnula on sudeettialue Keski-Suomen maakunnan luoteisimmassa kulmassa. Kulttuurillisesti ja osittain maantieteellisesti skitsofreeninen Kinnula kuuluu Savoon, Pohjanmaahan sekä jotenkin mystisesti Hämeeseen. ', 
        'Kinnula edustaa pääsääntöisesti kolmannen luokan kunnallistekniikkaa, mutta tiet ovat tarkoituksellisesti huonokuntoiset, jotta maaltapako voitaisiin tehokkaasti estää. Tässä on Kinnulankin osalta epäonnistuttu surkeasti. Kinnulaa kutsutaan Keski-Suomen Galliaksi, sillä tänä kuntaliitosten aikana kunta haluaa pitää kynsin hampain kiinni itsenäisyydestään.', 
        'Yli puolet Kinnulan tulonsaajista on maansiirtourakoitsijoita. Toinen puoli on maanviljelijöitä, joiden sivutulot tulevat maansiirtotöistä. Kinnulassa onkin siirretty maata paikasta toiseen enemmän kuin missään koko telluksella.', 
        'Kinnulassa on enemmän kevyen liikenteen väyliä asukasta kohden kuin missään muualla maailmassa. Tämä tosin johtuu kunnan alati pienenevästä väkiluvusta ja edelleen kasvavasta kevyen liikenteen väylien lukumäärästä.', 
        'Kinnulassa on täysin mahdotonta pitää hauskaa joutumatta tappeluun.', 'Väärässä paikassa nauraminen voi olla Kinnulassa fyysiseen edesvastuuseen johtava rike.', 
        'Valtaosa Kinnulan väestöstä on vanhoillislestadiolaisia, joten ikävän pitämisellä on vahvat ja juonikkaat perinteet.', 
        'Kinnula onkin monissa yhteyksissä mainittu Suomen uskovaisimmaksi kunnaksi, kirkollisvaalien äänestysaktiivisuuden ollessa ylivoimaisesti maan korkein, jopa toistasataa prosenttia.', 
        'Luonteenomainen piirre kinnulalaisissa ihmisissä on kateus ja paskanpuhuminen. Myös pahansuopaisia liikanimiä jaetaan Kinnulassa ihmisille herkästi.', 
        'Kinnulan entinen kunnanjohtaja yritti väkisinkin tehdä tästä alle 2000 asukkaan kylästä kaupunkia 1990-luvulla, ja hankkeen kariuduttua kaivoi roskiksesta esiin vanhan kauppala-käsitteen ja ajoi Kinnulasta kauppalaa.', 
        'Joka kesä järjestettävät Kinnula-päivät tarjoavat erilaisia tapahtumia, kuten Kinnulan vahvin juoppo. ', 
        '"Rieska ei oo leipeä eikä kinnuset ihmisiä", "Pohjalta paranoo ku kinnusten piimä", "Kinnulasta on kirvesheitto helvettiin", "Ei saa päästää hyviä geenejä Kinnulan rajojen ulkopuolelle" ja "Mitä serkumpi, sitä herkumpi" ovat kuuluisia kinnulalaisia sanontoja.']
        await client.send_message(message.channel, "Fakta: " + "```" + (random.choice(fakta)) + "```")
        print("Täyttä faktaa")

    if message.content == "!joulukalenteri":
        await client.send_message(message.channel, "```" + "Tämä on Ropotti Kinnusen joulukelenteri. Voit tarkastaa onko tämän päivän luukku vielä avattu komennolla: !tarkastaluukku. Hyvveä joulua kaikille kinnusille!!!" + "```")
        print("joulukalenteri")

    if message.content == "!tarkastaluukku":
        with open('D:\coding\RopottiKinnunen\kalenteriarvot.txt', 'r') as kalenterifile:
            luku = kalenterifile.read()
            x = datetime.datetime.now()
            pvm = x.strftime("%#d")
            luukku = luukkuauki[int(luku)]
            print("päivämäärä: " + pvm + " luku filessä: " + luku)
            if pvm > luku:
                await client.send_message(message.channel, pvm + ". luukku ei ole vielä auki. Avaa luukku komennolla: '!avaaluukku'")
            if pvm <= luku:
                await client.send_message(message.channel, pvm + ". Luukku on jo auki. Luukusta paljastui tänään...")
                await client.send_message(message.channel, luukkuauki[int(pvm)])

    if message.content == "!avaaluukku":
        with open('D:\coding\RopottiKinnunen\kalenteriarvot.txt', 'r') as kalenteriread:
            luku = kalenteriread.read()
            x = datetime.datetime.now()
            pvm = x.strftime("%#d")
            uusiluku = pvm
            luukku = luukkuauki[int(luku)]
            if pvm > luku:
                with open('D:\coding\RopottiKinnunen\kalenteriarvot.txt', 'w') as kalenteriwrite:
                    kalenteriwrite.write(uusiluku)
                await client.send_message(message.channel, "Luukusta numero " + pvm + " paljastuu...")
                await client.send_message(message.channel, luukkuauki[int(pvm)])
            if pvm <= luku:
                await client.send_message(message.channel, pvm + ". Luukku on jo auki. Luukusta paljastui tänään...")
                await client.send_message(message.channel, luukkuauki[int(pvm)])
                print(luku)
                        
    if message.content == "mitä sinä tiet?":
        await client.send_message(message.channel, "Komennot: " + "```" + "||| !ilimojapielly | onko polliisit kinnulassa? | !toikkane | kuka vei kinnusten rahat? | !kinnulafakt |||" + "```")
        print("Mitä sinä tiet?")

client.run("NDkyNzI5NjcwMDUyMzQ3OTA1.DoaqQw.i69PRqXdlb3eGkCm3M6zu5QJWMI")
