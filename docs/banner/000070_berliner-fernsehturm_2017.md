---
nummer: "70"
startLatitude: "52.520724"
startLongitude: "13.40934"
titel: "Berliner Fernsehturm"
picture: "https://api.bannergress.com/bnrs/pictures/31b08225ae72b1f2f2cc3a10d7491b92"
region: "Berlin"
country: "Deutschland"
completed: "1986"
missions: "372"
date: "2017"
bg-link: "https://bannergress.com/banner/berliner-fernsehturm-d601"
onyx: "0"
description: "NUR NOCH BIS ZUM 31.12.2021 SPIELBAR!\n\nZur Umgehung des nicht öffentlich begehbaren Charitè-Geländes sind die Missionen Berliner Fernsehturm (altern.) 035 bis Berliner Fernsehturm (altern.) 040 online. Die Änderung der Route beginnt bereits am Hauptbahnhof, um die benötigte Portalanzahl zu erreichen. Ab Mission 41 ist die Originalroute spielbar. https-//bannergress.com/banner/berliner-fernsehturm-altern-bee8"
lengthKMeters: "139,56"
umap: ""
title: "Berliner Fernsehturm"
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
