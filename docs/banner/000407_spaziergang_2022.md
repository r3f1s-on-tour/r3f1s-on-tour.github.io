---
nummer: "407"
startLatitude: "52,530972"
startLongitude: "13,382606"
titel: "SPAZIERGANG"
picture: ""
region: "Berlin"
country: "Deutschland"
completed: "8.676"
missions: "6"
date: "2022"
bg-link: "https://bannergress.com/banner/spaziergang-88bd"
onyx: "0"
description: "Eine kleine  Runde in Berlin Mitte"
lengthKMeters: "6,23"
umap: ""
title: "SPAZIERGANG"
---
# {{ page.meta.title | default('Untitled') }}

_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

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
