---
nummer: "306"
startLatitude: "52.521556"
startLongitude: "13.41123"
titel: "EXO5BERLIN East"
picture: "https://api.bannergress.com/bnrs/pictures/41d6f7b502f08abee0c2b50aec38082a"
region: "Berlin"
country: "Deutschland"
completed: "7158"
missions: "48"
date: "2021"
bg-link: "https://bannergress.com/banner/exo5berlin-east-9312"
onyx: "0"
description: "This mission leads you to famous places in Berlin.  See places of Resistance history and farmgrounds. The first mission starts at Alexanderplatz."
lengthKMeters: "12,65"
umap: ""
title: "EXO5BERLIN East"
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

