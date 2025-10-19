---
nummer: "546"
startLatitude: 50,8357
startLongitude: 12,924143
titel: "Do(o)m's Cat"
picture: Bitte Url nachtragen
region: Chemnitz
country: Deutschland
completed: "12.120"
missions: "48"
date: "2023"
bg-link: https://bannergress.com/banner/do-o-m-s-cat-1b2d
onyx: "0"
description: Explore Chemnitz Downtown while collecting the pieces of this Do(o)mCat
lengthKMeters: 18,487
title: "Do(o)m's Cat"
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

