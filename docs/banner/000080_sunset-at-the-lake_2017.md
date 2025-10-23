---
nummer: "80"
startLatitude: "48.077323"
startLongitude: "11.251291"
titel: "Sunset at the lake"
picture: "https://api.bannergress.com/bnrs/pictures/e3e494a190ecc79e317bf49128248159"
region: "Oberpfaffenhofen"
country: "Deutschland"
completed: "2142"
missions: "12"
date: "2017"
bg-link: "https://bannergress.com/banner/sunset-at-the-lake-8330"
onyx: "0"
description: "Erkunde den Wesslinger See und mache ein schönes Bild mit Sonnenuntergang am See. Die Missionsreihe besteht aus zwei Runden um den Wesslinger See- Hack&Capture und Link&Field. Endportal = Startportal."
lengthKMeters: "6,25"
umap: ""
title: "Sunset at the lake"
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
