---
nummer: "77"
startLatitude: "48.134439"
startLongitude: "11.596121"
titel: "Wiener Platz"
picture: "https://api.bannergress.com/bnrs/pictures/017bedff3d4bbcaf87c58d14b36ffd1e"
region: "München"
country: "Deutschland"
completed: "2088"
missions: "18"
date: "2017"
bg-link: "https://bannergress.com/banner/wiener-platz-d456"
onyx: "0"
description: "Am Wiener Platz befindet sich seit 1889 der kleinste der 4 ständigen Märkte Münchens. Nebenan befindet sich der Hofbräukeller, wo auch bis in die 1980er Jahre das Hofbräu-Bier gebraut wurde."
lengthKMeters: "7,90"
umap: ""
title: "Wiener Platz"
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
