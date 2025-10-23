---
nummer: "45"
startLatitude: "48.146732"
startLongitude: "11.563926"
titel: "Blauer Reiter Tour"
picture: "https://api.bannergress.com/bnrs/pictures/0d330415cd7568296591257b578f2bff"
region: "München"
country: "Deutschland"
completed: "1026"
missions: "48"
date: "2016"
bg-link: "https://bannergress.com/banner/blauer-reiter-tour-9d18"
onyx: "1"
description: "Wünsche viel Spaß beim Spielen beim 48 Mosaik des Blauen Reiters. \n\nErschaffen hat den Blauen Reiter Franz Marc (1880 – 1916), wo man das Original im Lenbachhaus anschauen kann."
lengthKMeters: "17,08"
umap: ""
title: "Blauer Reiter Tour"
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
