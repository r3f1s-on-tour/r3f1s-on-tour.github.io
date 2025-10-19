---
nummer: "225"
startLatitude: "48.1354439"
startLongitude: "11.5474184"
titel: "Raute Blau Weiß 2"
picture: "https://lh3.googleusercontent.com/pw/AM-JKLVBRyxOrf-h-DcUHGFg6w2td7SG6HV6qF2HZ295gi0TbhqJ7PEOiPJ2GN2OnkoYlSjo2rsYSnqhd_bw4iyDl_QvQAfUtWWQ9wFiR_qZARmM849k83ai_zXZowb8uCdjAjrDzpfxHX2D06PYGo_a6wpW6A=w1080-h153-no?authuser=0"
region: "München"
country: "Deutschland"
completed: "5406"
missions: "6"
date: "2019"
bg-link: "https://bannergress.com/banner/raute-blau-wei%C3%9F-teil-ii-63f0"
onyx: "0"
description: ""
lengthKMeters: ""
title: "Raute Blau Weiß 2"
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

