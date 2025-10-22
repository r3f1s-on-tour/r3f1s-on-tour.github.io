---
nummer: "434"
startLatitude: "53,429481"
startLongitude: "14,553038"
titel: "Biocard Szczecin"
picture: "https://api.bannergress.com/bnrs/pictures/20a058074b53019498efad8705ff63fd"
region: "Szczecin"
country: "Polska"
completed: "9.072"
missions: "48"
date: "2022"
bg-link: "https://bannergress.com/banner/biocard-szczecin-0805"
onyx: "0"
description: "Welcome to Szczecin! This banner will lead you through the city's most famous highlights. Complete it to earn a biocard depicting the statue of the Seaman."
lengthKMeters: "18,62"
umap: ""
title: "Biocard Szczecin"
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

