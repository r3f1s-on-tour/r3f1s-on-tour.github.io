---
nummer: "5"
startLatitude: "54.309207"
startLongitude: "13.115364"
titel: "Silhouette von Stralsund"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_a6I6CdPR7exdgpdMl0S3sYaN8tvKSfX7SZuX9USgHJhCYFaFbfySM6jaowslvLecQs76TbitOxUMqbwK3oxQT3AbS7cs-ZW7HBiWHLKY0K-9_xh2CvBYk9PxQ_R7q0MWzuvCWJ_ihHBTvIlZ7ij9IUzNFlo2sAyp_tZTIopsBqGmzEHEqj9fUfD3dSazDaoLgOO1BwkI43vypBpBZXTw8lHvVS1l--O0hLM7LQ0Vy5FHfdgVTFGPYDKP664z04qgEMM0J7d7rPFCCpoe1eH12RY8MOXrTVzIqGmLBEPCkbM7w5gj6gZSGCO_39w0-ZGRwofufifTAVRrZ4Xgv5Dx9qfBZ9XaxO0g8N6zwjvyrViQ6Yb5_ToIW2mhmU2pIRUlXzDaA_6uOgTbFvi97qFqpBlYPZ1E_K6HBc5RqDbxIkMVkX80gTFM8EkFkp32yEnTKY3TlL_DAOXQqLf2AcasJWNxvESVmZDmdYq1fc4EgwtdH81b13lB6b5T0hBTXCZRTCs1UuOfAlqgEAPqN3mW1-F2KXXWeMJ6VmwN7IjG8QJb_wPYCHWDtgLDnXmIh-j4UAxaVoM7Aa7tXkbjS8g48qn8D70fuGBlxVHFyDxMcfx0zy5yCElsmywFKJgVlFi3h3xtCX2V0XMBsGsgrqlLmxqMsc5HWRpE_JPD7bwGP5vrUV3ELE_zJYjdF6mzk0a7FQUXM6pw"
region: "Stralsund"
country: "Deutschland"
completed: "138"
missions: "6"
date: "2015"
bg-link: "https://bannergress.com/banner/silhouette-von-stralsund-a792"
onyx: "0"
description: "Vom Dänholm entlang des Strelasunds in Richtung  Parow charakterisiert die neue Rügenbrücke sowie die drei großen mittelalterlichen Kirchen der Backsteingotik die Silhouette Stralsunds."
lengthKMeters: "5,51"
title: "Silhouette von Stralsund"
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

