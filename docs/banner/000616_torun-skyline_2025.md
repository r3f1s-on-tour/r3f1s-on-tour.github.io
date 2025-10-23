---
nummer: "616"
startLatitude: ""
startLongitude: ""
titel: "Torun skyline"
picture: "https://api.bannergress.com/bnrs/pictures/d1413bb121e5d1d037822169d6c692b5"
region: "Torun"
country: "Polska"
completed: "13.470"
missions: "18"
date: "2025"
bg-link: "https://bannergress.com/banner/torun-skyline-15f3"
onyx: "0"
description: ""
lengthKMeters: "3,7"
umap: ""
title: "Torun skyline"
---
# {{ page.meta.title | default('Untitled') }}

_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

## Bild
![{{ page.meta.title | default('Bild') }}]({{ page.meta.picture }})

## Links
- **bg-link**: [{{ page.meta['bg-link'] }}]({{ page.meta['bg-link'] }})

## Infos
- **nummer**: {{ page.meta.nummer }}
- **region**: {{ page.meta.region }}
- **country**: {{ page.meta.country }}
- **completed**: {{ page.meta.completed }}
- **missions**: {{ page.meta.missions }}
- **onyx**: {{ page.meta.onyx }}
- **lengthKMeters**: {{ page.meta.lengthKMeters }}
