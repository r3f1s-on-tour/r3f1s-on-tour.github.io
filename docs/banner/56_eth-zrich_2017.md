---
nummer: "56"
startLatitude: "47.373046"
startLongitude: "8.541374"
titel: ETH Zürich
picture: https://lh3.googleusercontent.com/lr/AFBm1_YT-sSZwV1s8mgiA73-pQQDBM6MHhQUbSoKruWVbLgj5G8TtAcTDs_vPr0xBp3xnkpjNBtCdZtufiiUzAQDj61pfNf5OM88cONE_xIwlxIPcOCG4_J6HR0LUc7-lMdIuu3xVpQM8kNRLd9wAzEX7TJ3Uwy8YHYaLb81psaioNdh9DqkEDNfTKdN9YtZvScS7NKe90fvhUxxSifRlCowwG_rp30PehKQaRSDCH1b09FZc7NAqbUeDJM-p8R69ljfsb1il5QBIdbxPmF61EuEnGOt3shvFQlN4DAXidPs1yovVxIMFb9b7Lmrf6U6sqWjjdS75Tl1cv0c65mwKfZLLY5fVNSDI7FTQkQqCJWARdAKHboXERI3npk0I-rDBzH4vivq5qrR8fI86nUnoG4Y4zkoaZNbLVM7eJ00q5sLUUepsyzsddKFFQj0ogI55vmrKdLU_498qnqPEY7LwX3izKkN29M1AjDeWfXWgCHersP8qy3Aexym7mluf31cmk_6aRIJzI8yHk06VnBJb5CsEAQXUb4BtKt3G1QX-S0rhivWLQ4Iu_x-m1EPjaI720Eqbn-ZsPMTvX796c9fZbqCJk2PbNSbsCY2-Jfo1RPzh2NAOl3TFBrC56Xr8hzqFXkP4jqscdylRiiToEryeKWr6pvpVLgkNRAXhanSXkGj1_4z5W2AsNC-T_YELQhx1BvgmzouRRJtwPlSrUIXagLl25M3MCgMluaRVOz25NR89t4oV1vRL2DSpgm_ushjNkNLyPKFTreX9arCo4wHxuKMgMYaV9iB3XZ02onOaN_IL0dlv5atecWMQ247BvJwWR3zY5NwkxJbdlbhKtQiZmleNZBzp2ycORPlT4hz
region: Zürich
country: Schweiz/Suisse/Svizzera/Svizra
completed: "1290"
missions: "18"
date: "2017"
bg-link: https://bannergress.com/banner/eth-5c7b
onyx: "0"
description: Das Hauptgebäude der ETH Zürich wurde 1864 fertiggestellt. Von 1915 bis 1925 erhielt es ihr heutiges Aussehen.
lengthKMeters: 5,41
title: ETH Zürich
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

