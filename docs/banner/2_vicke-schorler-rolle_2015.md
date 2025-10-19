---
nummer: "2"
startLatitude: "54.088461"
startLongitude: "12.129432"
titel: "Vicke Schorler Rolle"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_Z8QtjY_UGNM372bXUY7gDxnSsw_VUB2Huu-skZ5Gpg5Gtj0TA0nyK2y6LTT9SvBTn1Pr4FQk0zVyYviBqDnXmlg7GeiEkPkWtmh2Sml3YGfaxxOUck7hrIdyItPa6k-6NVEXqQ-8ySxVq4Q6tZYZTYwjGYoSTWr6mBJ0I0ULBbLeCeRDg0l_aVio19yRlGEHmGcsXVnuV3L_HYuivCyhWnXuS3cpYH-P3ZfUeXM0UmBe63f3aMAS3T6p3HnnXXSXPxKr-HYgkmF94g8hsEXu3Hx_YCnFpuVRErLSWJX5QUL1HLdEu4qVHLiOjiTgkKUu5eXGICm9YMPJOOFnNVUqjNZzhTs5sBVUg_zc9RGyZplIck8F1JqzHFguXk60-cwRcb18PiDQzZFx7DyQFgrB0-XIMpbTwV5rrDO1SObTuusPf792ar-6K3s1vDaK_8rFoh8Jovi2yl355A_94dtu2n3cV8GWVaweZiO_i6XzzuEF_zu9WbHwoCy0fRlMJQHwA4eRa_nASCOFrY3uimCVEZ6XqyP5z3tHAgT1vfip5rXjxGCx2Zz2XM6CQ6KesFh3hj3jdO7N0hB8Mw68Mp4CpQaDpZvnLLPiIbqUhulKwrv2lzIex8K-oGig_RBmVBOrIwFWPInM7tZHZGwSlQLwcC8H7kO4kf0vTtDZ_Z18zu2AN8FBWqvjg5_Co8wU5xwtmbHm4XQw"
region: "Rostock"
country: "Deutschland"
completed: "102"
missions: "6"
date: "2015"
bg-link: ""
onyx: "0"
description: ""
lengthKMeters: ""
title: "Vicke Schorler Rolle"
---

# {{ page.meta.title }}
_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

## Bild
![{{ page.meta.title | default('Bild') }}]({{ page.meta.picture }})

## Infos
- **nummer**: {{ page.meta.nummer }}
- **startLatitude**: {{ page.meta.startLatitude }}
- **startLongitude**: {{ page.meta.startLongitude }}
- **region**: {{ page.meta.region }}
- **country**: {{ page.meta.country }}
- **completed**: {{ page.meta.completed }}
- **missions**: {{ page.meta.missions }}
- **onyx**: {{ page.meta.onyx }}

