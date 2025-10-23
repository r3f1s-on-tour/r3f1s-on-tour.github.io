---
nummer: "4"
startLatitude: "54.308652"
startLongitude: "13.078088"
titel: "Starry Night TARDIS"
picture: "https://lh3.googleusercontent.com/pw/AP1GczOYoXuwqJp6yd2kMQlUhFxc6l_VGhug7zs10AvGDFxAAzh07RDi_diFwOgtVu6l7dY_JUiUSpP7Jn4KRorWu0AUjLUZinfiiVYuchvBL-DZB-TiH39rbiRALO_JPRP75GnIifAZ8EA_0XSppe65X2Cl5w"
region: "Stralsund"
country: "Deutschland"
completed: "132"
missions: "24"
date: "2015"
bg-link: "https://bannergress.com/banner/starry-night-tardis-1458"
onyx: "0"
description: ""
lengthKMeters: ""
umap: ""
title: "Starry Night TARDIS"
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
