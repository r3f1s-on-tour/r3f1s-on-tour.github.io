---
nummer: "10"
startLatitude: "54.099775"
startLongitude: "13.382173"
titel: "Museumshafen Greifswald"
picture: "https://api.bannergress.com/bnrs/pictures/01328fd0e24c9c0a82a36a93613be784"
region: "Greifswald"
country: "Deutschland"
completed: "216"
missions: "18"
date: "2015"
bg-link: "https://bannergress.com/banner/museumshafen-greifswald-66c3"
onyx: "0"
description: "Teil 1 der Tour \"Museumshafen Greifswald\""
lengthKMeters: "5,93"
umap: ""
title: "Museumshafen Greifswald"
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
