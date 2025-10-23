# {{__TITLE__}}

*{{__DATE_DE__}}*{{__IF:city__}} • {{__VAL:city__}}{{__/IF__}}{{__IF:country__}} • {{__VAL:country__}}{{__/IF__}}

{{__IMG:picture__}}

## Details
{{__IF:lengthKMeters__}}- **Distanz (km):** {{__VAL:lengthKMeters__}}{{__/IF__}}
{{__IF:missionsCount__}}- **Missionen im Banner:** {{__VAL:missionsCount__}}{{__/IF__}}
{{__IF:totalCompleted__}}- **Insgesamt abgeschlossene Missionen:** {{__VAL:totalCompleted__}}{{__/IF__}}
{{__IF:bannerIndex__}}- **Das ist mein Banner Nr.:** {{__VAL:bannerIndex__}}{{__/IF__}}

{{__IF:description__}}
## Beschreibung
{{__VALBR:description__}}
{{__/IF__}}

{{__IFANY:bg-link,umap__}}
## Links
{{__IF:bg-link__}}<a href="{{__VAL:bg-link__}}" target="_blank" style="display:inline-block;margin-right:8px;padding:6px 12px;background:#3c8b3c;color:#fff;text-decoration:none;border-radius:6px;">🔗 Bannergress</a>{{__/IF__}}
{{__IF:umap__}}<a href="{{__VAL:umap__}}" target="_blank" style="display:inline-block;padding:6px 12px;background:#0066cc;color:#fff;text-decoration:none;border-radius:6px;">🗺️ uMap</a>{{__/IF__}}
{{__/IFANY__}}

> Datei: `{{__FILENAME__}}` • #{{__NUMBER__}} • Slug: `{{__SLUG__}}`
