# -*- coding: utf-8 -*-

import random

articles = {'der': ['Hund', 'Tisch', 'Stuhl', 'Apfel', 'Mann', 'Berg', 'Wald', 'See', 'Bär', 'Weg',
                    'Schuh', 'Vogel', 'Bote', 'Fluss', 'Schrank', 'Boden', 'Sturm', 'Mond', 'Fisch', 'Sohn',
                    'Anzug', 'Schmetterling', 'Frosch', 'Blick', 'Turm', 'Himmel', 'Mond', 'Käse', 'Stuhl',
                    'Ball', 'Hut', 'Garten', 'Mensch', 'Koffer', 'Tiger', 'Zug', 'Vogel', 'Fuchs', 'Wolf',
                    'Park', 'Sohn', 'Zwerg', 'Schlüssel', 'Tiger', 'Mond', 'Kopf', 'Kuss', 'Stift'],
            'die': ['Katze', 'Blume', 'Frau', 'Ente', 'Mädchen', 'Gans', 'Stadt', 'Nacht', 'Insel', 'Schule',
                    'Bluse', 'Rose', 'Sonne', 'Maus', 'Bank', 'Milch', 'Eule', 'Nase', 'Rose', 'Straße',
                    'Hand', 'Ecke', 'Blume', 'Ente', 'Schwester', 'Mutter', 'Tasse', 'Flasche', 'Treppe',
                    'Bank', 'Küche', 'Tante', 'Tür', 'Bank', 'Wolke', 'Nacht', 'Ecke', 'Ente', 'Königin',
                    'Rose', 'Tafel', 'Wiese', 'Straße', 'Kirche', 'Freundin', 'Schule', 'Pflanze', 'Straße'],
            'das': ['Buch', 'Haus', 'Kind', 'Auto', 'Boot', 'Zimmer', 'Geld', 'Geschenk', 'Leben', 'Problem',
                    'Fenster', 'Licht', 'Telefon', 'Land', 'Schiff', 'Bett', 'Pferd', 'Rad', 'Wasser', 'Papier',
                    'Bild', 'Glas', 'Ei', 'Schloss', 'Schiff', 'Wasser', 'Hemd', 'Bett', 'Rad', 'Tier',
                    'Telefon', 'Brot', 'Dach', 'Gras', 'Ei', 'Feld', 'Feuer', 'Geld', 'Pferd', 'Gesicht',
                    'Kino', 'Glück', 'Haus', 'Kissen', 'Kopf', 'Papier', 'Problem', 'Land', 'Rad']}
                    
def practice_articles():
    while True:
        article = random.choice(list(articles.keys()))
        noun = random.choice(articles[article])

        user_input = raw_input('Please enter the correct article for "{}": '.format(noun)).strip().lower()

        if user_input == article:
            print("Correct!")
        else:
            print('Wrong! The correct article for "{}" is "{}".'.format(noun, article))


if __name__ == "__main__":
    print("Welcome to German articles practice!")
    practice_articles()
