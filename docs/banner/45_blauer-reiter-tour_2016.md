---
nummer: "45"
startLatitude: "48.146732"
startLongitude: "11.563926"
titel: "Blauer Reiter Tour"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_ZgYV0ktZBvO-b4YpL6KHL8cMD-mC6Pg8VYQ45-1EjJDb9BcP9yh1PlZIZ_OKEuHvt8WXkNct-DbUty385aQRxenqhZx0FhM-zIZORSBGYJi1giJbWxKbxCJcObzhxB8zszKv0DHcWqjTV-fWdyYNxcyokRV-pARSqXlAROSymGuBKLTHb1Z1lA0iMO9LAKo939sfYfGCl4_-VKl-Jq6Va5Jn66XE3YDJumiFc7RbKBOn02uwtB0EP67EC_o3-x1CDYTrPdXzEODYKh00819JINQf5h0TOMh9n3pGblD6mz-GBEzikruQFue3tGG_g8MI9n-JXIogQ60iwteD7sirPBSoZ69ZUn2AuRTl0hKDipHUMJkBdmZ9acJ1mPUerdEOA3pxTddAjZRI-DeRq-4fGp_ijU3XzEiYLVekOfInY1Ido7kFPiaDuHOtMMlj5gZAT2cDd_iSUZ1_JdDKVvhp0XYT_LXooQRe9K1CT05e9LTADg4sI2mAwWad0dCH0CDm80DVPmIaf-l6ZRT9HkDcwENd3xzl9PH10wICLnKrv0fDIpbn-3oPyf4h3QkyA-0KuECr5soIOAhmpvcpUCTd3nhjgjrGjIH1OIszChyU7ta6zrdNGTDVTvNp8hYjPnMJZBUeiiQwhYjwMomo4v4XtIQNxrmYqHw1HzhfeLRBX17qY1T1s8YSDhYZmtKaZh4yjv-Ka-CpEAwKGGaR2QUhX99-Feg-wxA60z5nn320VYV-8-GFzJvDBUIf3OeC-LOl6X03dHt6yJkRaAmWPFCwAwemveS8rTDpkCKCqibjaDfUUqiQTL4-ByoPxhmIIX7xtLIEvsQGb2M0dUKTXiiT5kEu0VDelQm1AI"
region: "München"
country: "Deutschland"
completed: "1026"
missions: "48"
date: "2016"
bg-link: "https://bannergress.com/banner/blauer-reiter-tour-9d18"
onyx: "1"
description: "Wünsche viel Spaß beim Spielen beim 48 Mosaik des Blauen Reiters. \n\nErschaffen hat den Blauen Reiter Franz Marc (1880 – 1916), wo man das Original im Lenbachhaus anschauen kann."
lengthKMeters: "17,08"
title: "Blauer Reiter Tour"
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

