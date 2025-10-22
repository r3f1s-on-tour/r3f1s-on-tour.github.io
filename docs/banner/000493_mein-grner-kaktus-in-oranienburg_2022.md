---
nummer: "493"
startLatitude: "52,756491"
startLongitude: "13,245295"
titel: "Mein grüner Kaktus in Oranienburg"
picture: "https://api.bannergress.com/bnrs/pictures/8c94f3fbb77c8eef340b0ca8a9eda497"
region: "Oranienburg"
country: "Deutschland"
completed: "10.560"
missions: "18"
date: "2022"
bg-link: "https://bannergress.com/banner/mein-gr%C3%BCner-kaktus-in-oranienburg-fa23"
onyx: "0"
description: "Starte eine Runde durch Oranienburg. Die Tour beginnt in der Bernauer Straße"
lengthKMeters: "8"
umap: ""
title: "Mein grüner Kaktus in Oranienburg"
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

