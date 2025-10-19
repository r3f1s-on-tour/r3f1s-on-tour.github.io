---
nummer: "243"
startLatitude: "52.512885"
startLongitude: "13.451796"
titel: Frankfurter Tor
picture: https://lh3.googleusercontent.com/lr/AFBm1_YmBFkcHtsM0y7jbgIVAEK_uOC232HBlTnbP6EciuXhiEzG5spkMm1NbLx1mRW0I5V6i-YeejcpL86wqTl7vrYESjmNmPMoc0Uv1cIIjgbUNKfQ5h1Be9FNoLUn0BFH2PaHA9TzSdscO9lZvpgog5WN6r8W6g5kwC71wiBZFEExmn4GKfZRA4WtbswrLPfrGEkd6rPZx2_kAuZTDb7of-zBWcCTlD7CO-4MMB8T80vZNWCJzE_xT9ase6rqHmm5cW8nZowhd-mFe3jEmvciO51Da8Bb5tmpEAQY8eYK0cYwBsEA_x1RiC13538QvVZIChjtz1U24tRZIsOvkaSETuMm9CN-li4An6_rXrLZQFbWt_5F2ibQ_ZSB08LkGvSdQIsOt44ojEbxjvcxWJVzwq6ZCKxXIGcuASVn6MZ1-yiIDf7Be4IqoNoRAyODl0mcN3sq9fca1uuADa-6Qwd_ytu9PF01OvVplSkuXvgrdNhuhnh-_Elet82CaFUYWX2nnRZgy2LyHKoIZELdOpObXnmXi8noJPSC55BDjACV6Qguz9OEJsv50u6P740G8xglZrJg4ORKo6Zvr_J9JzhzZglnHWsLT-tnuF6Ni-vVHtH4axHlhdD1ZWB2EnMjzav5ZQlyXVb3mz13f9cctFtOKFp-paQd6OnrQV9HdNS7QOBZCywZwPwTKr5NXZvWAwf4Tl_XLawPEsBsZyq3ItxVWZ70djfUDfoLwbO5Ln6zvPCr61I0BCK0Qjj3gcjUI_dPL3j4JJPj21TxamgT9YVdThs0PnyWmNztxKIHawjdQiXX4s7OEeuHGYWFAkixV4-1PY6WzK9Jge2a2fi89N9NeMKFJhAwSBk
region: Berlin
country: Deutschland
completed: "5814"
missions: "12"
date: "2019"
bg-link: https://bannergress.com/banner/frankfurter-tor-940b
onyx: "0"
description: Das Frankfurter Tor ist heute ein Platz im Berliner Ortsteil Friedrichshain am östlichen Ende der Karl-Marx-Allee. Obwohl der Name es vermuten lässt.
lengthKMeters: 4,15
title: Frankfurter Tor
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

