---
nummer: "30"
startLatitude: "48.199911"
startLongitude: "11.658516"
titel: "Sound Vision"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_bVcwZIH3WisWebXtaBAqPgQ0QIWSMnN02DiaXmvALe77ekrlcLUc41uCZS3sV0pm1q63uvgNrd5dS8UJ9roec9fjiPAUY7_9QcfCZ1EeUaIzv98bQzJp6w5-D-PVmdwTNBVnjF-IeG_RlH0cp8vpsh-rkzwpcdZ2tUO2oltp6oETmcsLehkGClSDVs4T7ovXZozOS9Ub07srdLkOE9cblKAeacJaYUELOx_EYKv_Vo1U7D7mckrejWNc6FCPePqoWJqbO-ZnH8O7IxxfP8x_SCuU4Keq1Vp0HI4tONMjFSG8N2x-3zcGGGTz_xJkOa2TCa03YexWT4LqvU7JdaH7YgccB6iytqcNrFhHY9yujuwRA3qwohKhIa4zQDelLtmg8FuixrAKA0GEQp4SV7lWwAzlUunSE4avIf-BtXcDFJdXFNPIkVLKriAKWLEthBz3qg7pHrxwX7DFof2L7dNpBA0J0jlx0ceOpkMsihdTTTc4HDPiRgxSG8959UQ8-fyBkx6Y93W77fSlq89odmDfvHmoJ_vUe0qydwrz0sWwAonOGY6tM1LMMnVX_2juMUDEtzCd5l11Wgtu23hpHoHpElkifLTeuTJIMwSTKqLZXVYyljwUkHt3qLbuuxMMqwtJVb5SJnZW83YhPTtB7fQPqoTjf7XfbbjbE4-_QxozPYcwKKK-Z6qxRx3AmBvpxg1N6_RcXhetuhPLT0IocrbzEvaMK21U3qEd6swamIfi9Cjo6nhdWTQLaiQc2mvDqttf6xSak7C-cr4dUPz_EdlKD9IlEfDPjpLuakMezLecOoPl2JS9Oy6QTfRSCG9OoXM6v9e64O2g2cTlEm0KwBWups_6ZgrdYyyi2L"
region: "Unterföhring"
country: "Deutschland"
completed: "600"
missions: "54"
date: "2016"
bg-link: "https://bannergress.com/banner/sound-vision-f57e"
onyx: "0"
description: "Your journey will take you through three beautiful towns of Bavaria. Please enjoy the views and our historical towns."
lengthKMeters: "40,14"
title: "Sound Vision"
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

