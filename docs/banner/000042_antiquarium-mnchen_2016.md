---
nummer: "42"
startLatitude: "48.141742"
startLongitude: "11.57772"
titel: "Antiquarium München"
picture: "https://api.bannergress.com/bnrs/pictures/84f766e615e30748b7ad56ec92a8e957"
region: "München"
country: "Deutschland"
completed: "930"
missions: "24"
date: "2016"
bg-link: "https://bannergress.com/banner/antiquarium-m%C3%BCnchen-f327"
onyx: "0"
description: "Das Antiquarium wurde ab 1568 zur Aufnahme der herzoglichen Antikensammlung und Bibliothek als Erweiterung der Münchner Residenz errichtet und wenig später zu einem Festsaal umgestaltet."
lengthKMeters: "8,23"
umap: ""
title: "Antiquarium München"
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
