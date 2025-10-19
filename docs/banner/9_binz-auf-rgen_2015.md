---
nummer: "9"
startLatitude: "54.398545"
startLongitude: "13.625131"
titel: "Binz auf Rügen"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_YbPqra7Vy172F9RsHhOBR4e-dhmyNlnMIiTANQb3P56E11GvXmDZNdq8InXa8oc7c6q-vsNvEmwOSXV4CP74pkFIzhdQ5E8SbUsQbEWDlpJfb69ZjLSHNP8vEsLFEGdPPWZYp31fBwoVho7WSeCEZNRkEHdoHgVDK67QhNnC-Skx4gKhn0XndcaAqyNSXaLaPBBEyPaD_B0UQGtbV5FYIRhSfxFzBuXIC-TzVPvKL4tGqZ1FP7xKjs64VLizEYgdR7mIq7_oIOMtTXn_zT1a9RQNdqc5bnKMGLy3MhA_ZWSuS1Z9CiiLNIRachAW4_-2-Ig7FoP6bnU-dMYfzLQkYFUMmrkW5PmJ0mQIRVwCbN1q4ZQfvT-4KQf78D8NhxHtzl-hG-3VdAJO20liCM0kmrfOFBW2wEITCjm-zvhgf5yaTWHbaofxd-OxDwxHqgP_QsIzRPd0xdE4I5PYdQUu_OYQkTtsM1LUyWbUfYyKFAR0P9A2tGxvMMvXc8UGzaT_GwB9FU62cj7ajTpX7URiVW0E5ZubeICk0EFPdybbd2w3dvHexKR0q48sQisjZM9LH4gAqnK5K5-a-a4JYKm5DGPrkZDmXIahovVS8WQZmJzLKtzopYBcD6VLLFoNNLgcvLXn3p3XV-KsrkQ4A4-SJX7Y2r5_WdTrPknaW6cuGpJpgaOSSxARDDgS3FwozVX8hHFo6qVg"
region: "Binz"
country: "Deutschland"
completed: "198"
missions: "18"
date: "2015"
bg-link: "https://bannergress.com/banner/binz-auf-r%C3%BCgen-2ec3"
onyx: "0"
description: "Besonderer Anziehungspunkt ist die 3,2 km lange Strandpromenade mit zahlreichen und liebevoll restaurierten Bädervillen, Hotels, Cafés und Restaurants sowie der Seebrücke."
lengthKMeters: "9,08"
title: "Binz auf Rügen"
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

