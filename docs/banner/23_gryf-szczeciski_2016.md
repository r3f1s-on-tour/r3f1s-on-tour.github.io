---
nummer: "23"
startLatitude: "53.426583"
startLongitude: "14.54793"
titel: "Gryf Szczeciński"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_bMeMt1Mt-k7-rkFDFa8KYIff8m8MLl-Z_pGaZPE4KW_qvpIqS-XKSZDpogRqZw4HzR3s4uThJzCsYWpukr5SWtUFRuaRloCA2kP8LAhEH0fAvPNtWtlAegTfFF3SaCEgAAJpLKaJkGUCrkb0XZ6CdHzl4Lyb_xWXC_Asp9KSaTO9IkD0iZsaaH9AkhGgyuMSvHPo8DioF9cczg_08qfO4YtJwdzurCfLqSna87Eo4rKrHPe6RUeTPhtmarAKr9TZH6MWkyYMKPogCOiCWFq9sV6LubogiNvTJIhJB3zuK00uU7jJdnortH6AKDgj_dnBPnaR1r6-0lvudCND7NlPjV6VZrhOi4ifhQQXBm66pM4iNXO4RgpXZnxf9gZXez8--RIbf5Tz4yTDFCCnYpfXWRKosOSLjh6e_Sbures7Job2to4MI06b1uHNafR-jkQnaHJ7SWXL4llnC6Ni3YXzi4ZEcOhjW0JSG4QSXsnYO3tChFJwzeYbcMOpaaeYlOsmu7scStOTMgaJgp2DuE2yNiPrHZjrmvIrv3iQI57O8AZrEZHjiD5-sXS8wJkpU7uAOc0U2Nr0oSZDZu5CCmIjuNvXCnmwnK3vdjrg5Ez1CWap1Bj7GqedRG98TBY6fNusemn1macAFLj3Q7g6BVe60NJHs2GT5szKSF00PlXRA34QZwTqAaljM9vINnekMGJ5FS-D_o6wTcMYj9y5QDKikKThaQDIzrN3Ivwxb6Wnm7X0wdb7L0uwPqGyuI8xHrgAXMMbtar17Lenf7hpUKwN8gEldnpYWZ1GBlLEKkWkEpxYuWc6eFt7YyEKLDGdf-3LXB_OjlA6IpfWtlV1OGQqnRElnHzOzz8SXQ"
region: "Szczecin"
country: "Polska"
completed: "420"
missions: "42"
date: "2016"
bg-link: "https://bannergress.com/banner/gryf-szczeci%C5%84ski-6cc3"
onyx: "0"
description: "Jeden z symboli miejskich Szczecina. Symbol książąt z dynastii Gryfitów."
lengthKMeters: "12,44"
title: "Gryf Szczeciński"
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

