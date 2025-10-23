---
nummer: "508"
startLatitude: "51,260319"
startLongitude: "7,145203"
titel: "Elberfeld im Schneckentempo"
picture: "https://api.bannergress.com/bnrs/pictures/59a729228b1cf48cf1b3990eedf280e7"
region: "Wuppertal"
country: "Deutschland"
completed: "10.836"
missions: "12"
date: "2022"
bg-link: "https://bannergress.com/banner/elberfeld-im-schneckentempo-82c3"
onyx: "0"
description: "Eine gemütliche Runde durch den Stadtbezirk Elberfeld der Stadt Wuppertal."
lengthKMeters: "2,828"
umap: ""
title: "Elberfeld im Schneckentempo"
---
# {{ page.meta.title | default('Untitled') }}

_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

![{{ page.meta.title | default('Bild') }}]({{ page.meta.picture }})

- **bg-link**: [{{ page.meta['bg-link'] }}]({{ page.meta['bg-link'] }})

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
