---
nummer: "422"
startLatitude: "53,565661"
startLongitude: "13,260573"
titel: "Tiger of the Year"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_YKrTSeaC17B4pfS2HR-oMhNuj6yXXGqnHwcaHLAAN3o_y1DZc48cDN-oXCQrq8Mx_9ngu7mzpyI9-c1tiYCMZJZ5RPO2tOVoeyQP9-6pB_Tsy3NkJbqyoG6OucDcsD_8yWrLeWHurPDnNPI4Y1wNK-sv_SkJNrHmMwKfLpazbRnAK2Za4t-sVmDmOYcj-LEddrtXXkbnJPmjF_0d8YfpLWuWHA5XYHokFLSS_JX6BsjmhWVNfE0THgFzJzKEOUgbm4uiG1Ag3-hjPcsViwzadjPxBocPvYsTwpwKB2vo0jUUWq5EYGHnYNY4_Q8y6gwmbFpSP-rul38nbEeSS9l-ZEMpogV2Qvq67E9_Cc6oEbpfnWP--NDS3oY2qOBtvXQJU9JYik-Qx1c_a6m5vbafR9CK724-Q62PEFDorsi50hOhjN7TXJqz-_-O41xpWg-BCr7ZUtEMO-lWTZLd4oUzfXrCSt03EH095-9t_e9hZMUZ1DnDaQzE_kSBIQGR_vsFkC08GFyy_iGAYx6qzNGkvlBggtcDkJV9f3Dtkt8jCc2o4UAKwTewldBfCKE7ubRjgWbO0x6xhR1GaKnTtQj-ZtwA8VPIMHoJOdVZMEl8F0kqBogvvtqYAT6dwxiLb_8yJ6qgqsqtaSxB-W0RXqhjEn-oStfFKy9LTJG8E9XYzROrtKMX6McWnwDm4AfmF45jemp74zB1zCgujEHZPl4UvmG6cfxMhxTK1Vr6GE4L2nXsQhyaqIZJbo0blCL1uGv3fa06ccI0E8SgYl6G2S3CJoVYTfl9QkpNdRNSjFbdqkC05JUX3aPii758cB33cvONerTCXjn9P1ASYkDNiIdJgFL0OziYcJNoChIqSHmexN6jhOoStpCfn6HFjq4yXPBxpHhkIM"
region: "Neubrandenburg"
country: "Deutschland"
completed: "8.808"
missions: "30"
date: "2022"
bg-link: "https://bannergress.com/banner/tiger-of-the-year-15ba"
onyx: "0"
description: "Entdecke durch die Missionen Neubrandenburg. Die Mission beginnt  und endet im Vogelviertel."
lengthKMeters: "16,08"
title: "Tiger of the Year"
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

