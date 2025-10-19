---
nummer: "269"
startLatitude: "52.512688"
startLongitude: "13.411233"
titel: "Rainbow Bridge"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_ba1ulQYC_ImJVk4pAxhio8o6sW-Wb4yOyulh_6RCVATEn4ZlBvdsBiwTcn3-5MkINMridGXszbHuiTqSIMNpNgvgQt4Pt7CNYf8le6bqaJrP6BxOtANPCX7HfBkxHuklnunky3ivNfvE5yTf4i3rS7VNwi-QAXIkpJ2sUQcUZaFN9KXnCuAq4NiWkhQ1n9RiWZ5m_sEy0tF3BOqjxlvBp0cuO9IKK1UtGL1Szexn-iq0B-rA51lf4uZSdxWqzFOFjw67cRZAFrmlNZ6yq0rXiotkfTVRfxyom_U6SYE9B-ovXb6e0XHkr7IrCKmA0yezlAsuFDKw9Xlrt--tDL-UD1j3__QadR3ILXbui6qoX-ztyLaQk3q6t4ny5f-4txaegguRFzCEs6AQ6NoU_j4IbhnJXGydgZ9DnVKYGN01ReIJvnHX0nP_LrpggwNCpNMfg5NgXsWv5pY_WDM1qV1-EHfxBhtWGJMfKdgcvQlt1TjfcJdO95k3IXi78dkKKe8ymSJSTrsqPI3YLacu1rjL3lWgDaFzoEZaIwRJn-UOtjp26No9y6LkK0Hbqi6gZ0NO0DUOTwUUR0gRYYEelKZDVtufp-ci3UnU53IMq_zjbt7hf24niQ7BpSgwnBxsVBGLe9SlfBnHbw1ywZpYNWVnVEB98L3UBD7g_tHSXNP1-TgSweXvHyr6rOHTCi7nM1uz76sgmeq99pFEbwX9GfyW3aQ5ZwzZD3qawZ8mlw5h7XWOx-FaAS6A4D-9O2_tKu6aNF9VoC0EHpRuHrQpSYC-d4rptk0oofY29T1VkxF0f7WxVwz46i-D7sI9pw3Hu81a4XWPSW9uVskikYxUju1LpmqZyi6JE"
region: "Berlin"
country: "Deutschland"
completed: "6354"
missions: "12"
date: "2020"
bg-link: "https://bannergress.com/banner/rainbow-bridge-f3e7"
onyx: "0"
description: "Make your rounds in the park around the Märkisches Museum and receive a colourful picture for your Scanner."
lengthKMeters: "2,53"
title: "Rainbow Bridge"
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

