---
nummer: "509"
startLatitude: "51,25571"
startLongitude: "7,148301"
titel: "Victory of Joker"
picture: "https://api.bannergress.com/bnrs/pictures/944f3a74ebc07fb46703491c0a54556a"
region: "Wuppertal"
country: "Deutschland"
completed: "10.860"
missions: "24"
date: "2022"
bg-link: "https://bannergress.com/banner/victory-of-joker-bbb4"
onyx: "0"
description: "Capture die Innenstadt von Wuppertal/Elberfeld. Am besten bringst du viele burster mit und ein wenig zeit. Die Mission wird dich durch Elberfeld zum Luisenviertel führen. viel Spaß -D"
lengthKMeters: "6,081"
title: "Victory of Joker"
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

