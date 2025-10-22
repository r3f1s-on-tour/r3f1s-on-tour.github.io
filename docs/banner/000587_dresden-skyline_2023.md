---
nummer: "587"
startLatitude: "51,05795"
startLongitude: "13,74587"
titel: "Dresden Skyline"
picture: "https://api.bannergress.com/bnrs/pictures/24dd2b71b50b077aa14b9c7ff4a7c449"
region: "Dresden"
country: "Deutschland"
completed: "13.026"
missions: "12"
date: "2023"
bg-link: "https://bannergress.com/banner/dresden-skyline-06da"
onyx: "0"
description: "Dresden - eine barocke Perle an der Elbe. Viele Maler haben diese Pracht schon auf Leinwand verewigt. Nun könnt ihr ein Mosaik aus 12 Teilen in eurem Agent-Profil ergänzen.\nTeil 1 von 12"
lengthKMeters: "4,1"
title: "Dresden Skyline"
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

