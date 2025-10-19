---
nummer: "49"
startLatitude: "48.140735"
startLongitude: "11.599442"
titel: "Friedensengel"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_bDBwdbGMbyufjO5K3UZPQBaIQ9UKMIIHxzI7nQXXymTGpX5EuhrdmghzdA7mMv7aNO7_RiTNWtIiLGGDbNDGrKB84xXdWj2Zz9rJRmif8NbRbctWyT1s6xADrItjF1bQDybGzbz8jy6DH1mBji57W96wdBGRd-aDed0OjY-gk2j-suMZADntXcFcE7Fuoe25QzxxTJJcdaNKT6Tvbe1mGg75EMxa3N2kTidklmHDZAV7oTjJo-0HfGrgPA1Fm5_yhX7doHNIiBTL1HdC_qH3ilrwEtFNm2T3Wa-MQwYwfA27D3ONWgp2Ou7d3dq39QMSVDAIK8zN0LHrdnGD0kKqrTq5a3G5WeMgzycF0nuKkGG8DXpsJ9b6ajt4HKuyrXI0bpyRqg7TbN4lkMRksD_3-dFcjX_KdEEBhoI-gJ7CuRgxAblv4jqEZ4B3e9JmudiUcTfQO0h0T1P6MT_VXT9dGDsmo3VV8kYaYoj-Nih_K9mt5U3pF9ut8n1jca62rmGo9zPV0tjbbD5tuFOa4dk_d9PmBBZLUMQrk8TBqa2y86QAToSiuPSE77ER0U6FRy4DVB1ZNASw7KvkHg36RZ_kiQSuy2v6o9un1-S97h0l3rMSN6hdVaYp_s6w672vU9sF7wqpZgLUwDFObuQZ7BtsPplUCHKBqDKAZYR554XP4t3WMwvflDwslE1Y-_uOIKZOQHFEmxI-iLJcdNptprLlxXejJ26Tsva2bWHK3ejIDqIvRT-zxNnym400ZQpeVT5kiac1CNSQx8Njp1Z1LdO7DVhrlxPRXYmnuXT0_i2FMbuBeisMN3XlRWQXoxzNG0WsOjUgMWjHSpOx26hStZ1eNYZhs2IUa1qnvE"
region: "München"
country: "Deutschland"
completed: "1140"
missions: "48"
date: "2016"
bg-link: "https://bannergress.com/banner/friedensengel-8105"
onyx: "0"
description: "Der so genannte Friedensengel ist eigentlich der griechischen Siegesgöttin Nike nachempfunden und erinnert an den Friedensschluss nach Ende des Deutsch-Französischen Krieges von 1870/1871."
lengthKMeters: "13,40"
title: "Friedensengel"
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

