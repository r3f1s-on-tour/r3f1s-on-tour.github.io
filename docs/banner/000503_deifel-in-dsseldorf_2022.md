---
nummer: "503"
startLatitude: "51,220016"
startLongitude: "6,79448"
titel: "Deifel in Düsseldorf"
picture: "https://api.bannergress.com/bnrs/pictures/077dbe7f5a8f89090241712c3eec4522"
region: "Düsseldorf"
country: "Deutschland"
completed: "10.752"
missions: "6"
date: "2022"
bg-link: "https://bannergress.com/banner/deifel-in-d%C3%BCsseldorf-0642"
onyx: "0"
description: "Starte am Hauptbahnhof einen Rundgang und entdecke Düsseldorf. Auf deinem Abenteuer entdeckst du Sehenswürdigkeiten und historische Orte. Die Runde endet wieder am Hauptbahnhof"
lengthKMeters: "4"
umap: ""
title: "Deifel in Düsseldorf"
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
