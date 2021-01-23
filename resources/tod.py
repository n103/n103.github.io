import pandas as pd
import json 
import math

df = pd.read_csv('23211-0004_flat.csv', sep=';')

source = list()
target = list()
value  = list()
valueLog = list()
percentageF  = list()  
color = list()
text = list()

for f in range(len(sourceF)):
    for m in range(len(sourceM)):
        if sourceF[f]==sourceM[m]:
            if targetF[f]==targetM[m]:
                totalValue = (valueF[f] + valueM[m])
                if totalValue  == 0:
                    continue
                source.append(sourceF[f])
                target.append(targetF[f])
                value.append(totalValue)
                percentageF.append(valueF[f]/totalValue)
                

for i in range(len(source)):
    v = value[i]
    p = percentageF[i]
    
    valueLog.append(math.log(v,1.4))
    color.append('rgb(0,' + str((p*255))+','+str((1-p)*255)+')')
    hover = 'Gesamt: '+str(int(v))+'<br>'
    hover = hover + ('Frauenanteil: '+str(100*round(p,2))+'%')
    
    text.append(hover)
    
 d = {
    'source': source,
    'target': target,
    'value' : value,
    'color' : color,
    'valueLog':valueLog,
    'text':text
    
}

my_json = json.dumps(d)
with open("tod.js", "w") as outfile:
    outfile.write("var data = "+ str(d) )
