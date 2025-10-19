---
nummer: "211"
startLatitude: "48.116477"
startLongitude: "11.502844"
titel: "Westpark München"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_Y-mj2--VegCSJpsNQQ9YI-bQV9p6pwqvq6s5FUdPr9fEwrisH4A1BR0YFEBOuyEh-wYeq0LjSG3siPFoW5mnwnaqHU5YUHFe7Az9t22Vzp9WXdjk-6SHrAzUeLeluObaKpulMfiioVLgYynHvN2jhC-jNsA-9WJF7soV7fv4ujaneHNyICo8yGwls5SwY0NoAEiYFhtu46wKBnBsIfrQJ2GBhyyd1whyxgtRFr-SEsa0UICyBqW75WKs5ZWex2qknBMCnYBXfR5PAwsu02lBQOW2hJEjvX-sNciCjNfoe7K9LlVV7J7dK94_47-tzWeXE03Xe4gOFm0GCuGTaaIMSNfv8ogb6lvhlFhqDNF7ApqXa0s5l4bhnE8VWukOFa-fV5Lywn_WDntZR8C3JthNwHIzgAnPdAGPpSu_uosCCE3iEbXvyzTBkQ5AcpI8UW98hWQSi7Bkb8w66tBlwEEijlB2nI1syuiJBoeC8T3chC1HNPqmaVPmo6a8I9VsRdrqXD4WpknQaRTAKgDqXA14zERi04nBk9vO4W06X9kGF08zeomvx31egk5eIsptc987HJnJ31BagAX1WltUOul9WVyLMS23qwh5KXcjuxVkqE6OcBn25xLS8XtFJ7nEx9jvF7MrnY7x9shgCrh8med-wqG7YtbydCuLebkNDwpXWmomdOGzB3NAmjCm0C-IVM395NeNYWIlvABrI_H8kjdR37L1lUALfDwJNCvGLUKdfhM8RYjDTRBqcGpTACxC50OcKAxYefGwlFoiWN1p9xaz0UKJHLVXUPuP0QDhE1HFGdsLPgpCnLDfbF8xtPrVzhS9UPC-f8NxUARP4WBXA7dQJ-Fzp1R1zsWeX0"
region: "München"
country: "Deutschland"
completed: "5136"
missions: "24"
date: "2018"
bg-link: "https://bannergress.com/banner/westpark-m%C3%BCnchen-bf4a"
onyx: "0"
description: "Spaziergang durch den Westpark. Start ist an der U-Bahnstation Holzapfelkreuth, sie endet am Harras"
lengthKMeters: "8,73"
title: "Westpark München"
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

