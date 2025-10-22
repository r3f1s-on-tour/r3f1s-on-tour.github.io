---
nummer: "511"
startLatitude: "50,732038"
startLongitude: "7,097646"
titel: "Deifel in Bonn"
picture: "https://api.bannergress.com/bnrs/pictures/6666727754e8e2f93c7b7453c6529c6f"
region: "Bonn"
country: "Deutschland"
completed: "10.884"
missions: "6"
date: "2022"
bg-link: "https://bannergress.com/banner/deifel-in-bonn-c2e4"
onyx: "0"
description: "Starte am Hauptbahnhof einen Rundgang und entdecke Wuppertal. Auf deinem Abenteuer entdeckst du Sehenswürdigkeiten und historische Orte. Die Runde endet wieder am Hauptbahnhof"
lengthKMeters: "3"
title: "Deifel in Bonn"
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

