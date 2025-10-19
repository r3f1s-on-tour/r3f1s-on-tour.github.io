---
nummer: "334"
startLatitude: "54.322059"
startLongitude: "13.082235"
titel: "Tatort Stralsund"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_Y3hqa4wjfZAIGGzZbAic0wJdJkZx6wUz2jSZsihy22XBT1knr7kA58ai171zBamVFfWYyx055F7CnFmNNtGDIU621IiOaYOGfSawN_4ferWFMtirBT0FZSfgahWk-UDI7Hi7oWrwPg-rReRAXEVrjRCLewlwj9dNo5yVLQrTQ660sk69AnDIrqHZPYUKanq4DyG7nybK8ma4cjVJs6aCobhF5s_NVV-gaZoZsNMnRcHhoy1ZPCP3TLRODjR9JOCwf07xnDQkCOV3Ex_lacDL3DSLWScDqO_l7wgSFcxJTvWBGjBMqPyEXTMJlIF00_vuKQ9OkVsj5Yc1wdaJvO5zQtEWK2axlQiYR3GRZuZUdEk1r3j3QL85SKyYca7gNuwnlg_suM5AFSISDxheOXfub2l1llkf47b7oFLT5tOkPmsUVQGXVaIjIDErN4GLolROKw64I8766HOZ3ZKQWhuk6CcPu1oDWsgF2qLEDso46YT4TLx3aVBIKReuG2Zm4viqljcbam5PCZOkwvhjD-kQ2yzXORDSESCXewYeeX5Lr2g754B3QOI1SdR-zYb7pE53BLPRbXNnmpsf5DXIf0AvP3rqehznOSWsF2hA5LneFOaIyOmmFU2MDedMQI754RdUoc9R34lRCYD-LYfTMvIQ2M1VWKd9B_BAd_kKEq49ywwWgMtOgPAOH3bb-LrYPVsOuLlV_az1VAgHY5IyS3aQfItoEmiHbCn4gty21j0t_sxSBcPcKe92ryd31uURNbuBqcuK-joeW2xgVjIMYCxPL77-kZX1J6wRFORgPyoRuJGfqTDTyBnBd9QRhncB_0qBjbG5l2F8e_61REG5xuRT0OTTtJeknoHPd5"
region: "Stralsund"
country: "Deutschland"
completed: "7644"
missions: "18"
date: "2021"
bg-link: "https://bannergress.com/banner/tatort-stralsund-b5f9"
onyx: "0"
description: "Wir starten am Tatort Brunnenaue."
lengthKMeters: "6,10"
title: "Tatort Stralsund"
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

