# EKG und Power Analyse
von Till und Finn

Dies ist eine Streamlit-Anwendung zur Analyse von EKG- und Leistungsdaten. Die Anwendung lädt Aktivitätsdaten aus einer CSV-Datei, berechnet Herzfrequenzzonen und zeigt ein Diagramm sowie eine Tabelle mit der verbrachten Zeit und der durchschnittlichen Leistung in den verschiedenen Zonen an.


## Anfoderungen:

Stellen Sie sicher, dass Sie alle im requirements.txt erwähnten Bibliotheken installiert haben.

Um eine Bibliotheken zu Installieren verwenden Sie folgenden Befehl:

pip install "Name der Bibliothek"

## Webseite öffnen:

Um die Webseite zu öffnen führen Sie read_pandas.py und main.py aus um zu überprüfen, dass das Installieren der Bibliotheken geklappt hat.

Geben Sie danach folgenden Befehl in Ihr Terminal ein um die Webseite in ihrem Browser zu offnen:

python -m streamlit run app_website.py 


## Funktionen:

Nun können Sie im Menu den Punkt Personen, EKG oder Power Curve wählen

### Personen:
Hier können Sie zwischen drei Personen wählen und deren Namen und Geburtsjahr einsehen

### EKG:
Hier sehen Sie das EKG- und Leistungsdiagramm mit den entsprechenden Zonen. Über dem Diagramm können Sie die maximale Herzfrequenz einstellen, woraufhin sich die Zonen automatisch anpassen. Unter dem Diagramm können Sie die Eigenschaften der Leistung sowie der Zonen ablesen.

### Power Curve:
Hier wird die Power in einem Power-Zeit-Diagramm dargestellt. 

