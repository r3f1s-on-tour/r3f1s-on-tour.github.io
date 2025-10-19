---
nummer: "562"
startLatitude: "53,561402"
startLongitude: "13,261756"
titel: "Treptower Tor"
picture: "Bitte Url nachtragen"
region: "Neubrandenburg"
country: "Deutschland"
completed: "12.456"
missions: "24"
date: "2023"
bg-link: "https://bannergress.com/banner/treptower-tor-3721"
onyx: "0"
description: "Das Treptower Tor ist eines von 4 Toren  in Neubrandenburg. Im Baustil  der norddeutschen Backsteingotik wurde das Tor im 14. Jahrhundert errichtet."
lengthKMeters: "10,222"
title: "Treptower Tor"
---

#{{ page.meta.title}}
_**Datum:** {{ page.meta.date }} • **Country:**{{ page.meta.country}}_

## Bild
![{{page.meta.title | default('Bild')}}]({{page.meta.picture}})

## Links
- **bg-link**: {% raw %}[{{ page.meta.bg-link }}]({{ page.meta.bg-link }}){% endraw %}

## Infos
- **nummer**:{{ page.meta.nummer}}
- **startLatitude**:{{ page.meta.startLatitude}}
- **startLongitude**:{{ page.meta.startLongitude}}
- **region**:{{ page.meta.region}}
- **country**:{{ page.meta.country}}
- **completed**:{{ page.meta.completed}}
- **missions**:{{ page.meta.missions}}
- **onyx**:{{ page.meta.onyx}}
- **description**:{{ page.meta.description}}
- **lengthKMeters**:{{ page.meta.lengthKMeters}}

