---
nummer: '1'
startLatitude: '54.077793'
startLongitude: '12.129966'
titel: Rostocker Flagge
picture: https://lh3.googleusercontent.com/pw/AP1GczNZfmWJMlnG4IgP3QqtGnTgM4sx0qr9gu6y91N6J9zXIHbc3TdoB2ZleBNZ6HAPN43hoZFSr1m308E1sJP_NLIInCJy7p9q-dTx0TNiId-X9OsJnubD1ZRioYCEF7Hu1m7U9PtdyKV3uZQKAa17q2qQYQ
region: Rostock
country: Deutschland
completed: '96'
missions: '24'
date: '2015'
bg-link: https://bannergress.com/banner/rostocker-flagge-9920
onyx: '0'
description: 'Erkunde ab hier die wunderschöne Hansestadt Rostock mit Ihren Sehenswürdigkeiten.

  Beginne mit dem Bahnhof als zentralen Anlaufpunkt.

  PS- Es sollte das Fahrrad genutzt werden.'
lengthKMeters: 12,84
title: Rostocker Flagge
tg_posted: true
---
# {{ page.meta.title }}
_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

## Bild
![{{ page.meta.title | default('Bild') }}]({{ page.meta.picture }})

## Links
- **bg-link**: [{{ page.meta['bg-link'] }}]({{ page.meta['bg-link'] }})

## Infos
- **nummer**: {{ page.meta.nummer }}
- **startLatitude**: {{ page.meta.startLatitude }}
- **startLongitude**: {{ page.meta.startLongitude }}
- **region**: {{ page.meta.region }}
- **country**: {{ page.meta.country }}
- **completed**: {{ page.meta.completed }}
- **missions**: {{ page.meta.missions }}
- **onyx**: {{ page.meta.onyx }}
- **description**: {{ page.meta.description }}
- **lengthKMeters**: {{ page.meta.lengthKMeters }}

