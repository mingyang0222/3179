{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "width": 900,
  "height": 500,
  "projection": {"type": "equalEarth"},
  "data": {
    "url": "ne_110m_admin_0_countries.topojson",
    "format": {"type": "topojson", "feature": "ne_110m_admin_0_countries"}
  },
  "mark": {"type": "geoshape", "fill": "lightgray", "stroke": "white"}
}
