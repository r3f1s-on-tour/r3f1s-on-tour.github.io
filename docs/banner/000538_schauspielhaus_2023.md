---
nummer: "538"
startLatitude: "53,558893"
startLongitude: "13,261834"
titel: "Schauspielhaus"
picture: "https://api.bannergress.com/bnrs/pictures/1a84ff953b346ed980f83a30166ab1a2"
region: "Neubrandenburg"
country: "Deutschland"
completed: "11.862"
missions: "24"
date: "2023"
bg-link: "https://bannergress.com/banner/schauspielhaus-a53c"
onyx: "0"
description: "Das Schauspielhaus befindet sich im Zentrum von Neubrandenburg. Es ist das älteste erhaltene Theater von Mecklenburg Vorpommern."
lengthKMeters: "5,061"
umap: ""
title: "Schauspielhaus"
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
