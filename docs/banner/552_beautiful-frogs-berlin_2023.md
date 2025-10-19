---
nummer: "552"
startLatitude: 52,54767
startLongitude: 13,413923
titel: Beautiful Frogs Berlin
picture: Bitte Url nachtragen
region: Berlin
country: Deutschland
completed: "12.258"
missions: "6"
date: "2023"
bg-link: https://bannergress.com/banner/beautiful-frogs-berlin-35db
onyx: "0"
description: Have a walk around the Gethsemane church.
lengthKMeters: 1,459
title: Beautiful Frogs Berlin
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

