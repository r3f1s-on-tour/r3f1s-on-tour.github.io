---
nummer: "496"
startLatitude: "50,933153"
startLongitude: "6,933925"
titel: "Sushi Sonntag"
picture: "Bitte Url nachtragen"
region: "Köln"
country: "Deutschland"
completed: "10.602"
missions: "12"
date: "2022"
bg-link: "https://bannergress.com/banner/sushi-sonntag-781c"
onyx: "0"
description: "Zu den neuen Second Sundays Mission Days passt dieses Sushi Sonntag Banner. Auf der Strecke liegen mehrere Sushi Restaurants, aber hier findet man für jeden Geschmack etwas."
lengthKMeters: "3,283"
title: "Sushi Sonntag"
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

