# -*- coding: utf-8 -*-

import pyttsx3
import random

words_data = {
    'der': {
        'Hund': {'turkish_meaning': 'köpek'},
        'Tisch': {'turkish_meaning': 'masa'},
        'Stuhl': {'turkish_meaning': 'sandalye'},
        'Apfel': {'turkish_meaning': 'elma'},
        'Mann': {'turkish_meaning': 'adam'},
        'Frau': {'turkish_meaning': 'kadın'},
        'Himmel': {'turkish_meaning': 'gökyüzü'},
        'Mond': {'turkish_meaning': 'ay'},
        'Wald': {'turkish_meaning': 'orman'},
        'Berg': {'turkish_meaning': 'dağ'},
        'Fluss': {'turkish_meaning': 'nehir'},
        'See': {'turkish_meaning': 'göl'},
        'Haus': {'turkish_meaning': 'ev'},
        'Fenster': {'turkish_meaning': 'pencere'},
        'Tür': {'turkish_meaning': 'kapı'}
    },
    'die': {
        'Katze': {'turkish_meaning': 'kedi'},
        'Blume': {'turkish_meaning': 'çiçek'},
        'Frau': {'turkish_meaning': 'kadın'},
        'Ente': {'turkish_meaning': 'ördek'},
        'Schule': {'turkish_meaning': 'okul'},
        'Universität': {'turkish_meaning': 'üniversite'},
        'Stadt': {'turkish_meaning': 'şehir'},
        'Land': {'turkish_meaning': 'ülke'},
        'Sprache': {'turkish_meaning': 'dil'},
        'Musik': {'turkish_meaning': 'müzik'},
        'Blatt': {'turkish_meaning': 'yaprak'},
        'Straße': {'turkish_meaning': 'cadde'},
        'Zeitung': {'turkish_meaning': 'gazete'},
        'Zeitschrift': {'turkish_meaning': 'dergi'}
    },
    'das': {
        'Buch': {'turkish_meaning': 'kitap'},
        'Haus': {'turkish_meaning': 'ev'},
        'Kind': {'turkish_meaning': 'çocuk'},
        'Auto': {'turkish_meaning': 'araba'},
        'Geld': {'turkish_meaning': 'para'},
        'Telefon': {'turkish_meaning': 'telefon'},
        'Fahrrad': {'turkish_meaning': 'bisiklet'},
        'Boot': {'turkish_meaning': 'tekne'},
        'Uhr': {'turkish_meaning': 'saat'},
        'Radio': {'turkish_meaning': 'radyo'},
        'Fernsehen': {'turkish_meaning': 'televizyon'},
        'Computer': {'turkish_meaning': 'bilgisayar'},
        'Hemd': {'turkish_meaning': 'gömlek'},
        'Mantel': {'turkish_meaning': 'palto'},
        'Kleid': {'turkish_meaning': 'elbise'}
    }
}
engine = pyttsx3.init()

def speak(word):
    engine.say(word)
    engine.runAndWait()



def practice_articles():
    while True:
        article = random.choice(list(words_data.keys()))
        german_word, word_data = random.choice(list(words_data[article].items()))
        turkish_meaning = word_data['turkish_meaning']
        print('Please Type "quit" to end the program')
        user_input = raw_input("Please enter the correct article for '{}': ".format(german_word)).strip().lower()
        
        if user_input == article:
            print("Correct! '{}' means '{}' in Turkish.".format(german_word, turkish_meaning))
        elif user_input == 'quit':
            print('Take care!')
            break
        else:
            print("Wrong! The correct article for '{}' is '{}'. '{}' means '{}' in Turkish.".format(
                german_word, article, german_word, turkish_meaning))
        

if __name__ == "__main__":
    print("Welcome to German articles practice!")
    practice_articles()
