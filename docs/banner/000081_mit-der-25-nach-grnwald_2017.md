---
nummer: "81"
startLatitude: "48.135479"
startLongitude: "11.598087"
titel: "Mit der 25 nach Grünwald"
picture: "https://api.bannergress.com/bnrs/pictures/b53d37e0f534572b1c95f217c63c8344"
region: "München"
country: "Deutschland"
completed: "2160"
missions: "18"
date: "2017"
bg-link: "https://bannergress.com/banner/mit-der-25-nach-gr%C3%BCnwald-1b1f"
onyx: "0"
description: "Vom Max-Weber-Platz mit der Tram 25 nach Grünwald. Am Ende kann in Grünwald noch der Schriftzug „Entdecke Grünwald“ (6er Banner) angehängt werden."
lengthKMeters: "17,46"
title: "Mit der 25 nach Grünwald"
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

