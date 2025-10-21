---
nummer: "39"
startLatitude: "48.134114"
startLongitude: "11.389033"
titel: "Time Space und Fürstenfeldbruck"
picture: "https://api.bannergress.com/bnrs/pictures/0c9708630f31755d9cb89f468ad2e6ba"
region: "Germering"
country: "Deutschland"
completed: "828"
missions: "48"
date: "2016"
bg-link: "https://bannergress.com/banner/time-space-und-f%C3%BCrstenfeldbruck-7a7f"
onyx: "0"
description: "Eine Reise durch den schönen Landkreis Fürstenfeldbruck."
lengthKMeters: "98,19"
title: "Time Space und Fürstenfeldbruck"
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

