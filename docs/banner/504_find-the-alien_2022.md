---
nummer: "504"
startLatitude: "51,253636"
startLongitude: "6,771298"
titel: "Find the Alien"
picture: "Bitte Url nachtragen"
region: "Düsseldorf"
country: "Deutschland"
completed: "10.776"
missions: "24"
date: "2022"
bg-link: "https://bannergress.com/banner/find-the-alien-90f6"
onyx: "0"
description: "Willkommen auf dem Düsseldorfer Nordfriedhof. Nachdem hier schon die Borg gesichtet worden sind, \ngibt es starke Anzeichen dass es hier auch Aliens gibt. Folge der Route in der richtigen Reihenfolge!"
lengthKMeters: "5,541"
title: "Find the Alien"
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

