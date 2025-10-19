---
nummer: "400"
startLatitude: "52,509237"
startLongitude: "13,497382"
titel: "Catwalk Pippa"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_a6AB_g1So7OX7u9Wfu6WU1nxJzifco8ivOqgNMtmyUVVursmykBYH2J_2lSPRrF3vbUnv-sHSVryRSOWHr8Fc7Uk1hBXXklh4KJM3a4C0JTfI6IikKeDzPgaV6uymL_5oxqCBoyWbF0v3_hxb1inSmVrjLSmPWgXeC7NFGfyfqxDhxvAAhT_yiPfri_-7hDcbS7RhC7-29Gqwjh6g2C3uTSRQfa6mora8LhuGoPO3614y8RPKb21we9IsvJgeIFilAML78i4HvqethnZZoPGcm1FDbOBGyZbN6zSnzcsf67ISQH52oo9PV3w3tHTxKFpkw3qzBkDySV4mcjcTMz7xUU52KcBBXx5MLfoxCM0BHWbEJ9lbKPchDMdVP_5vmdhWcBarPdeFIbmsNVDnzJzxidbKTH6hZjGxD_F8UBj9NXREXCMg6w9qdJtDk-DRhtQsAA_SRteVVMtpdJwDAE_39ATZMfkIPhCSAUgnRcGm6HQ6Ul-qfrNsh38FtJWfGYREW4GOUhcpN0sj-mEeXjDAQ-kOf2hfcoNIqMVLv7uDdupLr4b_vpZvQ6ouRIEaWp3V_xijLqmkDOVcz9zYB3vMVOxMBXxZhXOOAUccq1yL7y56V6hVxltU55ng4u75rWuFxxEC3ymisgOMVRUScbPIaJzqhSkef3OY-TgeCZwE_ZG29K7UpzVIIpQvX8FfCARROenDK85PDqBAgNrGoNEe9AKqbMoTTYIQj6cvfbgQBjQUP4-WituY098o4b9j7joZzSLb59R-coc51S7LzOJK57RY8rwN6NCl0Bulz-UzTH4chVPN2y4WTVW_gOffeHOr6kC3OCEdA9vdnIL0dKJKOYKqqnoSuAV9q"
region: "Berlin"
country: "Deutschland"
completed: "8.574"
missions: "18"
date: "2022"
bg-link: "https://bannergress.com/banner/catwalk-pippa-9bcd"
onyx: "0"
description: "Begleite Pippa auf einen Entdeckungsstreifzug vom S+U Lichtenberg nach Friedrichsfelde und dort im Bogen durch den Weitlingkiez zurück zu seinem Ausgangspunkt."
lengthKMeters: "5,00"
title: "Catwalk Pippa"
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

