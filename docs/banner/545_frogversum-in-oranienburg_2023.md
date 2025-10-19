---
nummer: "545"
startLatitude: "52,756645"
startLongitude: "13,244983"
titel: "FrogVersum in Oranienburg"
picture: "Bitte Url nachtragen"
region: "Oranienburg"
country: "Deutschland"
completed: "12.072"
missions: "36"
date: "2023"
bg-link: "https://bannergress.com/banner/frogversum-in-oranienburg-c78b"
onyx: "0"
description: "Beginne eine Runde durch Oranienburg und entdecke auf deiner Runde Sehenswürdigkeiten und Denkmäler der Stadt Oranienburg. Starte in der Bernauer Straße"
lengthKMeters: "9,631"
title: "FrogVersum in Oranienburg"
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

