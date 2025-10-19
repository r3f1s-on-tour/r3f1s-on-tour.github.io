---
nummer: "220"
startLatitude: "47.804923"
startLongitude: "13.049646"
titel: "Salzburg City Panorama"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_avtucsb4Hj9On0bKlrOOzi78rndiRXw7P2jbdqaxI2nL9oDJybn6s_3YvN467rIs94o1jVXS10ZVWwnmJpmEXhCbmlyXGtYYxpPlmvCUBPBxuazHKIkluo6YUdoO8cHaZDoDvAuUkjBt73WHfx3-FDArH53w8nhS_vuLVUuGfgIMZ4uAXZNywD4qBYZyV6Xs2oVcakdzTbMSHFP-gGyL6-TknMygdJo6N6uvy4qNF6zw8Y5IUeEs0MkrZiXWgySrpo7GNnYvwzgbvLwTyE6RkKPaZcBIA31KoLShDZRP87xIdcgEyM1pD1oOHbgIeiugEPaQ_P9XLdDnXIUy3q_oPKY46fqedT54PKZzaju8XV5DZCruCzTNIxWpDqZdtiqGV3lY_kbGQD6I-Ho2nmxWZsCQD5jkVK2YgGlNvrArQfj8o_siV7zKTXBNW_gGbKG5-JnYAm6fzdyygclRTEILkv6Qa-u1hb8zVqDSeb1DP-9t4GOKQqfOXNnA8eFqxXNOBxu8U6944kPvVjuUhaXGvJKCCTVMLKLIRZ5dK15X9PwJmPaZTIqxbtn0Sgjk5FEwh_2_QUDEXMWlM1y2o5me8j_1eObYCCP2oeW9Enf_KCX46KwYHtB7V66gfjrnFEJZrssg_WvnW3P-2As7sydJWnjgy8IJx3avyiITJypskmc0FmIUU6ZZLJyS74ggekXfLHZYT4foeKPSctRJUPdXUieet3RVnzUYdJ_I1M7ObcOXofyEqd8TDkVMsaMTGfKy0z_HfCOlrulCgf3ojBoQwap64GhshPWK7S2VO0uK9JWMXiM65y9q08pHFiuNFXJkXQKEYlDRnDeyW4EkAHXPziGdUeuhz-gCO_"
region: "Salzburg"
country: "Österreich"
completed: "5322"
missions: "18"
date: "2019"
bg-link: "https://bannergress.com/banner/salzburg-city-panorama-a104"
onyx: "0"
description: "Salzburg City Panorama"
lengthKMeters: "4,19"
title: "Salzburg City Panorama"
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

