Der folgende Beitrag entstand im Zuge des Seminars ["Mobile Roboter"](https://tams.informatik.uni-hamburg.de/lectures/2021ws/praktikum/mobileRob/) an der Uni Hamburg. 

## Zielverfolgung des Turtlebot
Die Zugrundeliegende Problemstellung ist folgende: Der Turtlebot muss den Apriltag eines anderen Roboters möglichst mittig und nah Fotografieren. Dafür haben wir den "Target Mode" entwickelt. Mit der Nachricht auf dem tag detections Topic, also unmittelbar nachdem der Roboter ein Apriltag erkannt hat, wechselt der Roboter in den Target-Mode. Im Target-Mode arbeitet der Roboter ohne die Costmap, navigiert wird anhand des Apriltags im Kamerabild und die Kollisionsvermeidung  findet über den Xbox-Kinect Tiefensensor statt.

### Grundlagen des Konzepts
Die Punktzahl aus den Faktoren Ent-
fernung, Position im Bild und Ausrichtung des Tags. Das Tag wird vorerst als stationär betrachtet. Die Ausrichtung im Bild ist direkt von der Rotation des Roboters abhängig. Ist das Tag mittig im Bild, ist die Entfernung direkt von der Bewegung nach vorne und hinten abhängig. Es bleibt die Ausrichtung desTags zum Roboter, um diese kontrolliert zu beeinflussen, bedarf es der zweidimensionalen Bewegung im Raum.

#### Approach Tag
Hat der Roboter ein bestimmtes Tag anvisiert, soll er zunächst auf die Achse dieses Tags gelangen. Der schnellste Weg wäre die direkte Verbindung. Allerdings
wird der Roboter so das Apriltag in der Kamera temporär verlieren. Bewegt sich
das Tag in dieser Zeit, müsste unter Umständen der Target-Mode erfolglos abgebrochen werden. Um dies zu verhindern, soll der Roboter immer Sichtkontakt
zum Tag haben.
Der gewünschte Weg ist für uns also der kürzeste, bei dem das Tag nicht
verloren geht. Das erreichen wir, indem das Tag immer an einem Idealwert
gehalten wird. Konkret bedeutet das bei einem FOV von etwa 60°, das Tag bei
ungefähr ± 28° zu halten. Der in Abbildung 2b gezeigte Weg ist der kürzeste mit stetigem Sichtkontakt
zum Tag, bringt aber noch weitere Vorteile mit sich. So ist eine Kurvenfahrt
für den Roboter gegenüber einer ’eckigen’ zu bevorzugen. Der Roboter muss
nicht abrupt abbremsen, drehen und beschleunigen, sondern kann stabil und
relativ kontinuierlich fahren. Davon versprechen wir uns eine schnellere Anfahrt,
weniger Akkuverbrauch und ein stabileres Kamerabild.

#### Closing In

Ist der Roboter auf der Achse des Tags, so muss er sich nur zentrieren und anschließend die Distanz verkürzen.

#### Close Up
Im Close-Up Mouds dreht sich der Roboter nur noch um die eigene Achse, um
das Tag im Kamerabild zu zentrieren. Ursprünglich sollte auch spätestens hier
das Foto aufgenommen werden. Jedoch haben wir das Fotografieren letztendlich
komplett ausgelagert.

#### Bewegtes Tag und Wechsel der Modi

Auch wenn hier zur Abstraktion das Tag als stationär betrachtet wurde, funktio-
nieren die Prinzipien auch beim bewegten Tag. Das liegt an der durchgehenden
Verfolgung per Kamera. So passen sich die Modi bei jedem Frame neu an die
Gegebenheiten an. Ob sich das Tag oder der Roboter bewegen ist für die Ana-
lyse (die zu einem einzelnen Zeitpunkt berechnet wird) unerheblich. In diesem
Sinne kann der Roboter als ’zustandslos’ betrachtet werden.
Der Wechsel zwischen den Modulen funktioniert uneingeschränkt, aus jedem
Modus soll bei Bedarf gewechselt werden können. Dreht sich beispielsweise der
gegnerische Roboter während des Closing-In, befindet sich unser Roboter nicht
mehr auf der Achse und wechselt in den Approach-Tag Modus. Entfernt sich
der Roboter im Close-Up Modus, wechselt der Roboter je nach Ausrichtung
des Tags in den Closing-In oder Approach-Tag Modus. Der uneingeschränkte
Wechsel gilt nur im Kontext der einfachen Verfolgung von Tags. Im Wettkampf
ist dieser Wechsel aus taktischen Gründen nicht uneingeschränkt gewollt.
In der Praxis ist dafür wichtig, dass der Wechsel flüssig erfolgt. Im Folgenden
Abschnitt der Implementierung wird dies von großer Bedeutung sein.

### Implementierung
In diesem Kapitel wird die Implementierung vorgestellt. Die Ausschnitte des
Codes sind aus Gründen der Lesbarkeit in Pseudocode formuliert. Die Einheiten
entsprechen dem SI-System.

tagDistance Entfernung des Apriltags zum Roboter.
lostManeuver() initiiert eine Abfolge von Aktionen die ausgeführt werden
wenn das Tag verloren wurde.
takePicture() schickt das aktuell beste Foto an den Gameserver und führt
anschließend eine Routine für die folgenden zehn Sekunden der Inaktivität
aus.
move(a,b) sendet (published) eine Bewegung an den Roboter. ’a’ ist die Ge-
schwindigkeit nach vorne, ’b’ die Drehgeschwindigkeit.
timeSinceImprovement Die Zeitspanne seitdem das letzte, beste Bild aufge-
nommen wurde.
winkelR Der Winkel, in welchem das Apriltag horizontal im eigenen Kamera-
bild steht. Mittig sind 0°.
winkelD Der Winkel, in welchem der Roboter aus Sicht des Apriltags steht.
Perfekt auf der Achse sind 0°.

#### Close Up
Im Close-Up Modus werden zuerst Bedingungen untersucht, unter denen dieser
abgebrochen wird. Die Drehgeschwindigkeit wird mit −(winkelR/14) berech-
net und steigt linear1 an oder ab. Ist der gegnerische Roboter mittig im Bild,
geht winkelR also gegen 0, so reduziert sich auch die Drehgeschwindigkeit gegen
0. Ist das gegnerische Tag 14° von der Mitte entfernt, so beträgt die Drehge-
schwindigkeit 1 und steigt mit Zunahme des Winkels. Das negative Vorzeichen
sorgt für die Drehung in die richtige Richtung. Die 14 wurde beim Testen als
Minimum ermittelt, bei dem der Roboter trotz seiner Geschwindigkeit das Tag
noch verfolgen kann.

#### Closing In
Die Drehgeschwindigkeit ist im Closing-In Modus wie im Close-Up Modus ge-
staltet, nur ist sie etwas langsamer. Hinzu kommt die Geschwindigkeit nach
vorne. Hier gibt es mehrere Faktoren, die eine Rolle spielen. Zum einen ist das
der Winkel des Tags im Kamerabild. Ist dieser maximal, also 30, soll sich der
Roboter nicht nach vorne bewegen. Der Faktor ist in diesem Fall 0. Wenn das
Tag zentriert ist, beträgt der Faktor 1 und hat keine Auswirkungen auf die
Geschwindigkeit. Ähnlich verhält es sich mit der Entfernung. Bei 0.9m, ist der
Faktor Entfernung 0, um den Übergang in den Close-Up Modus zu vollziehen.
Bis 1.1m steigt der Faktor auf sein Maximum 1 an.2

#### Approach Tag

Erwähnenswert ist hier Zeile zwei, in welcher geprüft wird, ob der Roboter sich
auf der Achse des Apriltags befindet. Da der Approach Modus leider nur selten
verwendet wird, haben wir keine Zeit in die Entwicklung von dynamischen Ge-
schwindigkeiten investiert. Das Fenster für den Winkel des Tags im Bild, haben
wir hier auf ± 23° bis ± 26° gesetzt. Wird dieses Fenster eingehalten, bewegt sich
der Roboter mit einer festen Geschwindigkeit vorwärts. Weicht der tatsächliche
Winkel davon ab, verlangsamen wir die Vorwärtsbewegung und drehen den Ro-
boter in die entsprechende Richtung. Somit gibt es zwei Geschwindigkeitsstufen,
deren Wechsel abrupt erfolgt. Die konkreten Werte haben sich beim Testen eta-
bliert.

### Evaluation
Während der Approach-Tag Modus den Kern unserer theoretischen Konzeption 
bildet, befand sich der Roboter nur äußerst selten und kurz in diesem Modus.
Grund dafür ist die sehr unzuverlässige Berechnung des Winkels, in welchem
das gegnerische Apriltag steht. Gründe hierfür sind die technischen Limitierun-
gen der Kamera und der Umstand, dass kleinste Veränderungen auf der Basis
weniger Pixel in großen Änderungen beim berrechneten Winkel resultieren. Die
Schwankungen des Winkels von zum Teil über ± 10° versuchen wir über einen
gleitenden Median zu mindern. Trotzdem mussten wir große Toleranzen nutzen
(± 8°). Auch werden Winkel über ca. 30° nur sehr unzuverlässig erkannt.
Die Auswirkungen der dynamischen Geschwindigkeitsanpassung haben unse-
re Erwartungen übertroffen. Die dynamische Geschwindigkeit brachte merklich
Stabilität in den Roboter und verhinderte ein Zittern zwischen verschiedenen
Stufen/Modi. Auch außerhalb unseres Teams schienen diese Fahreigenschaften
einen Eindruck hinterlassen zu haben. Generell konnten wir im Vergleich fest-
stellen, dass die Verfolgung von Tags mit unserem Ansatz den auf moveGoal
basierenden Ansätzen überlegen war. Das grundlegende Konzept sowie Teile
der Implementierung haben sich trotz der Schwierigkeiten mit den vorhandenen
Sensoren bewährt. Eine höher auflösende Kamera und Entfernungssensoren im
Nahbereich könnten das Potenzial zukünftig noch weiter ausreizen.
