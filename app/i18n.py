from dataclasses import dataclass

import streamlit as st


@dataclass
class Dictionary:
    app_title: str = 'Public transport to Swiss mountains'
    menu_language: str = 'Language'
    menu_starting_location: str = 'Starting location'
    menu_min_altitude: str = 'Min altitude'
    menu_max_altitude: str = 'Max altitude'
    menu_max_duration: str = 'Max transport duration'
    tooltip_stop: str = 'Stop'
    tooltip_altitude: str = 'Altitude'
    tooltip_duration: str = 'Duration'
    app_introduction: str = """
Public transport to Swiss Mountains is a personal project initiated in 2023
with the aim of promoting the use of public transportation for mountain sports
in Switzerland. Its primary objective is to provide information about the most
efficient routes via public transportation to reach various altitudes in
Switzerland. This project is designed to assist users in discovering new
destinations for snow sports or simply finding an enjoyable spots with
breathtaking views and fresh air atop Switzerland mountains,
all while promoting environmental preservation.

The displayed transport duration corresponds to the fastest travel found
among the first three connections on the morning of the following day. Due to
the associated computational costs, the schedules are not updated daily.
Therefore, the displayed transport durations should be considered indicative,
and the validity of a proposed destination must be verified before travel.
"""

def get_i18n_strings() -> Dictionary:
    """Get i18n strings

    Returns:
        Dictionary
    """
    if 'language_sel' not in st.session_state:
        return LANG['en']
    else:
        return LANG[st.session_state['language_sel']]

LANG = dict()

LANG['en'] = Dictionary()

LANG['fr'] = Dictionary(
    app_title='En TP à la montagne',
    menu_language='Langue',
    menu_starting_location='Lieu de départ',
    menu_min_altitude='Altitude minimale',
    menu_max_altitude='Altitude maximale',
    menu_max_duration='Durée maximale du trajet',
    tooltip_stop='Arrêt',
    tooltip_altitude='Altitude',
    tooltip_duration='Durée',
    app_introduction="""
En TP à la montagne est un projet personnel initié en 2023 dans le but de
promouvoir l'utilisation des transports publics pour les sports de montagne
en Suisse. Son objectif principal est de fournir des informations sur les
itinéraires les plus efficaces avec les transports en commun pour atteindre
différentes altitudes en Suisse. Ce projet est conçu pour aider les
utilisateurs à découvrir de nouvelles destinations pour les sports de neige ou
simplement trouver des endroits intéressants avec un peu d'air frais et un
décor inoubliable au sommet des montagnes suisses, tout en limitant l'impact
des trajets sur l'environnement.

La durée de transport affichée correspond au voyage le plus rapide trouvé parmi
les trois premières connexions du matin du jour suivant.
En raison des coûts de calcul associés, les horaires ne sont pas mis à jour
tous les jours. Par conséquent, les durées de transport affichées doivent être
considérées comme indicatives, et la validité d'une destination proposée doit
être vérifiée avant le voyage.
"""
)

LANG['de'] = Dictionary(
    app_title='Mit ÖV in die Schweizer Berge',
    menu_language='Sprache',
    menu_starting_location='Startpunkt',
    menu_min_altitude='Minimale Höhe',
    menu_max_altitude='Maximale Höhe',
    menu_max_duration='Maximale Transportdauer',
    tooltip_stop='Haltestelle',
    tooltip_altitude='Höhe',
    tooltip_duration='Dauer',
    app_introduction="""
Mit ÖV in die Schweizer Berge ist ein persönliches Projekt, das im Jahr 2023
gestartet wurde, um die Nutzung öffentlicher Verkehrsmittel für den
Bergsport in der Schweiz zu fördern. Das Hauptziel ist es, Informationen über
die effizientesten Routen mit öffentlichen Verkehrsmitteln zu verschiedenen
Höhen in der Schweiz bereitzustellen. Dieses Projekt soll den Nutzern helfen,
neue Ziele für Wintersportarten zu entdecken oder einfach nur interessante Orte
mit etwas frischer Luft und unvergesslicher Aussicht auf den Gipfeln der
Schweizer Berge zu finden, und dabei die Umweltbelastung der Reisen zu minimieren.

Die angezeigte Transportdauer entspricht der schnellsten Verbindung, die unter
den ersten drei Verbindungen am Morgen des folgenden Tages gefunden wurde.
Aufgrund der damit verbundenen Rechenkosten werden die Fahrpläne noch nicht
täglich aktualisiert. Daher sollten die angezeigten Transportdauern als
indikativ betrachtet werden, und die Gültigkeit eines vorgeschlagenen
Reiseziels muss vor der Reise überprüft werden.
"""
)