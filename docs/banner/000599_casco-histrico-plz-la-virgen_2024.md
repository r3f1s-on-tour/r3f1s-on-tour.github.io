---
nummer: "599"
startLatitude: "39,46944"
startLongitude: "-0,375533"
titel: "Casco Histórico Plz. La Virgen"
picture: "https://api.bannergress.com/bnrs/pictures/342c7600849e873a4902bf8f0f8af4d0"
region: "València"
country: "España"
completed: "13.218"
missions: "18"
date: "2024"
bg-link: "https://bannergress.com/banner/casco-hist%C3%B3rico-plz-la-virgen-4c18"
onyx: "0"
description: "Uno de los lugares mas emblemáticos de la ciudad Valenciana, es sin duda la plaza de la Virgen en pleno centro del casco antiguo y rodeado de muchas calles con un ambiente muy muy agradable."
lengthKMeters: "4,275"
umap: ""
title: "Casco Histórico Plz. La Virgen"
---
# {{ page.meta.title | default('Untitled') }}

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
