---
nummer: "404"
startLatitude: "52,535859"
startLongitude: "13,433165"
titel: "Bötzows Dutzend"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_YRQ0L88c4zOVx2MZ4pllC8g7j_zjMr_3nstgvqHl2tTUBHyFkQ1SqB7E1xnnY6AerouUf7g8-xeIyYqzX19-2wtHZu_KnUjraTNEbwsCcTiRbKL1FskF4_GoXxuc9GW6njeuCeHvcnF--iSuWMl7TOMJdRt_JsnxoflsnUKx2scWxsr6Gb4Kzr_T_n0Q86cBGVBEcolglQdSA8UW8YZBBwn-ANiwdJ-Bkwd2mRBUCrJrjIZv_nfDrs-czexThPKCKxoESZWxsCZ8QeajMGdxuHma3SZqss-SYiSuZL0Q8YbRMwOmJ2Hbf1ptfVFiP_tciMhn_jNvrwM0xXa-nCIm6HAbbzd7fXN9tenzb1lJtP_24JgWRRnz5fT8JpoHylI7MWsIbKyc3W_wSFW9oUNX9n_7XlO8TiOaP8ELXvKzJ8kpQan6KeLVwkc-v9avUX1uT1plwbfgIIflGiWFbdCdAWIObNnIwK_clCrrpH_1tm2GDv_x91dfYBOOhZuIWTGlPpwzAqE7L8eIeVHIeNYfECqQsgO7dBnYILqWK6aNfFkoy-e2gouzRVQJIQzPkQ6GBgUrdHpjVlxPZLghl_-bsb7RtkfQpoJrxJsBLGSEVolTlUebmvx9eHzMjwyoHjCsE3iSapV5tUiPVpYudV7HSreacwyMraGf2Hp1IRPYizRA0Y-ZixYL29FjavYb2aNWEXT1D6hKk8BkodBEbr9hCIEhxm7XP1wpuLjhgPEKhJ-UhMRKzLPfa51Z5WdIHf6SqOWV8rowRafq3z1Z-1M0hpPqQTmV_FyWhhJjUAhjotBGFX_a9HLj07Y8jAbnfam8n3D0Z9VCQCwoFg3Gh6L8-JMRo1sjTPIGQ1"
region: "Berlin"
country: "Deutschland"
completed: "8.628"
missions: "12"
date: "2022"
bg-link: "https://bannergress.com/banner/b%C3%B6tzows-dutzend-d1f4"
onyx: "0"
description: "Als Bötzowviertel wird die Ortslage zwischen der Danziger Straße im Nordosten, dem Volkspark Friedrichshain im Süden und der Greifswalder Straße im Nordwesten bezeichnet."
lengthKMeters: "6,56"
title: "Bötzows Dutzend"
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

