---
nummer: "59"
startLatitude: "47.374226"
startLongitude: "8.542888"
titel: "MissionDay Zürich"
picture: "https://api.bannergress.com/bnrs/pictures/60989b4a7ea4e993c9d23756812cb691"
region: "Zürich"
country: "Schweiz/Suisse/Svizzera/Svizra"
completed: "1344"
missions: "24"
date: "2017"
bg-link: "https://bannergress.com/banner/md-z%C3%BCrich-32cc"
onyx: "0"
description: ""
lengthKMeters: "20,03"
umap: ""
title: "MissionDay Zürich"
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
- **lengthKMeters**: {{ page.meta.lengthKMeters }}

