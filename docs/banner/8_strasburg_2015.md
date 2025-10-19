---
nummer: "8"
startLatitude: "53.506861"
startLongitude: "13.74885"
titel: Strasburg
picture: https://lh3.googleusercontent.com/lr/AFBm1_YHocJTozHb2PU-fJnCVyoQax-cIniAru54mWUt9ry7Oh_tZXJW0crVqMsdoJIggwlOWMXY3x05rx9r_ICDMQaOvtTR9AAY2PmWTQUaSdGGxyfTTYBxC0jjzfKFKq9F25iMqOAs3JAdTyb0mywDPDWoNGSQjvSaYrNJ1xGrAMf61Rzb1GpWCmA3tB6Ab6nexYNiQ7aw9vJcVkqE3RfMmXyHEfXyFbdr4B-ztgyr0Q1b3xU0adIw-TG1ls8xxse_whQwYP-c-hpNVcnIQHWCiHcbWMlwuMQM0r1qkJIkeVErdvXigtewwlVges64iii2PIR0H9t1KySKMOfqe8s2SQBg_VX0Bip7sQBMGJCdO7sEiH3cOWDEUwj_N_lZrn9L1Qf_aMd6iw99m2kW55ku02a1PeSPYTdLCgaYUNS8sYxXYxuVVZ2y2S-PZ1fW52ErYWvwtMnrsdQhMWGy_4gZAgZWimqJoba3g8Dj3rR9GmGdbGyjoNynVhSyxNK7JyUezNBQMkAr7vHHqM3kaq7JeGsPkA50q8QRHpDbfCvwhq5f6exgudqNF6BOEgMkCk37W-8gajx5hu7wDZT0XslQdxHNsMhTRuA0cz5ed-Fz_XgOiyu42j2ap1FO0pOmIzRi8jGqCPO1DuehQNDXdeE8QLNi6JbIrfKWGQd6KiY2926fCtK7Dy3VeKxBHvMWdiZDDyP6hYapvhvCVfawsdx7RcNjEkpc5Akqun3S9Q10p6H5ysk9RY_VfXddIykpW84U274hTPH5zWrOiguT5TLk9alTipUCA5zJJT2fErEZ0s4JgjNleyhV1zp8Bu8YEuj8A2O9ph0xjN_a12U7X9IaGK9pjHEkv8s
region: Strasburg (Uckermark)
country: Deutschland
completed: "180"
missions: "6"
date: "2015"
bg-link: https://bannergress.com/banner/strasburg-bc8d
onyx: "0"
description: 
lengthKMeters: 
title: Strasburg
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

