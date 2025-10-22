---
nummer: "588"
startLatitude: "51,044895"
startLongitude: "13,739913"
titel: "DARK FROG RISES"
picture: "https://api.bannergress.com/bnrs/pictures/81e737911804f4785c856eac86305ba1"
region: "Dresden"
country: "Deutschland"
completed: "13.044"
missions: "18"
date: "2023"
bg-link: "https://bannergress.com/banner/dark-frog-rises-7776"
onyx: "0"
description: "This is the mosaic for the Enlightened at Umbra Dresden, which consists of 18 missions and offers a short walk through the city.\nBatfrog is calling!"
lengthKMeters: "6,811"
umap: ""
title: "DARK FROG RISES"
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

