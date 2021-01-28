---
layout: post
---
Die Grafik ist für Computer optimiert. Auf kleinen Bildschirmen (z.B. Smartphones) ist das Querformat zu bevorzugen.

In dieser Grafik sind aus Gründen der Üersichtlichkeit nur Todesursachen mit einem Datenpunkt größer als 8000 aufgeführt. Ein Datenpunkt besteht aus jeweils einer Altersgruppe und einer Todesursache. Die Farbverlauf entspricht entspricht der Geschlechterverteilung, wobei Männer blau und Frauen grün repräsentiert werden.

<div id='B'></div>

Auffällig ist, dass alle Datenpunkte von Altersgruppen unter 50 Jahren so klein sind, dass sie nicht mehr erkennbar sind. In der folgenden Grafik sind deshalb die ALtersgruppen unter 50 Jahren, mit Todesursachen mit einem Datenpunkt größer als 200, dargestelt.

<div id='C'></div>

Im folgenden nochmal alle Todesursachen aller Altersgruppen. Die größe der Datenpunkte verhält sich logarithmisch zu einander (zur Basis 1,4).

<div id='A'></div>
    
<script src="{{base}}/assets/tod.js" > </script>
<script src="{{base}}/assets/plotly.js" > </script>
 <script>
        var A = {
            x: data['sourceA'],
            y: data['targetA'],
            text: data['textA'],

            mode: 'markers',
            marker: {
                size: data['sizeA'],
                color: data['colorA']
            }
        };

        var B = {
            x: data['sourceB'],
            y: data['targetB'],
            text: data['textB'],

            mode: 'markers',
            marker: {
                size: data['sizeB'],
                color: data['colorB']
            }
        };

        var C = {
            x: data['sourceC'],
            y: data['targetC'],
            text: data['textC'],

            mode: 'markers',
            marker: {
                size: data['sizeC'],
                color: data['colorC']
            }
        };


        //var dataPlotly = [A];

        var layoutA = {
            title: 'Alle Ursachen und Altersgruppen. Darstellung logarithmisch',
            hovermode: "closest",
            showlegend: false,
            height: 1600,
            //width: 1400,
            autosize: true,
            margin: {
                l: 310
            }

        };

        var layoutB = {
            title:'Ursachen mit mindestens 8000 Fällen einer Altersgruppe',
            hovermode: "closest",
            showlegend: false,
            height: 600,
            //width: 1400,
            autosize: true,
            margin: {
                l: 310
            }

        };

        var layoutC = {
            title: 'Alter unter 50. Ursachen mit mindestens 200 Fällen einer Altersgruppe.',
            hovermode: "closest",
            showlegend: false,
            height: 900,
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


        Plotly.newPlot('A', [A], layoutA, config);
        Plotly.newPlot('B', [B], layoutB, config);
        Plotly.newPlot('C', [C], layoutC, config);

    </script>

Quelle: [Statistisches Bundesamt (Destatis)](https://www-genesis.destatis.de/genesis/online?sequenz=tabelleErgebnis&selectionname=23211-0004#abreadcrumb) (Code: 23211-0004)

Die Daten wurden als [Flat-CSV](https://raw.githubusercontent.com/n103/n103.github.io/master/resources/todeszahlen/23211-0004_flat.csv) heruntergeladen und nicht benötigte Spalten entfernt. Daraus wurde anschliessend mit einem [Python-Script](https://raw.githubusercontent.com/n103/n103.github.io/master/resources/todeszahlen/tod_script.py) eine [Java-Script Datei](https://raw.githubusercontent.com/n103/n103.github.io/master/assets/tod.js) generiert. Diese wird mirhilfe von [Plotly](https://plotly.com/javascript/bubble-charts/) graphisch aufbereited.
{% comment %}
Might you have an include in your theme? Why not try it here!
{% include my-themes-great-include.html %}
{% endcomment %}

