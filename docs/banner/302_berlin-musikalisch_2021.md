---
nummer: "302"
startLatitude: "52.499205"
startLongitude: "13.445166"
titel: "Berlin musikalisch"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_aZi72221jH6jmzBa_bhiq2gll-RdTIy-j2Ps8sWvEq-P0BZ8KAz_DtxWa0HjzaRV5r7n9Gbv5prCmv3nkyf9GqOrIU8pEeoMIVF0SKDZvlZoqz7ixgEC2t0TM96wQDi44CfiKAp8lXI50LY743gBy_HiEJjKm7xU43-6fggrAxfWt0fcdZxxp0Z6ZNWeedpiomBQ_ozrWU8Z1aQbiug7-rUaAPyjQH2kGk4AAL5vT1frdPizAjqQDI4dT_DoyJJxRb_4uA8mw_OWAHtQ4bj6hbE5iLo14F-6WesahkmTjbefpV-wQjUfztdbHqsRb3cycBeyOXTTNEWGI_spCRDzq_Ce7b_kU5f6822X3T0Z3mWP6XDepNk7dK5LAzEb4cZZle5CB2AzoDLUpJKICyouIfsZKo1UqWiqljVp1g7M3mhqWwmzPUaVhK6wjd1yM5fOp_OqMpehMTpHU_ZNBSYOWQbT9kBTEXUmSlrgPgoIGFa7y5-FfqQNfEobPFVVA-JKP-yBy3at_fsqx4l6nMwjGpOT2NjT8p2BPqtOUhoD9_MkXi-Cm3Hna1KwzpZQG6d4jnlG7sLJanIb8NeTijARDXesbjWiwCwA9uO7oZYbPYHFGtZLe_T4rX5GSVtwmscUH_BNjeEGt8zjAAhHoAnBMUd_n5lfHPgqs5l1PB4eo0a9f0gM8m-lmcTfdrq_yuz6zK2C1Am78ABo1oQR6_IPsHnlK20rLr4u_0gZP9CcB8JnhQyZ8WyMS7e2rVV7qm33wJiwoSdPORVl4Yix7eVBvKXqlKdrAQ1BhvxG4pfAVW5Dg5PRW3gU32xCJf85nFsgqNvX366KCNZzkUXdPfZYMzrtQjv4jndWlc"
region: "Berlin"
country: "Deutschland"
completed: "7062"
missions: "48"
date: "2021"
bg-link: "https://bannergress.com/banner/berlin-musikalisch-5b7d"
onyx: "0"
description: "Auf dem Weg vom Postbahnhof zum Lido. \nZwei der besten Konzertlocations in Berlin."
lengthKMeters: "15,82"
title: "Berlin musikalisch"
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

