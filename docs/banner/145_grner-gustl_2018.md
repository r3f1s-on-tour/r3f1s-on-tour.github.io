---
nummer: "145"
startLatitude: "48.138648"
startLongitude: "11.568919"
titel: "Grüner Gustl"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_YrR6jvNNaBGDT7XT-vudc4hbBdo_c6TGUK0pubLiN1qLmIWOoDC1pyJK77Pcy9rDiSgKeok1fjfIQQiGeZ_GZNnQCzO_Ia6YvVyML-ZEZj3y_quwxlfPIHmlgquikVsdn-tOfai4c9ZhapQrAqnGliUTFRqGIWeDiWSqeOckzaQlIQt-by0KtYjjdbqg0-31c8ByICnNaF9lBz8fcxeYuVfHILMmfhgWe93BsszIZWe9aS7iykOhmdzTuqntAmewkvfc9UvAc9CgUhdcqcTHlIDzsVjJPz4Svlf-o008BLkuG5zds4Zu9fgGYalObqzwPp8CXCMXFBBZ4u99fKUdWMzjzv8Hep5wwgeZzvk3BURdImPfUUed-x7ORzYH244nv01mHnRDGA50pC4t_Dw8Z7MT_9XSKPUfyY4glSYJ52YSbO7bGN-eaZxbDoxb64ubmYH8Ld1GFKgph_WBVzBUHKUjo8DSWZGPm60z5C_ULdHR5zy4P1xuMDBQx6S3NdFNDnDfViY1DCE560wexRt7cgZFU845dbIyNNkTpMpkacnGTrtLLeG0sNUvVIlbTpgk0H0yEQMbS5pJ4eq11hz14xx8FWo8htqifVrPf3T6taq5YYDDSkgjNpfP1ooZXDrDW3PPfFwDWnX06Za1oS-0h9lx9XrQVmO0uoZ3SvFHjREifKKwoaE2hjsjYT6koFCv4FqmpVt2bRxLbOe9xJ4K6JcYPbBzoWi1OGgUKhkL1zvlfxFmq7sAE2k-hb8wSDv21iwwQ5hF8jg4hrHpG8CvGGb5SCGxuUaLKeLr2kdWpvuH2hMxdO8fdgKhg4gEPWhesdmqAmrLa92lw-gs8grXu5RB235c3-IZ-t"
region: "München"
country: "Deutschland"
completed: "3522"
missions: "90"
date: "2018"
bg-link: "https://bannergress.com/banner/gr%C3%BCner-gustl-2b31"
onyx: "1"
description: "Mit dem Grünen Gustl durch die Münchner Innenstadt."
lengthKMeters: "24,48"
title: "Grüner Gustl"
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

