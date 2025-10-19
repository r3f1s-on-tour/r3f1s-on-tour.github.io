---
nummer: "34"
startLatitude: "49.461617"
startLongitude: "11.025122"
titel: "Mission Day Nürnberg"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_YP5SkCj_PHd37DF7rOcOdLAPHNqLVmlFcTkT9Me0CMD-RpoFVZQq4zlRy6sbKOh-52kcc9042gAsm0fgETZPtif0yPFxH5JjWAhKS_zZc09O_VUx_1WgWVSR6KHBPfhvaE_mODryjXExpkWteoqhIUcXIEfHLw4bkQNv5LXO3vSFgInKKX1cc2LWajpnHKwhiqi61HMawSbyfa0rTO9Uf0TtVaNJ-_3LC3qZpJ9u_1784_d2ufOZhDstQIJvyzjBf8og2SX63wBrCE9fFAq6fflMSHlJ-GJk2yzLXZ7qywppc48jGhNhQEoRzBSO1EN5Iqxi1LOGeVL8qfahLYRCm0BgzdpPT4AYdiPNMqbDJcEM0b-axrhDAadgj0pDK_-QOBKH3nu4fdCecES5_wbfyLXn38C3_x-OjEB-m-X853oFC5CuWaULdoa6NRNhEy1EuBq2uPgdIzJR_qWKsDel54k71Lq-LSyxQ--oQJbJ3-wy4ls0DDAmgwo6l2yB_m-26RRt5xKYFcVvp2Me3ouJp4L-AzANo-s8aWrIYZ4rkfsoMxAr5PBnUXOt1raTU7fhArQK87nRDpqoIFEWxjxq8OUrmP-8D9lkI9jmzbY6vb94e-BsTLnF4mE6IMcWB_0oo6gUw80OMykn7AJLhqSh7-V3rIsDR4RIUb9F3yFXjyW06I7FSSuopJ798IMFmcEDNMfdcStMo2fqXRqaj6IzXhJzIrUam0DZhgaQAXgayPdDF1nvnaFHjxXUm1gBb9jkWfkavjmGtgbAy6yeYgWD5b5X8EjCpWKTXoisRwQ_8M4xMjln7kAISlRzsAy9tVzPjagGZxXeTV5DPcg-AdnAMi6Gt22k9L_1sY"
region: "Nürnberg"
country: "Deutschland"
completed: "684"
missions: "12"
date: "2016"
bg-link: "https://bannergress.com/banner/md-n%C3%BCrnberg-2280"
onyx: "0"
description: "The former AEG factory premises have been become a lively urban site with IT offices, workshops, photographs’ and artists’ studios, exhibition halls and last but not least Nuremberg’s FabLab."
lengthKMeters: "31,10"
title: "Mission Day Nürnberg"
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

