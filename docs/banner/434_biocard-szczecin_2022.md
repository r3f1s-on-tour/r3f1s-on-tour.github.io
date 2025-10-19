---
nummer: "434"
startLatitude: "53,429481"
startLongitude: "14,553038"
titel: "Biocard Szczecin"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_Z_B_o9jOSaxU1xyRdWdaKOECYeCxq6bL-fl54qLOD_Yt_TJo-SZGDeN6Hv7ogzxiRl_cF0L1NVb2jpTAiHwxBJIzXFqoH4yOGEMBRkgOgyTFSPOGWHtVP_SW4mWjdAPwJgqYaiw20P7LfrDYBJvVJHSn4-e4v1Y4qbgwda6izq0vh_GOyhZKC_CNE8OdvZydMRq_2wYguPfdZ-XOyeryJ9UhBpcHvGoZ9bJmX4G42XE4fVfnhLElvlpEAyNXC2xxGpZ_zGnSNzB0wi0HW6ce6RPnG9RCWxg0EdVEN52R37JYkT6Ja3YfONpTvTU9df70016O3y7_qz7I3RvG5C3ZvntPXhl5WabW43q0EMeIFdLUaoyG_pcuJxrqO3iCf6WfZb31JJsO_vf9kmBHkf8rIfCLpLyYwgd55MX7QMjMT8M6DE5pZYLbhtG9nfHYPJPkAnzt8LU_N9TjCulw6IIDhvxJXui2NAZgIklrcvu9faiZb0EA8PjZpeXMXVTBm7jLmYVmYvUu8iewpl29q_IRG67pANyOi6JcFhZJJVOWh161GcMjXTDtnnsTpJnuYdzY3tJoFfNYi0HDJ5vxe8hh5aWdsgozbXsGMNaTZUKaM2Wo2CzYXjeJQMPXUANwQC69lDyBJyHjD-rWx38iSyrUDf_yEqNfhIQftM5-QjmhMKdHhH0XuS_uS_LIFtSCIIxe1GrXuSAsl-EKMHLYJCm28QjCToohS0xsifOAN60i0F9MCznA2CanVvoVaX5RPmoXjidRaqbOELodDk-cay5dvKXOuD5W8uD5x5f7S2i1MIkiOGhkQUuq23KtnX1os1zm7rPLJ78FpLzsGpz8dm8dp28foVVYQkJP8o68RrjDaelE9Xh05YGhpraT8eggGZiQuf2tle"
region: "Szczecin"
country: "Polska"
completed: "9.072"
missions: "48"
date: "2022"
bg-link: "https://bannergress.com/banner/biocard-szczecin-0805"
onyx: "0"
description: "Welcome to Szczecin! This banner will lead you through the city's most famous highlights. Complete it to earn a biocard depicting the statue of the Seaman."
lengthKMeters: "18,62"
title: "Biocard Szczecin"
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

