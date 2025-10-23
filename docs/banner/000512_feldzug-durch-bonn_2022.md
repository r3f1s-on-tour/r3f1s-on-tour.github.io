---
nummer: "512"
startLatitude: "50,732331"
startLongitude: "7,097059"
titel: "Feldzug durch Bonn"
picture: "https://api.bannergress.com/bnrs/pictures/930e8b5b12515495725c0e0d4fcac97a"
region: "Bonn"
country: "Deutschland"
completed: "10.902"
missions: "18"
date: "2022"
bg-link: "https://bannergress.com/banner/feldzug-durch-bonn-8bf0"
onyx: "0"
description: "Diese Missionsreihe führt durch Bonn. Vom Hauptbahnhof über den alten Friedhof und wieder zurück."
lengthKMeters: "3,806"
umap: ""
title: "Feldzug durch Bonn"
---
# {{ page.meta.title | default('Untitled') }}

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
