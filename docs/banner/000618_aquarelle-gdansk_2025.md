---
nummer: "618"
startLatitude: ""
startLongitude: ""
titel: "Aquarelle Gdansk"
picture: "https://api.bannergress.com/bnrs/pictures/ec7c1f87079942aabcfc16d660f09708"
region: "Gdansk"
country: "Polska"
completed: "13.500"
missions: "12"
date: "2025"
bg-link: "https://bannergress.com/banner/aquarelle-gdansk-a640"
onyx: "1"
description: ""
lengthKMeters: ""
title: "Aquarelle Gdansk"
---

# {{ page.meta.title }}
_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

## Bild
![{{ page.meta.title | default('Bild') }}]({{ page.meta.picture }})

## Links
- **bg-link**: [{{ page.meta['bg-link'] }}]({{ page.meta['bg-link'] }})

## Infos
- **nummer**: {{ page.meta.nummer }}
- **region**: {{ page.meta.region }}
- **country**: {{ page.meta.country }}
- **completed**: {{ page.meta.completed }}
- **missions**: {{ page.meta.missions }}
- **onyx**: {{ page.meta.onyx }}

