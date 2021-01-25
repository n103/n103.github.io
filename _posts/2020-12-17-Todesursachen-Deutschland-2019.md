---
layout: post
---
Die Grafik ist für Computer optimiert. Auf kleinen Bildschirmen (z.B. Smartphones) ist das Querformat zu bevorzugen.
<div id='myDiv'>
<!-- Plotly chart will be drawn inside this DIV -->
</div>
<script src="{{base}}/assets/tod.js" > </script>
<script src="{{base}}/assets/plotly.js" > </script>
<script>
        var log = {
            x: data['source'],
            y: data['target'],
            text: data['text'],

            mode: 'markers',
            marker: {
                size: data['valueLog'],
                color: data['color']
            }
        };

        var dataPlotly = [log];

        var layout = {
            title: 'Todezahlen in Deutschland aus 2019. Nach Ursache, Alter und Geschlecht.',
            hovermode: "closest",
            showlegend: false,
            height: 1800,
            //width: 1400,
            autosize: true,
            margin: {
                l: 310
            }

        };

        var config = {
            modeBarButtonsToRemove: ['zoom2d', 'pan2d', 'select2d', 'lasso2d', 'zoomIn2d', 'zoomOut2d', 'autoScale2d', 'resetScale2d', 'toggleSpikelines', 'hoverCompareCartesian', 'hoverClosestCartesian'],
            displaylogo: false
        }

        Plotly.newPlot('myDiv', dataPlotly, layout, config );

</script>

Quelle: [Statistisches Bundesamt (Destatis)](https://www-genesis.destatis.de/genesis/online?sequenz=tabelleErgebnis&selectionname=23211-0004#abreadcrumb) (Code: 23211-0004)

Die Daten wurden als [Flat-CSV](https://raw.githubusercontent.com/n103/n103.github.io/master/resources/todeszahlen/23211-0004_flat.csv) heruntergeladen und nicht benötigte Spalten entfernt. Daraus wurde anschliessend mit einem [Python-Script](https://raw.githubusercontent.com/n103/n103.github.io/master/resources/todeszahlen/tod_script.py) eine [Java-Script Datei](https://raw.githubusercontent.com/n103/n103.github.io/master/assets/tod.js) generiert. Diese wird mirhilfe von [Plotly](https://plotly.com/javascript/bubble-charts/) graphisch aufbereited.
{% comment %}
Might you have an include in your theme? Why not try it here!
{% include my-themes-great-include.html %}
{% endcomment %}

