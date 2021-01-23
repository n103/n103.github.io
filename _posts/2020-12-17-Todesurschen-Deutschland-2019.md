---
layout: post
---
Todezahlen in Deutschland aus 2019. Nach Ursache, Alter und Geschlecht.
Die GRafik ist für Computer optimiert. Auf kleinen Bildschirmen (z.B. Smartphones) ist das Querformat zu bevorzugen.
<div id='myDiv'>
<!-- Plotly chart will be drawn inside this DIV -->
</div>
<script src="{{base}}/assets/tod.js" > </script>
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

        var config = [log];

        var layout = { 
            title: 'Todeszahlen Deutschland 2019',
            showlegend: false,
            height: 1800,
            //width: 1400,
            autosize: true,
            margin: {
                l: 310
            }

        };

        Plotly.newPlot('myDiv', config, layout);

</script>

Quelle: [Statistisches Bundesamt (Destatis)](https://www-genesis.destatis.de/genesis/online?sequenz=tabelleErgebnis&selectionname=23211-0004#abreadcrumb) (Code: 23211-0004)

Die Daten wurden als [Flat-CSV](https://raw.githubusercontent.com/n103/n103.github.io/master/resources/todeszahlen/23211-0004_flat.csv) heruntergeladen und nicht benötigte Spalten entfernt. Daraus wurde anschliessend mit einem [Python-Script](hhttps://raw.githubusercontent.com/n103/n103.github.io/master/resources/todeszahlen/tod_script.py) eine [Java-Script Datei](https://raw.githubusercontent.com/n103/n103.github.io/master/assets/tod.js) generiert. Diese wird mirhilfe von [Plotly](https://plotly.com/javascript/bubble-charts/) graphisch aufbereited.
{% comment %}
Might you have an include in your theme? Why not try it here!
{% include my-themes-great-include.html %}
{% endcomment %}

