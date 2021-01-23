---
layout: post
---
Todezahlen in Deutschland aus 2019. Nach Ursache, Alter und Geschlecht
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

Die Daten wurden als [Flat-CSV mit einem]() heruntergeladen. Daraus wurde anschliessend mit einem [Python-Script]() eine Java-Script Datei generiert. Diese wird mirhilfe von Plotly graphisch aufbereited.
{% comment %}
Might you have an include in your theme? Why not try it here!
{% include my-themes-great-include.html %}
{% endcomment %}

