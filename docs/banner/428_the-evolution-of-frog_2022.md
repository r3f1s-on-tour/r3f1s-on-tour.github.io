---
nummer: "428"
startLatitude: "53,565159"
startLongitude: "13,273601"
titel: "The evolution of frog"
picture: "Bitte Url nachtragen"
region: "Neubrandenburg"
country: "Deutschland"
completed: "8.910"
missions: "6"
date: "2022"
bg-link: "https://bannergress.com/banner/the-evolution-of-frog-1d8f"
onyx: "0"
description: "Macht einen kleinen Spaziergang durch die Vorstadt und schaut Euch dabei die Entwicklung des Frosches genau an. Wenn ihr wollt, könnt Ihr vor dem Start und am Ende ein schönes Eis essen."
lengthKMeters: "2,37"
title: "The evolution of frog"
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

