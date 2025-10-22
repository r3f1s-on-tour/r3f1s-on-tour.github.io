---
nummer: "573"
startLatitude: "53,502666"
startLongitude: "13,989784"
titel: "Kiek in de Mark"
picture: "https://api.bannergress.com/bnrs/pictures/e075ccd90e335eba835d0a349672f3d1"
region: "Pasewalk"
country: "Deutschland"
completed: "12.630"
missions: "6"
date: "2023"
bg-link: "https://bannergress.com/banner/kiek-in-de-mark-80d9"
onyx: "0"
description: "Walk through the city and pick up a banner with the tower in rainbow colours."
lengthKMeters: "3,24"
title: "Kiek in de Mark"
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

