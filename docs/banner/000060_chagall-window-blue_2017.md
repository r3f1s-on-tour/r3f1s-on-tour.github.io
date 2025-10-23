---
nummer: "60"
startLatitude: "47.36981"
startLongitude: "8.541585"
titel: "Chagall Window blue"
picture: "https://api.bannergress.com/bnrs/pictures/ea8abd6fbee2c76131fb4a97016de779"
region: "Zürich"
country: "Schweiz/Suisse/Svizzera/Svizra"
completed: "1350"
missions: "6"
date: "2017"
bg-link: "https://bannergress.com/banner/chagall-window-blue-8212"
onyx: "0"
description: "The beautiful windows made by Marc Chagall in 1970 belong to the modern, yet classic cultural heritage of Zurich and bring many tourists to Fraumünster.\n\nOptimal starting point for all three windows"
lengthKMeters: "1,74"
umap: ""
title: "Chagall Window blue"
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
