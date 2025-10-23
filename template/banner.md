# {{__TITLE__}}

*{{__DATE_DE__}}*{{__IF:region__}} • {{__VAL:region__}}{{__/IF__}}{{__IF:country__}} • {{__VAL:country__}}{{__/IF__}}

{{__IMG:picture__}}

{{__IF:notice__}}
<div style="margin: 10px 0 18px; padding: 10px 12px; border-left: 6px solid #f0ad4e; background: #fff8e6; border-radius: 6px;">
  <strong>Notice:</strong><br>
  {{__VALBR:notice__}}
</div>
{{__/IF__}}

## Details
{{__IF:lengthKMeters__}}- **Distance (km):** {{__VAL2DP:lengthKMeters__}}{{__/IF__}}
{{__IF:missions__}}- **Missions in banner:** {{__VAL:missions__}}{{__/IF__}}
{{__IF:completed__}}- **Total missions completed:** {{__VAL:completed__}}{{__/IF__}}
{{__IF:nummer__}}- **This is my banner no.:** {{__VAL:nummer__}}{{__/IF__}}
{{__IF:missionDay__}}- **Mission Day:** {{__VALYESNO:missionDay__}}{{__/IF__}}

{{__IF:description__}}
## Description
{{__VALBR:description__}}
{{__/IF__}}

{{__IFANY:bg-link,umap__}}
## Links
{{__IF:bg-link__}}<a href="{{__VAL:bg-link__}}" target="_blank" style="display:inline-block;margin-right:8px;padding:6px 12px;background:#3c8b3c;color:#fff;text-decoration:none;border-radius:6px;">🔗 Bannergress</a>{{__/IF__}}
{{__IF:umap__}}<a href="{{__VAL:umap__}}" target="_blank" style="display:inline-block;padding:6px 12px;background:#0066cc;color:#fff;text-decoration:none;border-radius:6px;">🗺️ uMap</a>{{__/IF__}}
{{__/IFANY__}}

> File: `{{__FILENAME__}}` • #{{__NUMBER__}} • Slug: `{{__SLUG__}}`
