---
nummer: "486"
startLatitude: "52,50834"
startLongitude: "13,45134"
titel: "Northern Legends"
picture: "Bitte Url nachtragen"
region: "Berlin"
country: "Deutschland"
completed: "10.488"
missions: "6"
date: "2022"
bg-link: "https://bannergress.com/banner/northern-legends-5c88"
onyx: "0"
description: "Follow your path through the neighborhood of Friedrichshain."
lengthKMeters: "1,259"
title: "Northern Legends"
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

