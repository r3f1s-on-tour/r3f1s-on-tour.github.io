---
nummer: "579"
startLatitude: "40,417009"
startLongitude: "-3,70231"
titel: "Visita a Madrid"
picture: "https://api.bannergress.com/bnrs/pictures/39251cd3df3e8cd862e8823254136dae"
region: "Madrid"
country: "España"
completed: "12.846"
missions: "6"
date: "2023"
bg-link: "https://bannergress.com/banner/visita-a-madrid-cbcd"
onyx: "0"
description: "Primera parte de la visita al la Puerta del Sol y sus alrededores, centro turístico y emblemático de la Capital de España, que no se puede dejar de visitar al ir a esta importante ciudad."
lengthKMeters: "949"
title: "Visita a Madrid"
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

