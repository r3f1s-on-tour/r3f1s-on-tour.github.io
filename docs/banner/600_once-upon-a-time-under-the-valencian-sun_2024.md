---
nummer: "600"
startLatitude: "39,470876"
startLongitude: "-0,376593"
titel: "Once Upon A Time Under The Valencian Sun"
picture: "https://api.bannergress.com/bnrs/pictures/ac7cc5b5c57769ac63ca1dee8f5d8afa"
region: "València"
country: "España"
completed: "13.236"
missions: "18"
date: "2024"
bg-link: "https://bannergress.com/banner/once-upon-a-time-under-the-valencian-sun-f640"
onyx: "0"
description: "Discover Valencia's Old Town, where historic charm meets vibrant culture. Wander through medieval streets, admire stunning architecture, and indulge in local cuisine at lively plazas."
lengthKMeters: "4,879"
title: "Once Upon A Time Under The Valencian Sun"
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

