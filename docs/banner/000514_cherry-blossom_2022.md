---
nummer: "514"
startLatitude: "50,741751"
startLongitude: "7,095997"
titel: "Cherry Blossom"
picture: "https://api.bannergress.com/bnrs/pictures/e9952cd06db29653926eedd0a0c39360"
region: "Bonn"
country: "Deutschland"
completed: "10.944"
missions: "24"
date: "2022"
bg-link: "https://bannergress.com/banner/cherry-blossom-7cc3"
onyx: "0"
description: "Welcome to Bonn! Have a great time and enjoy the Cherry Blossom."
lengthKMeters: "5,954"
umap: ""
title: "Cherry Blossom"
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

