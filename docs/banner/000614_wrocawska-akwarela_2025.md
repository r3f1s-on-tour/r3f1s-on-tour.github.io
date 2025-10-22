---
nummer: "614"
startLatitude: ""
startLongitude: ""
titel: "Wrocławska akwarela"
picture: "https://api.bannergress.com/bnrs/pictures/3d3813d1331c65663189a5e5a17636a9"
region: "Wroclaw"
country: "Polska"
completed: "13.440"
missions: "18"
date: "2025"
bg-link: "https://bannergress.com/banner/wroc%C5%82awska-akwarela-6252"
onyx: "0"
description: ""
lengthKMeters: ""
umap: ""
title: "Wrocławska akwarela"
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

