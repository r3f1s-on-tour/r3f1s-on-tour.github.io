---
nummer: "507"
startLatitude: "51,25423"
startLongitude: "7,149983"
titel: "Deifel in Wuppertal"
picture: "https://api.bannergress.com/bnrs/pictures/5043c3a180f5f2f1114de085f13cdf83"
region: "Wuppertal"
country: "Deutschland"
completed: "10.824"
missions: "6"
date: "2022"
bg-link: "https://bannergress.com/banner/deifel-in-wuppertal-5ea7"
onyx: "0"
description: "Starte am Hauptbahnhof einen Rundgang und entdecke Wuppertal. Auf deinem Abenteuer entdeckst du Sehenswürdigkeiten und historische Orte. Die Runde endet wieder am Hauptbahnhof"
lengthKMeters: "1,323"
umap: ""
title: "Deifel in Wuppertal"
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
