---
nummer: "610"
startLatitude: "53.561265"
startLongitude: "13.259266"
titel: "Playing Frogs NB"
picture: "https://api.bannergress.com/bnrs/pictures/38c1dd490e87d10690357af83dccbb59"
region: "Neubrandenburg"
country: "Deutschland"
completed: "13.362"
missions: "24"
date: "2025"
bg-link: "https://bannergress.com/banner/playing-frogs-nb-2fed"
onyx: "0"
description: "Diese Missionen führen entlang des Strandbads Brodas und dem Kulturpark von Neubrandenburg. Entdecke dabei auch die zahlreichen Skulpturen im Kulturpark."
lengthKMeters: "6,965"
title: "Playing Frogs NB"
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

