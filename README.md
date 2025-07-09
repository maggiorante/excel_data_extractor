# Utilizzo
Verificare l'installazione di Python sul proprio sistema, se non fosse presente installarlo seguendo le istruzioni sul sito apposito.

Aprire un terminale, ad esempio su windows `prompt dei comandi` o `terminale di windows`.
Posizionarsi nella cartella in cui è contenuto questo progetto spostandosi fra le cartelle usando il comando `cd`.
Eseguire il seguente comando:
```
py -m pip install -r requirements.txt
```

Di seguito una breve descrizione di ogni file contenuto nel progetto:
1. `main.py`: script per estrarre i dati da dei file excel;
2. `merge.py`: script per unire diversi file `csv` creando un unico file con tutte le righe dei vari file che si vogliono unire. __Prima di eseguire questo file bisogna uniformare gli header dei file `csv`,
3. `join.py`: script per unire diversi file `csv` in cui sono presenti righe con lo stesso identificativo ma con colonne differenti, per creare un unico file con tutte le colonne per tutti gli ientificativi unite.