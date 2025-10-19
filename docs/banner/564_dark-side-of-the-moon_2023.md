---
nummer: "564"
startLatitude: "52,413667"
startLongitude: "13,051148"
titel: "Dark Side of the Moon"
picture: "Bitte Url nachtragen"
region: "Potsdam"
country: "Deutschland"
completed: "12.498"
missions: "18"
date: "2023"
bg-link: "https://bannergress.com/banner/dark-side-of-the-moon-b01f"
onyx: "0"
description: "Discover the dark side of the moon in Potsdam. Start at the Fachhochschule and move towards Nauener Tor."
lengthKMeters: "5,476"
title: "Dark Side of the Moon"
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

