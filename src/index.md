# MAP2LE

```js
// const metadata = FileAttachment("metadata.parquet").parquet();
const vt_topo = FileAttachment("vt_topo.json").json();
const vt_trails = FileAttachment("FS_VCGI_OPENDATA_Emergency_TRAILS_line_SP_v1_-1226006560882090274.geojson").json();
const lake_topo = FileAttachment("lake_champlain.json").json();
```

```js
const districts_mesh = topojson.mesh(vt_topo, vt_topo.objects.state)
const districts = topojson.feature(vt_topo, vt_topo.objects.state).features
const lake_champlain = topojson.feature(lake_topo, lake_topo.objects.lake).features
```

```js
const activityInput = Inputs.select(['hiking'], {label: "activity:"})
const activity = Generators.input(activityInput);

const modelInput = Inputs.select(['autoregressive'], {label: "models:"})
const industry = Generators.input(modelInput);

const vectorlInput = Inputs.select(['ticks', 'mosquitoes', "Blacklegged ticks"], {label: "vector:", multiple: 3})
const vector = Generators.input(modelInput);

const pathogenInput = Inputs.select(['B burgdorferi (Lyme)'], {label: "pathogen:"})
const pathogen = Generators.input(pathogenInput);
```

```js
const chosen_counties = ['BURLINGTON', 'ALBANY', 'MONTPELIER', 'SWANTON', 'RUTLAND', 'BARRE', 'NEWPORT', 'VERGENNES']
```

<div class="grid grid-cols-3">
    <div class="card grid-colspan-1">
    <h1>MAP2LE</h1>
    <em>Toggle different layers of activities and wildlife vectors of interest to visualize pathogen risk.</em><br><br>
    ${activityInput}<br>
    ${vectorlInput}<br>
    ${pathogenInput}<br><br>
    You can also choose different models to forecast the risk, based on various indices.<br><br>
    ${modelInput}
    </div>
    <div class="grid-colspan-2">
    ${resize((width) => Plot.plot({
        width,
        height: 800,
        projection: {
            domain: d3.geoCircle().center([-73, 43.90]).radius(1.2)(),
            type: "mercator",
        },
        marks: [
            Plot.geo(vt_trails, {stroke: "brown", strokeOpacity: 0.2, tip:true}),
            Plot.geo(districts_mesh, {strokeOpacity: 0.2}),
            Plot.geo(lake_champlain, { fill: "lightblue"}),
            Plot.text(districts, Plot.centroid({
                text: (d) => chosen_counties.includes(d.properties.town) ? d.properties.town : null, 
                fill: "currentColor", stroke: "white"
            }))
        ]
    }))}
    </div>
</div>


