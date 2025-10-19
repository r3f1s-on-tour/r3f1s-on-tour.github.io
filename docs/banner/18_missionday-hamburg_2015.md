---
nummer: "18"
startLatitude: "53.552386"
startLongitude: "9.993663"
titel: "MissionDay Hamburg"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_YpLRCD8EL4fWrYkC5hiu3fzrch8aW_bpTAqfSjUm4Y5ENvuboVBnzKYfH4KqweTlmLHBFXsAcyfRjtafVg6Ry82ob-NTRAaW7JzWU8mpeMtwh9ELfLmcicAEfCdrwcW9Bl2zjfbTfZxZyO1XrUIm75QNP4qz5B5z_ku2K64FGz8CxkCaaLf3jckeQMePbiKRTak9kPZmXT1SyBNcAyLOTMjWlBElNgvTWa9iuUJmxA72c0ElI_2PAjOd6_wAYHertzAnlIQLTTorJTWzQ2-jF8TiWlt4lBfLJMFdxKxhuC7EDF_E3Ht5r0bB6QGMpind3S6Nk73VjlhJgi4ohm5MUUifqK-pySRs11Z74squzuoWPR_SDChJKgzNCNuWe7nJhD8OVXBiWQct_WbFDBx2n4ZEIOkM-Gfs4BjAaPmQsAa-z1dlbfXz9RnmdrN65ulGAteCAkD60NA0gCE0sjX6EhzFNo0ZzS4amGVwOw_bHxbs0sgjBDxTxs2FIAoal2f6mVAGRk91OzEMhnMMkDBf0mpU4AAvNCGZeaMBr-jF3uLaDaVhNsg8JN_6MYsHRAPaXQG58iir4MFaSzSaCdjmdcXcALGhYjbbsW8H-LgIdO81HqAcLN5602kKyWkEmT_YdFsz2p3JRSTjrMDWEOqXh41lhppEkceSNkqevmVEM8NUe_x3XchuBkCsCelQXz02TCJGXkcg"
region: "Hamburg"
country: "Deutschland"
completed: "330"
missions: "12"
date: "2015"
bg-link: "https://bannergress.com/banner/md-hamburg-0950"
onyx: "0"
description: "The Alsterarkaden is the smallest and oldest shopping arcade in Hamburg."
lengthKMeters: "71,95"
title: "MissionDay Hamburg"
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

