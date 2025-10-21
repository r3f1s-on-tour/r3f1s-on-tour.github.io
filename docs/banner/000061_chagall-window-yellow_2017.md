---
nummer: "61"
startLatitude: "47.374777"
startLongitude: "8.537097"
titel: "Chagall Window yellow"
picture: "https://api.bannergress.com/bnrs/pictures/8611b3520266f1e355ead4be0fa96bec"
region: "Zürich"
country: "Schweiz/Suisse/Svizzera/Svizra"
completed: "1356"
missions: "6"
date: "2017"
bg-link: "https://bannergress.com/banner/chagall-window-yellow-b02b"
onyx: "0"
description: ""
lengthKMeters: "1,20"
title: "Chagall Window yellow"
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

