---
nummer: "53"
startLatitude: "48.150701"
startLongitude: "11.461687"
titel: "Pasinger Stadtwappen"
picture: "https://api.bannergress.com/bnrs/pictures/fd818caf54ddf0a3b1cdbe1e34009f71"
region: "München"
country: "Deutschland"
completed: "1224"
missions: "24"
date: "2017"
bg-link: "https://bannergress.com/banner/pasinger-stadtwappen-0d09"
onyx: "0"
description: "Die nächste Mission beginnt jeweils am letzten Portal der vorherigen Mission. Es kommen Hack- und Capture/Upgrade-Missionen vor. Fahrrad ist von Vorteil."
lengthKMeters: "13,85"
title: "Pasinger Stadtwappen"
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

