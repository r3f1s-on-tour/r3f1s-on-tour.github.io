---
nummer: "82"
startLatitude: "48.139034"
startLongitude: "11.570978"
titel: "Münchner Tatort-Ermittler 1972 bis heute"
picture: "https://api.bannergress.com/bnrs/pictures/77711b4cacce06b18fab3b10425c745d"
region: "München"
country: "Deutschland"
completed: "2166"
missions: "6"
date: "2017"
bg-link: "https://bannergress.com/banner/m%C3%BCnchner-tatort-ermittler-1636"
onyx: "0"
description: "Ivo Batic und Franz Leitmayr, gespielt von Miroslav Nemec und Udo Wachtveitl, sind seit seit 1991 Münchner Tatort-Kommissare. In den ersten 25 Jahren bekamen sie es mit 152 Toten zu tun ..."
lengthKMeters: "2,11"
umap: ""
title: "Münchner Tatort-Ermittler 1972 bis heute"
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
