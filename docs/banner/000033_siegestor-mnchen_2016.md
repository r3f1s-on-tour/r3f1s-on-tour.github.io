---
nummer: "33"
startLatitude: "48.140569"
startLongitude: "11.577356"
titel: "Siegestor München"
picture: "https://api.bannergress.com/bnrs/pictures/235ff037bace8063259176a2f8e669d9"
region: "München"
country: "Deutschland"
completed: "672"
missions: "24"
date: "2016"
bg-link: "https://bannergress.com/banner/siegestor-m%C3%BCnchen-4f77"
onyx: "0"
description: "Das Siegestor wurde 1843 bis 1850 aus Kelheimer Kalkstein errichtet. Am 15. Oktober 1850 übergab König Maximilian II. im Namen seines abgedankten Vaters das Siegestor an die Stadt München."
lengthKMeters: "7,66"
title: "Siegestor München"
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

