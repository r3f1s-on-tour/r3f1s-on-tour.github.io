---
nummer: "543"
startLatitude: 53,507919
startLongitude: 13,746105
titel: A Second Sunday Cat Paws in Strasburg
picture: Bitte Url nachtragen
region: Strasburg (Uckermark)
country: Deutschland
completed: "12.000"
missions: "6"
date: "2023"
bg-link: https://bannergress.com/banner/a-second-sunday-cat-paws-in-strasburg-9199
onyx: "1"
description: Beginne eine Runde durch Strasburg und entdecke auf deiner Runde Sehenswürdigkeiten und Denkmäler der Stadt Strasburg. Starte in der Schulstraße
lengthKMeters: 1,047
title: A Second Sunday Cat Paws in Strasburg
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

