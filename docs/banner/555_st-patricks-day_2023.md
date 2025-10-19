---
nummer: "555"
startLatitude: 53,568315
startLongitude: 13,276832
titel: St-Patricks-Day
picture: Bitte Url nachtragen
region: Neubrandenburg
country: Deutschland
completed: "12.366"
missions: "6"
date: "2023"
bg-link: https://bannergress.com/banner/st-patricks-day-9a7a
onyx: "0"
description: Der Saint Patrick’s Day ist der Gedenktag des irischen Bischofs Patrick, der im 5. Jahrhundert lebte und als erster christlicher Missionar in Irland gilt. (Cargress ready!)
lengthKMeters: 3,3
title: St-Patricks-Day
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

