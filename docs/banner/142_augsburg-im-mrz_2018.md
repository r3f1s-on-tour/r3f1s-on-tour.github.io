---
nummer: "142"
startLatitude: "48.366462"
startLongitude: "10.894585"
titel: "Augsburg im März"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_ZEU0k3eQ9i7Al1KiVaiEsYWH0TeL55umnvtKzrCps-5ooKVOyH52YFSqOx_hmjEQfYlg4q1QOX_Ld074x2UXOqyKFP3-bCJ1dIQoSEnESBF3M9eS3C84ruvUBmr52mfPGElWEwW-7APWAcTHy-J3Ar3HzvVPvE-q4FG8SkiOMfdhJpB0sA1I2CSx1Q3vJIFHxAkDed6m10cEbfdXuISUaolj9bkkMWnbE-iJ808Z6JTyHE38HhGbbjQ2yKtOL-2piWeAIqiSKTJvfqong_oqThmzP1R8GoLNXu6GoITXt823IZBwgYnyW_6wr6yoM3w6EHIE8VoEHjBM_BrIwG3WGNzDrJrwyQUxtMWkn6vbk3GhDpzQ8FnCy2OqnGk98ujsnfI9m5LU71oUA4ze2c2NhFSln83gg6ngNHpf34Rq0FurK1JlXWv-26NeSAC_FSMQmH-AFMrwEkRV_8-pXP_f96MmZBK5vRH_WeauLNYTsptnrOqffeN1bnLr4yBS1CEVIZY5At1Ovb8_07V_xco5_yWVsy6nv1Pd2qoeMTK2FIetK64ihzwIyyUj-Q2_Bj1iQXqNnZmyE7a4cIBtz1G1hTts7WrLvrFvj1Vud87ttzM4mvl4_c7Zaz6Zntl0vrj0uklhW4IvPtEcBbLufuxs0i2ZQhL_j025WEFeqUgOWDtN-zh8X8SdpYKJ-4PoRzhGc_E52PWhtOg_cCv2KWmVZONZp0dTWjEUoyW3nsGdLu3exO7TIW93RWE2pR4jbNNPQltqhLc_M1SHRKR6YHdzVksvb0rwxbL889F8sC8js0SoPA8bL7EoT-mfipo79dO50DTnhd21hhVRuK8Py0xgi78ZpKp5g"
region: "Augsburg"
country: "Deutschland"
completed: "3396"
missions: "30"
date: "2018"
bg-link: ""
onyx: "0"
description: ""
lengthKMeters: ""
title: "Augsburg im März"
---

# {{ page.meta.title }}
_**Datum:** {{ page.meta.date }} • **Country:** {{ page.meta.country }}_

## Bild
![{{ page.meta.title | default('Bild') }}]({{ page.meta.picture }})

## Infos
- **nummer**: {{ page.meta.nummer }}
- **startLatitude**: {{ page.meta.startLatitude }}
- **startLongitude**: {{ page.meta.startLongitude }}
- **region**: {{ page.meta.region }}
- **country**: {{ page.meta.country }}
- **completed**: {{ page.meta.completed }}
- **missions**: {{ page.meta.missions }}
- **onyx**: {{ page.meta.onyx }}

