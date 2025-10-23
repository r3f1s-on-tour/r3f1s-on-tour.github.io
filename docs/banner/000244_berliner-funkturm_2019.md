---
nummer: "244"
startLatitude: "52.504929"
startLongitude: "13.279174"
titel: "Berliner Funkturm"
picture: "https://api.bannergress.com/bnrs/pictures/e5bdca79ae49d548bcbd328e0c16509e"
region: "Berlin"
country: "Deutschland"
completed: "5964"
missions: "150"
date: "2019"
bg-link: "https://bannergress.com/banner/berliner-funkturm-c3d7"
onyx: "0"
description: "Der Berliner Funkturm ist ein 146,7m hoher Stahlfachwerkturm in Berlin und  eines der Wahrzeichen der Stadt sowie Symbol des Widerstandes und Freiheitswillen der West-Berliner in der Nachkriegszeit."
lengthKMeters: "86,77"
umap: ""
title: "Berliner Funkturm"
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
