---
nummer: "94"
startLatitude: "53.431931"
startLongitude: "14.552350"
titel: "MD Szczecin"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_ZzYydsKk2eBIuBN_DhVYZGB6Dst5Vk4b_hKksAqxmRsVL6u_JPA9Ngp7a1D9K74i1o0QwLxSczxvl9-4hK3f7vcfmuZmyAXLi4HAttmWZsTJK9cZHt7IDTDDKQVU2ptuAMuv368vJh-5fi797KC3KrOQ6s7tSKmKAKWf4XekPhuS5XzDFVhQ6RJDBWek7KJ9ckn9mBshzO6MlqGgfRP2StDZvMx0FUnO5-6jVmYhGuSGH2Bv14sBhyYy5rZ9DW1deqrABHzMrLU6i2s5MT05QHE5LdozVC9TUrn7siul8-8CrYG0UbeVCnpFzqXKJXAb_IugLZFZffxFNHGoVDwvxlLvLxHW_lIiDYBtOuwwRd07PgIMA8FqcqkZTyLPGRT6bjcbuBgSquTTRXjyFalqzFUC2OdrQK-NEF2I-A9UFuIGUcrv90T4R4wWufMKYJoJNe3JvmUF-QSmRgk7bq39S3tfRdrkMbAa7zpxQWDFV18Zcpg6idCx0F6R2STTIwUYjr5NbYU_UOlUAg-kPhmgY7EDiz_f1krIkmmFY9lJJ9eha4r7JrMU13GRTU51o5XEGTxXhYlBIk5yy9Qtq3kWSoLDzZ-holTX5KpWALLmRMHPwtafA7jQF_rxSEokgQUHrlZNFJOcBkNvsN5MiIDhU0-c9m3PO6dWADtymLoRg8umog4uTZLR7pWUzFL5GtTWO7dHU6qmHXjYzjxVkIAt7IWUVk9ilwL06Iu6t9aX-A0PIT_hYu2ewDYju9s7wG6ByNa_AhAwUEqRA1Gjyp3lgGJtqvFjHdNJs3OvzioAEl5B6w12xWVfvyxxl_p6DGpFhcq6jCeeGxrEjLpXCT_CM1kvHDm96pXoPF"
region: "Szczecin"
country: "Polska"
completed: "2430"
missions: "12"
date: "2017"
bg-link: "https://bannergress.com/banner/md-szczecin-46c7"
onyx: "0"
description: "The Avenue of Fountains, part of the Golden Route is a common place for walking and relaxing. It is lined with rectangular fountains, hedges, and a multitude of restaurants."
lengthKMeters: "41,61"
title: "MD Szczecin"
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

