---
nummer: "1"
startLatitude: "54.077793"
startLongitude: "12.129966"
titel: "Rostocker Flagge"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_be9DpknfbWe8QLROiqbX5kH10NiOBje_XG5_yoYdjSNGeNyF7k_Y2JUIUv7W06eyNpFoHtsGPuSpyQ-8-8S1jMaUs-dSxUrwjx2DTnk4g_KHVsr8aR2i1a10SkSp_Nh6597vVV0maWbk57GeKWvzZywkCAysKoM6rJegESG2vdvRIaI1s4D-2t9qTtyFq9q-8kcKZTtMfL9zbQ55NTJvuSbEcr0_GGV-cu4_l5080HqeQ68GWFeVyC9Kyfo6CPBpHTmZirx4eEN6Buw0UCJ60GU9B-G2nXKO34of-OBlwJFgevnbEBesZHZV7dGqSYJJUyKk8AekDhQzGgxToyahYqnmlh8uLkgpq7r3EKgV6GwWTzrDs769P6rPgZcNJ5OXSTNxJbTSAtQwpBhaec_Koko_0H8sxReIRtvlK6fjpDdnIP-g4UbX5AYnzTOTxkXbEAR2W3P2j3DUBzf4QymN2RWtjxWwV7pFz0Ohm07RvA6hX5U1GLmMiUXCAr5pHaLPlL6hkz_DV5a0ufb0NYcVszGZIIwYPIbh6ZLlrDkAX0oKTdTM0H4lQ4VshUcH3lPSmOmmxsv09mbPdtw-jMGKQB8Js5PDK-w7k3r5Nj7aswAizV0SGpHnGkfTH3O9Gw1cWiadpmJwWMlnZAlACL3scXKV1DqFVDU0756-C488to_D-jceUQRK1Ru6z0gw-QwsMl9FwmgQ"
region: "Rostock"
country: "Deutschland"
completed: "96"
missions: "24"
date: "2015"
bg-link: "https://bannergress.com/banner/rostocker-flagge-9920"
onyx: "0"
description: "Erkunde ab hier die wunderschöne Hansestadt Rostock mit Ihren Sehenswürdigkeiten.\nBeginne mit dem Bahnhof als zentralen Anlaufpunkt.\nPS- Es sollte das Fahrrad genutzt werden."
lengthKMeters: "12,84"
title: "Rostocker Flagge"
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

