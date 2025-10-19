---
nummer: "200"
startLatitude: "55.604689"
startLongitude: "12.987334"
titel: "Slaget om Malmö"
picture: "https://lh3.googleusercontent.com/lr/AFBm1_YE7IzoblvCYSmlJTN4VXMwpKNH6NsMwl3s4mZ1Q6V8MV3uxkHven6Wqg9uteKyeNWOIjUyIRFbkD-SEl05-XGIx6E1MFEHMoUA2AGF8xx-uDiNzUeaWR1fI6XP9tOlGWOOsq1w_XrKrq4aojE-f62NAgngdbcOMg834Ly7bD4gguFK9RGYiIU3LZZw8HCRidoz4ogZGbFVCz4hg5daehIb2C68akmDMk-4yggX6rG7qhAG6gteezbSVKqf9j2mIrwki9WAEcAVx2rRat_JjWcHKTCC2YoJ-D2Q_AD9pOudbKZlSOWJhYcxkSh5k6VOm5uKmTKjHOEkApzPxbmI5CVaYsN9D5OskkQZQATQPwwqd6-uCiyRvI8rdLvjeYXSe0j_97F3V4zXxlv8ZpTgzEZXjSW5VlXNXsPC21ZTR4Pvxm3cRgo2ArZoEma9Z415dKExqjRZHN-uuuZEIbIqiZh2ry0KPgbDvGs6ZvKVJ-d0BFXIRw2QZAizwNLqlu5y3Pv2eVzsDVjZVj54Av96Ipw2PsC8nBpfNKUUbSknFGB9FlzbmwQPaI1BOth_5Om45YqRE1kT18VWgRYjI32Z4JA2Rm-JkMWbgsjPYnjAxBKsej9p_mu_LrsJ6ygUmH0kbTg6NR1PlNbmo18NVC_7xLEEgCcjlRIi8pJufBHJIqjk09gsRnxkbqNJgSWws9icHLQChPqdJ-zrxucbtmU8fmF6LtHcoUAuy-g0eMb1I6OwZU3B7N-g7D5xTa2U7crJVvs8LusCmxxNvdWPKtUsFzg_eVynj-go5HYZ3zQrzGi7cwCT3MeknscBnTWpeKvhZ0U3aksBA2ZTEkLaocxbU8eQgQCJSf0"
region: "Malmö"
country: "Sverige"
completed: "4674"
missions: "6"
date: "2018"
bg-link: "https://bannergress.com/banner/slaget-om-malm%C3%B6-8c4a"
onyx: "0"
description: "Sista kriget mellan Sverige och Danmark var i slutet av 1600-talet. Då hade det krigats  till och från i ett par hundra år om Skåne.  Bild av 1658 när Karl X Gustav besöker nya staden. Not 24/7!"
lengthKMeters: "2,56"
title: "Slaget om Malmö"
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

