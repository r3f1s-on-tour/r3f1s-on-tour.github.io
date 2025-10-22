---
nummer: "2"
startLatitude: "54.088461"
startLongitude: "12.129432"
titel: "Vicke Schorler Rolle"
picture: "https://lh3.googleusercontent.com/pw/AP1GczMR6Ew49IolF_yKFAtKx2CaWrCeRg9NtiP3RF5H4aUAGzMi9Po7v_tc626pFIPbloPP7-yaBtUmO_eF3MXvescWN4xJwPrBo3MTsCvzMTaGSy4cKd4QGRvobKJSXWe8IH0AO9irvuhPwjU1t5JUw_cJ9Q"
region: "Rostock"
country: "Deutschland"
completed: "102"
missions: "6"
date: "2015"
bg-link: ""
onyx: "0"
description: ""
lengthKMeters: ""
umap: ""
title: "Vicke Schorler Rolle"
---

# {{ page.meta.title }}
_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

## Bild
![{{ page.meta.title | default('Bild') }}]({{ page.meta.picture }})

## Infos
- **nummer**: {{ page.meta.nummer }}
- **startLatitude**: {{ page.meta.startLatitude }}
- **startLongitude**: {{ page.meta.startLongitude }}
- **region**: {{ page.meta.region }}
- **country**: {{ page.meta.country }}
- **completed**: {{ page.meta.completed }}
- **missions**: {{ page.meta.missions }}
- **onyx**: {{ page.meta.onyx }}

