---
nummer: "557"
startLatitude: "50,946435"
startLongitude: "7,455323"
titel: "Frog Wall Drabenderhöhe"
picture: "Bitte Url nachtragen"
region: "Drabenderhöhe"
country: "Deutschland"
completed: "12.390"
missions: "6"
date: "2023"
bg-link: "https://bannergress.com/banner/frog-wall-drabenderh%C3%B6he-176f"
onyx: "0"
description: "Kleine Runde um die Kirche und dem Turm der Erinnerung in Drabenderhöhe."
lengthKMeters: "2,081"
title: "Frog Wall Drabenderhöhe"
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

