---
nummer: "15"
startLatitude: "53.545576"
startLongitude: "9.970032"
titel: "Landungsbrücken"
picture: "https://api.bannergress.com/bnrs/pictures/b5b4e97a8c42aca70facc47acb35a5ca"
region: "Hamburg"
country: "Deutschland"
completed: "294"
missions: "18"
date: "2015"
bg-link: "https://bannergress.com/banner/landungsbr%C3%BCcken-mosaik-5dad"
onyx: "0"
description: "Mosaic around the Landungsbrücken"
lengthKMeters: "5,87"
umap: ""
title: "Landungsbrücken"
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

