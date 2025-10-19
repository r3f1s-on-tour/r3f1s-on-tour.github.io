---
nummer: "538"
startLatitude: "53,558893"
startLongitude: "13,261834"
titel: "Schauspielhaus"
picture: "Bitte Url nachtragen"
region: "Neubrandenburg"
country: "Deutschland"
completed: "11.862"
missions: "24"
date: "2023"
bg-link: "https://bannergress.com/banner/schauspielhaus-a53c"
onyx: "0"
description: "Das Schauspielhaus befindet sich im Zentrum von Neubrandenburg. Es ist das älteste erhaltene Theater von Mecklenburg Vorpommern."
lengthKMeters: "5,061"
title: "Schauspielhaus"
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

