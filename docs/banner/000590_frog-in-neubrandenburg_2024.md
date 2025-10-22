---
nummer: "590"
startLatitude: "53,561425"
startLongitude: "13,259994"
titel: "Frog in Neubrandenburg"
picture: "https://api.bannergress.com/bnrs/pictures/9582c8830b4adf1afd3623aa41313d9a"
region: "Neubrandenburg"
country: "Deutschland"
completed: "13.068"
missions: "18"
date: "2024"
bg-link: "https://bannergress.com/banner/frog-in-neubrandenburg-fbd3"
onyx: "0"
description: "Beginne eine Runde durch Neubrandenburg und entdecke auf deiner Runde die Sehenswürdigkeiten und Denkmäler der Stadt."
lengthKMeters: "4,795"
title: "Frog in Neubrandenburg"
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

