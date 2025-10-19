---
nummer: "314"
startLatitude: "53.146971"
startLongitude: "8.213374"
titel: "Serenity"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_YqbI0LHlj3WfFca-Bt_70k1Rkld4DOw7i33RxmYd3h04_gaWP8SMmFirhcqqdOKd26s4N2QzlHA4i1ci6Omln5XJfwg7lK-X93RobXOnneGv_Gxvl20qzgoQnhSyQ9VyCnCSdZAkW4inB_I5c2bbIIQBu-kJL2N6gnzTu9V8yNfMBvVlkcoBK5xnjZJR7hHGRdvRUjP7wcOTY1iz5B9MBHS_eyjUeHgngm1nVqyUQzSAszpwh-IDGE2-LUQ_sINbe4uPqt5MxhSuNp10D0IfrdqZs_XzfgTJK4PcAZR4q7hChbVZINrRyXmQ57b7K5fYy_UZ-IKlkQ-1ssy3zM6s7i8x5Q99QWrnjmAzC5xZVxs6CUcAYEbLdc3gGgvBsw8IuINxf6rOZ73ozGkJvD5Cl72NHLtAkIltZPYwSwGHYNSbllkNeH-xehmazuI6IAxzOOczxvdkktn0aHd9_7xs5DsM-wuUVPlHYChBIPrKB31Aclbw_QrllvkJF7HA1OI7VrihhfgNvC5HcUDhA9-ryn3tNBRjoZ-L6MQ9wNH-eC3JCU3jc6M2Mo-5Io6WqjlCUJr-5kEMnDYBMYa8zpK25tljQiy2C_drM1BG2p7BwUYQFDm--HVOtljv2WBsWRHCPs-ibIiudoGczbuZOsFrmH9oGdYjBc_ApH6snAfjnlH0K3ZdIPYd974qKMOuFKVMefVHJz9Jk4dZ12thphnTZEJU0zRHK792Tn1NMe7ielNG4bet_zCv9dRFIoXJgGK2xWCE0zjBujPEOTa8Tp-TKlvdTWtq--63X4GaEy-kzMIlDKd2HVCoLEApMGciCElm9rteKhbTbIZjzzkYvCHjqbJjQWNjE"
region: "Oldenburg"
country: "Deutschland"
completed: "7332"
missions: "24"
date: "2021"
bg-link: "https://bannergress.com/banner/serenity-b1ef"
onyx: "0"
description: "Begleite die Crew der Serenity auf ihrer Reise durch Oldenburg. Es sollte einige uniques geben."
lengthKMeters: "7,77"
title: "Serenity"
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

