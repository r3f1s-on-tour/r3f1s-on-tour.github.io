---
nummer: "42"
startLatitude: "48.141742"
startLongitude: "11.57772"
titel: Antiquarium München
picture: https://lh3.googleusercontent.com/lr/AFBm1_Yk_Kkk5UULe9qsO9dZ-8XnXJOBfgaW-6GUW75zFV5SA1ReKEufz4CKJ-DYFG_PVhnQooQ_n-k5z65wJUSa3t2BwacDkiPyCPKFF0a2m-XMyj2dxFyCvPw0LLrcYjkiKw4Gj3WoRaJ4F2rdD1RMOMtsf_WVkH_4vxcUfDY9XtRUTcJTmg-F85j83mVZVP7d-6ERbzNk5q0LtkFNlNoUpogJ7OJ8r8ixXwwRAEQrCSCJrBK0asrN7dks8VBoizwT7xjgbUQrPzY8PHfgSqYzIJFtRwpOF_va6qIjMjFc2Ecm1oUxkgYsccDN5fsoXR7TwP3mEljqu7Dh6EUg-teBEJy2HWHEeiSWEV9vSaYWKKH11GEm66y348IpWqPgHk_eImqg0RTeWkAh1Z539093Oow5E_JVNDmp8M7umMJiYBfHTw5AfzZNxL7ZEgAygMONq__6Q2OHXk0dRmDJpqBbkxmLt9BJSQXkFda8HAWjc8UDUQCeT9zl29zHJ3eI3lKznCen4BOvv7qb_a-UMCE3XUGklX3C91MbfgZqPyqwjHiG8EBq37rFhvzyhgm1RGBcm2Zh0RDd-cvdNoR88h1xLQPDRy2esXmTq3bAydsx2CqfvtV_BDdlTJI4-sDo0vF0HinJK9q4Sjj-_1WCs7ewvjVjMTEjCaTuVvPCUEtkl4GlWJ-dQvY2u8ZkHnVQ2YVmaZonjkheP5-84RKrKKty8iTZXOXl_DDNLYLP-WLQ67tpMvS_RGeHkUYFx7z4mK6Zx886baofcVtBIe8vAfgBZAW8ZefqVqh00yqMEWjMu9BWtcGNIwsI34epNs5O5TubIUUDF1AxrzP3XsdmtT7s7IuIe4GjJE2CS6Ly
region: München
country: Deutschland
completed: "930"
missions: "24"
date: "2016"
bg-link: https://bannergress.com/banner/antiquarium-m%C3%BCnchen-f327
onyx: "0"
description: Das Antiquarium wurde ab 1568 zur Aufnahme der herzoglichen Antikensammlung und Bibliothek als Erweiterung der Münchner Residenz errichtet und wenig später zu einem Festsaal umgestaltet.
lengthKMeters: 8,23
title: Antiquarium München
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

