---
nummer: "427"
startLatitude: "53,625655"
startLongitude: "11,417381"
titel: "Schweriner Schloss"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_Z32aWzWZQ79cmsmea8nobgPevIQ4KExjfIEi6O9UFGOwDG6Cpx02UujNVNHmuZIMzzL_LuoA_fzGFLr3E4i-XP0cn7H3Gd6y9hYQrgw0_3TZkVQAImL8fbOru9uGHquI2SH3kXLpW7fxt23Yj77qUD6F4S5ZzdmXO4tKorgbAIAwuas3BlqygmA84eHIBX3xrmElF9-x5-g5C2haCQntjgJi3q85H7a5w3y-tkNZj2SavgOGHa_7wVzMX61RU6iwkFhkeBAg2GEpnP8wZgP8ZWF_f_D5Idh4gNDeoQLsQIL6cYCfHPIKNXdlikiM8KWt49Xv7VvjcNlrCpVtP_vVt560l1lz0lp2_sY5Rbc36k8uH8VrTh4GqWomWilVi2hANBmHnimX4DnTiM1-ZBtQJDGAmhPBE_Oj2eZtLsOTE69Ci2DP6TvHp682lM2RgK1Mc92GnF4rdz6AfSfyExQQGSZg1NonsBxOajX1Srn4EnY5L1s-HEz1sU2dZh6xM6dw3cppQlVJ7wCf-9OZ-ay-diYXJv3jT_aBHYtwn1Azy7VogZxrSENX74aD2FyIxRQvGf5sRqtPArWIsZHN6hYTK8zDNDpo3SbFfafjeizwYvFgKVeOF8BD3pN1mvOiPikry_fiDCJ7BTUy50tbD3p8yB7lIGUzaMOcnZJDk-hreH66m6WBXSHYvzsiqHdlzVhkzZAjs63UWdXjZieZswmEbRwjHHrUxlhYQkk-7rwWVd6c0wVY_HwRsieicYeyKUnMEqVD0CbexBRzuGPs86zAACyXiM9YhW7t9H5nccpFBN1THe9g_FgyOkYfFdnhThWD4a6UOEnUTIHvoPiF1VYEcQkwsTkHbkLXSZLO3Dug0Peyp1_3-mTLm7BfdGbb4o_YvxQhAM"
region: "Schwerin"
country: "Deutschland"
completed: "8.904"
missions: "30"
date: "2022"
bg-link: "https://bannergress.com/banner/schweriner-schloss-8ca1"
onyx: "0"
description: "Nach Absolvieren der Missionsreihe erhalten Sie ein schönes Bild des Schweriner Schlosses."
lengthKMeters: "18,13"
title: "Schweriner Schloss"
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

