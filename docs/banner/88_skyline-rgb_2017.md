---
nummer: "88"
startLatitude: "49.020536"
startLongitude: "12.102202"
titel: Skyline RGB
picture: https://lh3.googleusercontent.com/lr/AFBm1_ZdRQM-yYGWcPzUEGPkSkxn8LOABPn4B-7hRKSWE_vNvsVzHxG4dbWWb-oqXXZ8bwtgTl3zvGxUuMvG-xJxsKrQoU9OE6abLM2pfO9Nrbf9IQIDMT4eVg-puESyeJ1EdeUQpYYlK7OCke7-u72ComjJiznZo4YlhEVA7ShoqYaLWP8NHPqX-inNmQI683n4Mn_lkHZWsk476kJgpmv662Dj8LE2rH7CLi9UuEvCasz_4GJSxDAxPkU1GuX5st2OItThZkJqpw7b1of-0xWFEYIneX00ndD5hS7uf7rlXZpwmKCnbZBCv3VaYL24w0w4HpPoX9Sv7iz9rr9P6f56EfOhzgJmLEevn8bho-HGf9Gx2sGNPU-S6ajJY9AXVAvR_ogTAFOZJTC-Z-BbkISRAVvJmO3PotiG-LmoLfPe3bKHadxlN5psRgm_5lAdcc1DoUfEXtWxRqNFOGV3P6X8bE2JgK7id-8oIh0C9yg2WlyximlsejzV1VuN6RcmssmFArVRzE63nsIFASMli0Hbc3kJMLGwqMscigHBZ9X-JUjA2GhoCKh2jFIeWWRbxehHEk9SfbTT0-f2QEWMOKBISyYh7IMNApm6yurgfyjJOfe0ckOhY70sA3w2MyfGG094AEMDoRryQ8nxlb6A3NtPCtV-6WGiJTCtTX1Ai7QjU4R9fwk56R-iO46Zw2Bc8V_-pUytpe_9UfRL6p25dS82I6IG2euqPHK6MtN1JxT1a4XJZSwrwjiDWEQvjuxEzIHejr-N_cwGsqHXcUjHbYOa6CrOlwYjxG00zIBMw_cLv9eU92ZBvqWFavb85PNFSzdlr58BgpJQbdGsKlfLf0cwYzlzTwEVJRKlh6zx
region: Regensburg
country: Deutschland
completed: "2262"
missions: "6"
date: "2017"
bg-link: https://bannergress.com/banner/skyline-rgb-40c3
onyx: "0"
description: Entdecke Regensburg entlang der Donau! // Explore Regensburg on a series of six consecutive hack-only missions!
lengthKMeters: 1,46
title: Skyline RGB
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

