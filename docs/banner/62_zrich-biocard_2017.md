---
nummer: "62"
startLatitude: "47.377718"
startLongitude: "8.54146"
titel: Zürich Biocard
picture: https://lh3.googleusercontent.com/lr/AFBm1_YZErq8BD4iYOGyhKOhJI-7LGa_GZOYMoS_bnZQ7tPdwVQ-_DL4D3W4H2SWRR3jUWwQve2t1zW7pzBnzsOy2dyKfVnrZZfzIzQRobL5loMa12Q8bTIRjfE6V9rE1NpQRUIT7t5L66EpKFulZ_nQVkFAfKAYvnsz-FyPKwh0Y4sKOla7IF1BaN2YG_E8EXr73GmtCZXtpAJH3C32hr2EDsAiI7Bs483W8hMBQv7QsM21j9eukRL3A-4hvNF0NYVfaE6P5mOdYG0sbvmU0C4qPTkhIwDMyRInhpPQ2WOH8-VF7GqDVqX_wqFHCweuPEiAQtW6p7T_ouj46XY1K9bQN8xt2jg1MNG39I38U1vNyLXqrTeRvtJt7xkwAI_ZyU7SbQnG9w04fvoM7_oqYozAEDGZIThSGYp3RMx1e5UZJJ1AVkFyRPrE_BVqnMrZlAQRji0qBvhq6_J5jFiCq4HYD7Oqu8e0Nydmte56vnjjFNpCK1Iw0BfTAp-PAJY30-oMm-wN5jRcVFA2k5-CUassWKrVsvALvqO2AHhL9DbBJLoSczuIjsisOsM26BOz9Sjoe280mVjaoHF022fPHqI4xMc21l8HzsksxUWU7_Fea1-YunFDtalXcNl2R46KWRkVO_kfncdeiU75U12fyXezOLwxaVAa5BnLXzeGo3a8OGkjFbQMso-GVQ2r1azXpkofIO4IItHPj9mjoyZJhfQN1qgZNdZ-8raAV7D2VmZK_OR9RNiJDzSPrXbmZzDY8CMoFpBdq0X-5xrrEm_czW09GWi2TvCil96hgk9gRVnnAD9KE8Jv38iJzOuE9r2iXZal4JmWq9pmkkuWy9vAZDa0IgOsST9gnFhnvGN1
region: Zürich
country: Schweiz/Suisse/Svizzera/Svizra
completed: "1380"
missions: "24"
date: "2017"
bg-link: https://bannergress.com/banner/z%C3%BCrich-biocard-79bc
onyx: "0"
description: "Zurich Main Station is the largest train station in Switzerland, it serves about 3000 connections a day. It's the main hub to connect to the rest of Switzerland."
lengthKMeters: 7,97
title: Zürich Biocard
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

