---
nummer: "59"
startLatitude: "47.374226"
startLongitude: "8.542888"
titel: "MissionDay Zürich"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_Z6rH3Dy0dak9B1j6w3D9mh0-LqkmLx9USbXvj_0PMDvhUB6QVTLYupCFVEFol-zR7-G_wNguQXdohtQ0BUsnTIl76tCgBKKWQOiAFP9AcCgCNXUyjWf8qOoOS_G5LpCftZSwq4OezHrBCAl5hhTPToZSIT3b3hSIXyj3EmCmjKbWhaLBpsMDRf1a6TQIiVkRL2bzdxjpu9morfCvy2wEfnTM8Rqg5lChMdZm7HxL268LfHhsxyhDoxylV3dvrGYTcgMkt6xJT24DgrxBhlCIVo0h3rhBzD50pga7JKZKd2wTOx1Pzjvy4WXvSSsDwQk7_fX0v2xJNg8H9ClVuGHJa1GFPwwQS7thYTgyEcc66cf9ADvfKbeAPbpz9AahooXdOklJbiJVEZ7isCeNn9bUa90MV-C7guYj8uyZ0344TNEa-7v87pjN2B3CL2JiL220pzTkHcg8cVVWX3Y4R6e9SO74lWIhrVfbdymjJzzP8ZgEYgXphu0r5meOBTD1U4pgOSQQT2d_GL5gPpWSIT5-YEVqIvTdljyxf4EeoLZxz1A1kE04PRlKfQoUumdn2MlBpwYQ-OwbV8IicMGI5TGPGu9fLU-P3BeiCdHUb4ityRFS-u983uCuwivPxPgCtrXAfG6RXQr43tBYPAl_UAEPecZNkH_b1UUg1bxqnu7d9HRsU0LpqJDaX9naL3iBdbksKkx49Gxcr3OtqkwB9X6o2aDDRjIv9MlPd_E9qVQDs1tj8rSM2co-C_hEVdKow9CWSH9_FGn_kYkJPyvkcXgzFCkvqt4GRq02khk9J8pHv7Me6hLmdAEV_EEOZkjP4Pldmb3S6rA84nkqbGS4JcLhp493yt_VPv2TgC"
region: "Zürich"
country: "Schweiz/Suisse/Svizzera/Svizra"
completed: "1344"
missions: "24"
date: "2017"
bg-link: "https://bannergress.com/banner/md-z%C3%BCrich-32cc"
onyx: "0"
description: ""
lengthKMeters: "20,03"
title: "MissionDay Zürich"
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
- **lengthKMeters**:{{ page.meta.lengthKMeters}}

