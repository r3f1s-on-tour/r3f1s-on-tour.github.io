---
nummer: "612"
startLatitude: ""
startLongitude: ""
titel: "Marx is calling you - Berlin"
picture: "https://api.bannergress.com/bnrs/pictures/b4febc4fc81e9a74a0a8f4477b56ed56"
region: "Berlin"
country: "Deutschland"
completed: "13.416"
missions: "6"
date: "2025"
bg-link: "https://bannergress.com/banner/marx-is-calling-you-berlin-6c02"
onyx: "0"
description: ""
lengthKMeters: ""
umap: ""
title: "Marx is calling you - Berlin"
---

# {{ page.meta.title }}
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

