---
nummer: "50"
startLatitude: "48.137238"
startLongitude: "11.576208"
titel: "Weihnachten am Chinesischen Turm"
picture: "https://api.bannergress.com/bnrs/pictures/4b5ea303a04b6c745ca69d622a2b195f"
region: "München"
country: "Deutschland"
completed: "1164"
missions: "24"
date: "2016"
bg-link: "https://bannergress.com/banner/weihnachten-am-chinesischen-turm-46d7"
onyx: "0"
description: "Der Chinesische Turm wurde in den Jahren 1789 bis 1790 erbaut und 1792 mit der Eröffnung des Englischen Gartens als Aussichtsplattform der Öffentlichkeit zugänglich gemacht."
lengthKMeters: "5,54"
umap: ""
title: "Weihnachten am Chinesischen Turm"
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
