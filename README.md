## eight - ein super einfacher 8Bit computer

**TODO**: ordentliche README schreiben

Dies sind die Datein für einen simulierten 8Bit computer und einem Prototyp des S3BPAL compiliers

### Eigenschaften
---

 - arbeitet mit 8 Bit [signed](https://en.wikipedia.org/wiki/Signed_number_representations) Integers
 - benutzt S3BPAL (gesp. "see-pal") (gekürzt), meine eigene Assembly sprache für super einfache Prozessoren (**Note**: leider benutzt S3BPAL 16Bit Befehle, deher müssen wir an manchen Stellen 16Bit, nicht 8Bit Zahlen speichern)

### Benötigte Programme
---

 - Sebastian Lague's Digital Logic Sim: [itch.io](https://sebastian.itch.io/digital-logic-sim), [github](https://github.com/SebLague/Digital-Logic-Sim)  
-> Kostenlos, einfach zu benutzen, open source; leider nicht völlig bug-free

**Installation**:

Das Simultations Programm installieren, ausführen und Str + Alt + Shift + O DrÜcken.  
Dies sollte einen Ordner öffnen.  
In den Unterordner müsst ihr dieses Repo clonen. So sollte das dann aussehen:

```
Digital-Logic-Sim
├── AppSettings.json
├── Player.log
├── Player-prev.log
├── prefs
└── Projects
    └── eight
        ├── Chips
        ├── compiling
        ├── Deleted Chips
        └── ProjectDescription.json
```

Solltet ihr dieser Erklärung nicht folgen können, mach ein [Issue](https://github.com/IamLegende7/8Bit/issues) auf, fragt mich in der Schule, schreibt mich an, etc

### Schreiben von S3BPAL Programmen für eight
---

**Syntax Highlighting**

>**ACHTUNG!** Ihr solltet *niemals* einfach so eine VSCode Extention installieren! **Sie sind einfach nur Programme, die auf eurem Computer laufen!** (Das gilt übrigens auch für Extentions auf dem VSCode Marketplace).  
>In diesem Fall kennt ihr ja aber den Autor persönlich: Ihr könnt also selbst einschätzen ob Ich euch einen Virus andrehen würde.

Solltet ihr VSCode benutzen, so könnt ihr (in VSCode) auf die datei `compiling/s3bpal-lang-0.0.1.vsix` Rechts-Clicken und auf `Install Extention VSIX` drücken. Dies sollte eine, von Mir selbst erstellte VSCode Extention, installieren.  
Diese sorgt für Syntax Highlighting für S3BPAL (Also dass der Code so schön bunt ist).

Erwartet bloß bitte nicht zu viel; sie wurde in so ca. 1h (und ohne vorheriger Erfahrung) zusammengeworfen.

**Beispiele**

Unter [compiling](https://github.com/IamLegende7/8Bit/tree/main/compiling) solltet ihr einige Assembly Datein (1. S3BPAL assembly nicht richtige Assembly; 2. die Datein, die mit .s3 enden) und ihre compilierten Gegenstücke (die Datein, die mit .pal enden) finden.  
Diese könnt ihr als Beispiele nutzen.

**TODO**: zu ende schreiben!
