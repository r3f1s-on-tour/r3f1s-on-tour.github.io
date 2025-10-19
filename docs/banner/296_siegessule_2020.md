---
nummer: "296"
startLatitude: "52.516489"
startLongitude: "13.380383"
titel: "Siegessäule"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_bAAXlbz22OnKWA-2wvtYZESQpHZ5YN8SPkYluOXOizsPitGrtTJie_jQUTDXQMG3RG3BUVWmvd2ZFyhHXYQMnOAwa-I-_GI9Q61rlrE8SM9Untmy3YjU54E646LjGy3F9hFOxUf0uBh0E6P1hM8devyyEg_fOC7PatGEExqvYWvr9MUocLhrsEX3zehOxuOZJxr8YEwl5klaA6iwvV8Zrbnr2-gK6Wveko7uq-7Is-4ZDwXQ0Dga0CVbsme-0UkebaC2Th_5QV8sh8eoeT2yJPTeATrQ8CTc7BSfvef5wAv_axeJUVxVvBwx8cs7DtJ97CUyMFQwhj9JjvGUpSka0vDJ7t-eCrB8O40-cJuxIOfUwDmhO5UU502QbZwxyBvLfNxC6ZkTU3hBcps6m9KJ3daE-Hw5fr4sQWox-PixeDfmnSGFGjoxWW3JlvEbYJnl0Dip5M0lU4XgxCCnfjezfJFpYW8srRsDg-CvFtMTz_Qgciy7MRrsvfRJh2HPONv9UljXcsdI4JEcCG6U4ZzF-W2jIWdIz4gMESV-PPPvR02ESq1MKNO9GYBDv2Cz5SDcOq_b9R761q7pAGd9VIJ5g04od5NTdxhk3KgfctA5ZjSdbXLdjK9EmZ6sqxjpMS2rsOQoF0Hqv8GLdLLKWoIgEMq44vnckex6aA1oaSGK1hTFWQA7VdU8upagkoPfR5FghEE2u2PyIqlus14vu9dmCFR7MDyP-o4U1xYeAdL6nybgORealqaooy1rtsK_QbXvMigYl2GHtQo8ZYdHDX2-9ncoXn2jvq4PYuRc2u5wagSkcEdmr6-qvi0ApD8OpbThRtZRG5zA1cKQCjhom2-C8BhLdV7FUHBgj-"
region: "Berlin"
country: "Deutschland"
completed: "6906"
missions: "60"
date: "2020"
bg-link: "https://bannergress.com/banner/siegess%C3%A4ule-ebae"
onyx: "0"
description: "Mosaic around the Victory Column in 60 missions"
lengthKMeters: "22,20"
title: "Siegessäule"
---

# {{ page.meta.title }}
_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

## Bild
![{{ page.meta.title | default('Bild') }}]({{ page.meta.picture }})

## Links
- **bg-link**: [{{ page.meta['bg-link'] }}]({{ page.meta['bg-link'] }})

## Infos
- **nummer**: {{ page.meta.nummer }}
- **startLatitude**: {{ page.meta.startLatitude }}
- **startLongitude**: {{ page.meta.startLongitude }}
- **region**: {{ page.meta.region }}
- **country**: {{ page.meta.country }}
- **completed**: {{ page.meta.completed }}
- **missions**: {{ page.meta.missions }}
- **onyx**: {{ page.meta.onyx }}
- **description**: {{ page.meta.description }}
- **lengthKMeters**: {{ page.meta.lengthKMeters }}

