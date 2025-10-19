---
nummer: "281"
startLatitude: "52.552344"
startLongitude: "13.469973"
titel: "Weissensee"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_aWsVdEEw2dP8mwAk-kp4UvVRpV_2FE5vHxwE6x3f6DynvIz7o0Gr_IlDSQqGmReqWWq4GW5yAbkVUPcbPw-nxXFQ_ZOn4XFy8BQz7gX4Yxqsk-mFGcHYWiMNqoZ3AAk27N0u7Z6slXaxYJzHTE2gM0p9Gbjb6-O8x-nB0elT_qbJ9t22pMFqyLDsRjbXyneyS1rnRdGq9K-W9-fzT6jXp1EIlhlt-74dA4aSZlSCGXI8lCvpnYFgq1Dr-57ZSoZzGFuJL8jq_2ikEFYndxvVWOxZ5eYFYrWdIvMBFma_X2zC7-95z1j1mjm2938WUFqPGYrr6py7Y6H0mo7-Fd6lgQXYnpPeq-_fKcRd2PwR0jEwCHRdv20ugGvvUvJ-9GYVPlkR7R2_vseZGPvhBp9p9_CH_RSUCJ4z_x9zgKCC-qdHynOQks0n7XMiEcP25uWfXS7UQ3HmRPOFXW4aahv6L2oSC0MRwJMPAQqXYEuGUWSKJ2iliq1Tb-Ub6HyxvcYMDixYcVCYZx1EgrFDL0offWg3bQrih5wAbGA_QsTxrHfdYnkA8blbabTC30pZI5bU5RF-va52Y9LAeZ16G7jUMnVYcyniuJuiAHy8eaOS7UD6BkHX315emhuW2F2qS-Nf0bpsGY2SzIFbPws1IzvBVJvyDqpAORa2pqQtkNFwn7vialQh2fmzPyXEEQslC5NfomQzzLcjCeJPWfAbXLtok7T9myPA1DWqj_omzRtkGQksSxn7pGmuwnNN4PerGfVTtipMQr6ti4CbICzuVKxQv4jR0r5cFAGALzbnYM85ORax9gOJQzvOOZBNzckI7DkPkCNVdEPEo3XYGCJeQkfrE2dJgaiOtY-pAz"
region: "Berlin"
country: "Deutschland"
completed: "6510"
missions: "18"
date: "2020"
bg-link: "https://bannergress.com/banner/weissensee-1d82"
onyx: "1"
description: "Kleine Runde durch den Stadtteil Weissensee. Achtzehn kleine Missionen, beginnt bei Teil eins!"
lengthKMeters: "9,57"
title: "Weissensee"
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

