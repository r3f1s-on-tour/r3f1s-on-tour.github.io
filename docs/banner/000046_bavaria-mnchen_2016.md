---
nummer: "46"
startLatitude: "48.130672"
startLongitude: "11.545971"
titel: "Bavaria München"
picture: "https://api.bannergress.com/bnrs/pictures/f62fd3943e8a8f40cd07ff30a8d09d1a"
region: "München"
country: "Deutschland"
completed: "1050"
missions: "24"
date: "2016"
bg-link: "https://bannergress.com/banner/bavaria-m%C3%BCnchen-78e7"
onyx: "0"
description: "Die kolossale und monumental anmutende Bronzestatue der Bavaria wurde im Auftrag von König Ludwig I. (1786–1868) in den Jahren 1843 bis 1850 errichtet. Sie bildet eine Einheit mit der Ruhmeshalle."
lengthKMeters: "9,69"
umap: ""
title: "Bavaria München"
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
