# ProjetZKP

Ce projet utilise https://github.com/Zokrates/ZoKrates

L'utilisation des différents outils est inspirée de:

- ZoKrates: https://blog.gnosis.pm/getting-started-with-zksnarks-zokrates-61e4f8e66bcc
- truffle et ganache: https://hackernoon.com/ethereum-development-walkthrough-part-2-truffle-ganache-geth-and-mist-8d6320e12269

A noter que ceci peut aussi se faire sur Windows via PowerShell.
Une documentation à ce sujet est disponible, afin d'avoir du code partagé par un docker sur Windows.

## Dépendances

- Debian 9
- Docker
- npm
  - ganache
  - truffle
- Python

## Installation

Cloner le dépôt de ZoKrates:

```bash
git clone https://github.com/Zokrates/ZoKrates.git
```



Cloner ce dépôt:

```bash
git clone https://github.com/Ashcatran/projetZKP.git
```



Copier les fichiers de `ZoKrates` dans `projetZKP`:

```bash
cp ZoKrates/* projetZKP/ZoKrates
```



Installer le docker requis dans `projetZKP/ZoKrates`:

```bash
cd projetZKP/ZoKrates
docker build -t zokrates_tutorial .
```



### Dépendances

Installer truffle et ganache:

```bash
npm install -g truffle@">=4.0.0 <5.0.0"
npm install -g ganache-cli
```
Afin d'éviter des conflits de version entre Zokrates et Truffle, la version 4.0 a été prise en compte pour Truffle.
La version GUI de Ganache peut être trouvée ici: https://truffleframework.com/ganache

## Utilisation

La boite à outils ZoKrates permet de traduire du code en langage ZoKrates en Solidity, pour une utilisation dans la Blockchain Ethereum.

### Ecriture du Code

Le code à écrire est situé dans `ZoKrates/code` . La documentation associée au langage requis peut être trouvée ici: https://zokrates.github.io/

### Traduction en Solidity et génération de la preuve

Lancer le docker de `ZoKrates`:

```bash
docker run -v $PWD/code:/home/zokrates/ZoKrates/target/debug/code -ti zokrates_tutorial /bin/bash
```

Compiler le code (ici `prime.code`) en Solidity:

```bash
./zokrates compile -i code/prime.code
```

Générer le témoin:

```bash
./zokrates compute-witness -a [Paramètres]
```

Générer le vérifieur:

```bash
./zokrates setup && ./zokrates export-verifier && cat verifier.sol
```

Générer le témoin:

```bash
./zokrates generate-proof
```

Copier les paramètres de la preuve (de A à K inclus) dans `output.txt` puis sortir du conteneur.  

Les paramètres a fournir au vérifieur peuvent être générés grâce à `parseOutput.py`. Ce script lit le contenu de `output.txt`.

```bash
python parseOutput.py [Paramètres]
```

### Déploiement sur une blockchain privée

Copier `verifier.sol` dans `contracts` :

```bash
cp ZoKrates/code/verifier.sol contracts/verifier.sol
```

Compiler :

```bash
truffle compile
```

Lancer Ganache, en interface graphique ou en console :

```bash
ganache-cli -p 7545
```

Migrer le contrat dans la blockchain:

```bash
truffle migrate
```

Lancer la console de truffle pour interagir avec le contrat:

```bash
truffle console
truffle(development)> Verifier.deployed().then(function(instance) { return instance.verifyTx([Paramètres]);})
```

> **Note:** Les paramètres sont ceux fournis par `parseOutput.py`

Le retour de cette exécution doit contenir:

```javascript
event: 'Verified'
```

