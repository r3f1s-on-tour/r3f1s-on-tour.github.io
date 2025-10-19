---
nummer: "40"
startLatitude: "48.137238"
startLongitude: "11.576208"
titel: "Uptown München"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_Yc10-bMRL1K9qY3p097-dHluD2ttS4UsijHgmhdXxY7FnTWKzgOHmRMWpkAMwedqWHqarDqDY8t_8Q3iVT0fCwwfTFrtzI-dJtwdeugQMqoVR5eTsH2QHGEZkQ8O6_qmg44kfi6OX10TCH8PTggzarqUHZh5vH6ij5Yn-112b-64yUypff0nbg34wVrp2SUHlm8AGQegZBYXlVjl5GHPvKKrdI_BMupl4tdIXrguej64RTB6eMyvdRRC-LQm_Cu2n68I4Rqf5x_rsi_-486Fu7FKgo_m8RrczV7gs-IGiVINef83IPJyIDnf_SoiJx4qg9Qsl32cgb8u4h31qGIbPoYc-t41jVunBtWFW-MULHleC6aAfhnRRoSX-_ifQQtPx6PNaXfBxMy1oryuaB0P9f6r3WNAWns8bBUvAg0YNeEru-QF1cClabsUtKEHqnt8E-Ek6IbiJkqCsa-Kv9wyjp-YNg0iyDlNMsxEOx-lex2H7LoG10CZKDE7lWdB6I_2q-UA-1MAx3aPHE-O8MxhQqg_tFYwr1bM-Oyu0b8FE29IxdVQxYAf9BtfFBZhtsSJuRlRxUM5RDdJXmCKGRLlKwxWbzZuZ2C44siWvfeKFZdqSKxDGFImYV5dNzHZ5XXePKZiqJxMr4qTQey2rzNuBGTfXkyhqYmuWWSwykWgQuZpbLMQ1OmS6h41k8Geqbsg-uRdtC2hRsnxwFdwvfThScIVOKb7qD2olt6iqKkeerLtdli9m60V0zW92VR8VjBsT4r5EyL3sH81nmllgkx9utysfaViApOTT4BW51sH-gdtEev4ucWl1PLLPm2GdsXeQJGRswsBbvOSV7NxIbd8GiLcFiKkIRk2gZ"
region: "München"
country: "Deutschland"
completed: "888"
missions: "60"
date: "2016"
bg-link: "https://bannergress.com/banner/uptown-m%C3%BCnchen-a93b"
onyx: "0"
description: "Die gläserne Fassade umhüllt das Tragwerk des nach dreijähriger Bauzeit im Jahre 2004 im Stadtteil Moosach fertiggestellten Büroturms. Das Hochhaus wird von vier siebengeschossigen Gebäuden flankiert"
lengthKMeters: "18,71"
title: "Uptown München"
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

