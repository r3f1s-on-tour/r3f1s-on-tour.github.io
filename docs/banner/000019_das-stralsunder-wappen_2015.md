---
nummer: "19"
startLatitude: "54.312901"
startLongitude: "13.078783"
titel: "Das Stralsunder Wappen"
picture: "https://api.bannergress.com/bnrs/pictures/ac273ab3137912d9cb9b92f74520cf2a"
region: "Stralsund"
country: "Deutschland"
completed: "348"
missions: "18"
date: "2015"
bg-link: "https://bannergress.com/banner/das-stralsunder-wappen-9a4d"
onyx: "0"
description: "Dies ist die 1. Mission für das Stralsunder Wappen!"
lengthKMeters: "5,64"
umap: ""
title: "Das Stralsunder Wappen"
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
