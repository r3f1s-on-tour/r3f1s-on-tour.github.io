---
nummer: "174"
startLatitude: "51.866831"
startLongitude: "12.633432"
titel: "Wittenberg Art"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_Z19W61WTs_wWPzwLF66Ng3qkCfQX5JI7Uj6HEqqLwPaZk-CYwHWhdSjHrJo428Rbc1xXgNn_tVA44UmIc0OM4yOggclHFQg84Ut79li-wP3k80WhGpAlKkd73oZmfRoN5ta8d3wdec5IbS3jecI5qdsbs9p9CxZukNjT8-6ABI-MyZCYjWKzibWejvv7H5kEHX5gI1XiSYtAPsmxyX_QLMfzS5ZTNiswwHxVd_qDNWacqjOWNzwArNSmFAb6_5sEHK2_yXk5BUyc8Euqb_ewXOxVjudkHVMsVN1Sn54Apbhr49V4XDGhLAPHNCcor84f0PLtAA7xuh3dTj2Y78TliBngDaaDRKvoQn6z4HP0kMP349mZ4lndc9IQG56-02QO_9C6gFwTKGX9Op5QJpbK7bRo0bOZ3LapdabnEDA6upaSthoLV-Bkfh-rbVizF3Tjt-fA86OsMPqXo6AqHfatRLQywyu1kJR4qHtq6Icjqz3hox1ur6HMbdsJgX60n6IgPoelfkMt5kuqXRCDCRnkyIAAsH7A1fOw_ugy-4ItCappN4oTyM-MzP5DP3T-XcSUPnzTD3TCrWniD7RlxkGNSIzHE0_EfXU3Fd_2ZC9qQu2xpXcxFCQjeBxlivQ3TJbp3E57vOWQ7zH596dKgFWlkXpn-KvjZEMLyj8NeNcXy2-tR4e354OXkZEScc5l6mOdBE0_IGC38TPHi8qSQp85yKzJUpcT4DYczdo_bafYtgnvM1iHHUOH29aGLkffzEQawD3ClB_OCSQjhXsQuyYJBL10eoL1tXzGhd11LjWx8w1aqtljR3jQg6SQG5vo5tcFHlPOlrRWIXb6sFaZhzwt4bdVVHnck"
region: "Wittenberg"
country: "Deutschland"
completed: "4182"
missions: "18"
date: "2018"
bg-link: "https://bannergress.com/banner/wittenberg-art-1499"
onyx: "0"
description: "eine lustige Runde"
lengthKMeters: "6,04"
title: "Wittenberg Art"
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

