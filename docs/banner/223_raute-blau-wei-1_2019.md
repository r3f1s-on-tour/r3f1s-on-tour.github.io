---
nummer: "223"
startLatitude: "48.1363204"
startLongitude: "11.5628643"
titel: "Raute Blau Weiß 1"
picture: "https://lh3.googleusercontent.com/pw/AM-JKLVxHtQh6Bn6jwi_jrKdau5SfX6mQgTG1Z-Clup9zYNC2391cA72wsdzyqma35o3WNi-gswPk7bBu_mQ8WBo-Bbgr5Wqj_-w2ShTaANPxtOBfF59kQpkRGUqqPS21r22cbp9W5XfxBspiC9AybFJ9_eI8Q=w1080-h153-no?authuser=0"
region: "Vaterstetten"
country: "Deutschland"
completed: "5352"
missions: "6"
date: "2019"
bg-link: "https://bannergress.com/banner/raute-blau-wei%C3%9F-teil-i-8b53"
onyx: ""
description: ""
lengthKMeters: ""
title: "Raute Blau Weiß 1"
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

