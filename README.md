# script-shodan
<h4>Installare lo script e le sue dipendenze</h4>

Crea il virtual environment
>python3 -m venv venv

Installa shodan
>venv/bin/pip install shodan

<h4>Usare lo script</h4>

Modificare il file config.ini, inserendo l'api key di shodan
>[shodan]
>
>apikey = *metti qui la tua api key*

Aggiungere la lista di ip 
> [ip]
>
> tagert1 = 8.8.8.8
> 
> target2 = 8.8.8.4

Oppure aggiungere l'intera rete
>[network]
>
> tagert1 = 8.8.8.0/24

I nomi degli IP o delle reti da scansionare **non** sono rilevanti, in questo esempio vengono chiamati target ma posso essere chiati anche pippo e ciccio.

<h4> Run </h4>

Avviare script
>venv/bin/python main.py

<h4>Log</h4>

Ogni errore genato dallo script viene salvato nel file **error.log**
