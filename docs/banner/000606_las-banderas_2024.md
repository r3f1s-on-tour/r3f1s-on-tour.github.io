---
nummer: "606"
startLatitude: "39,47116"
startLongitude: "-0,324172"
titel: "Las Banderas"
picture: "https://api.bannergress.com/bnrs/pictures/1b12a50c200b30ace4a20b0cd161dc02"
region: "València"
country: "España"
completed: "13.302"
missions: "12"
date: "2024"
bg-link: "https://bannergress.com/banner/las-banderas-c32a"
onyx: "0"
description: "Vamos a pasear desde un gran punto de reunión e interés (La Nau de l'aigua) hasta otro gran punto de referencia (Las Banderas) que hace de unión entre el paseo marítimo y \"La Marina de València\""
lengthKMeters: "4,719"
title: "Las Banderas"
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

