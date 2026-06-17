# Analyse de Sentiments Twitter 🐦

![Logo du projet](logo.png)

## 📝 Description

Ce projet implémente une analyse de sentiments sur des tweets en utilisant Python. Il permet d'évaluer si un tweet exprime un sentiment positif ou négatif en se basant sur des listes de mots prédéfinies.

## 👥 Auteurs

- Mohamed Islem Ben Farhat
- Oussama Benali

## 🛠️ Technologies Utilisées

- Python
- Pandas (manipulation des données)
- Bibliothèques standards Python (string)

## 📊 Fonctionnalités

1. Lecture et traitement des tweets depuis un fichier CSV
2. Analyse des sentiments basée sur des dictionnaires de mots positifs et négatifs
3. Calcul des scores de sentiment:
   - Score positif
   - Score négatif
   - Score net (différence entre positif et négatif)
4. Visualisation de la corrélation entre les sentiments et les retweets
5. Export des résultats dans un fichier CSV

## 📁 Structure du Projet

```
├── negative_words.txt          # Liste des mots négatifs
├── positive_words.txt          # Liste des mots positifs
├── project_twitter_data.csv    # Données des tweets à analyser
├── project_twitter.ipynb       # Notebook principal
├── scripts/
│   └── tweetclaw_to_project_csv.py # Convertisseur CSV TweetClaw
└── result_data.csv            # Résultats de l'analyse
```

## 🚀 Comment Utiliser

1. Assurez-vous d'avoir Python et les bibliothèques requises installées:
   ```bash
   pip install pandas
   ```
2. Placez vos fichiers de données (tweets et listes de mots) dans le même répertoire
3. Exécutez le notebook Jupyter `project_twitter.ipynb`

### Utiliser un export TweetClaw

Le notebook lit `project_twitter_data.csv` avec les colonnes `tweet_text`,
`retweet_count` et `reply_count`. Le script suivant convertit un export TweetClaw
CSV, JSON ou JSONL dans ce format:

```bash
python scripts/tweetclaw_to_project_csv.py tweetclaw_export.json project_twitter_data.csv
```

Les champs de texte acceptés sont `tweet_text`, `text`, `full_text`, `content`,
`body` et `tweet`. Les métriques absentes sont remplacées par `0` pour conserver
un fichier compatible avec le notebook.

## 📊 Analyse Détaillée des Résultats

### 1. Vue d'ensemble des données

Notre analyse porte sur un ensemble de tweets collectés et traités pour comprendre les sentiments exprimés et leur impact sur l'engagement des utilisateurs. L'analyse se concentre sur trois aspects principaux :

- Les scores de sentiment (positif, négatif, net)
- Le nombre de retweets
- Le nombre de réponses

### 2. Distribution des Sentiments

#### 2.1 Scores de Sentiment

Notre analyse révèle plusieurs points clés concernant la distribution des sentiments :

- **Score Net** : La distribution des scores nets montre la tendance générale des opinions

  - Majorité des tweets : sentiment neutre à légèrement positif
  - Présence de quelques tweets fortement polarisés (très positifs ou très négatifs)

- **Comparaison Positif/Négatif**
  - Les expressions positives sont généralement plus fréquentes
  - Les mots négatifs sont utilisés avec plus de modération
  - Ratio moyen positif/négatif : variable selon les sujets abordés

### 3. Engagement et Sentiment

#### 3.1 Corrélation avec les Retweets

L'analyse de la relation entre les sentiments et les retweets révèle :

- Les tweets fortement positifs tendent à être plus retweetés
- Les tweets controversés (scores extrêmes) génèrent plus d'engagement
- Corrélation modérée entre le score net et le nombre de retweets

#### 3.2 Impact sur les Réponses

Les données montrent que :

- Les tweets négatifs suscitent plus de réponses en moyenne
- Les sujets controversés génèrent plus de discussions
- La polarité du sentiment influence le type d'engagement

### 4. Observations Clés

#### 4.1 Tendances Principales

1. **Engagement Positif**

   - Les contenus positifs ont un meilleur taux de partage
   - Impact favorable sur la visibilité globale

2. **Discussions et Débats**

   - Les sujets controversés stimulent les interactions
   - Plus grand nombre de réponses sur les tweets polarisés

3. **Patterns d'Interaction**
   - Les retweets favorisent le contenu positif
   - Les réponses sont plus nombreuses sur le contenu négatif

#### 4.2 Implications Pratiques

Ces résultats ont plusieurs implications importantes :

1. **Pour la Communication**

   - Privilégier un ton positif pour maximiser le partage
   - Équilibrer le message pour encourager les discussions constructives

2. **Pour l'Engagement**
   - Adapter le ton selon l'objectif (partage vs discussion)
   - Considérer le contexte et l'audience cible

### 5. Recommandations

Sur la base de notre analyse, nous recommandons :

1. **Stratégie de Contenu**

   - Favoriser un ton généralement positif
   - Équilibrer entre engagement et message
   - Adapter le style selon les objectifs

2. **Mesures d'Impact**

   - Suivre régulièrement les métriques d'engagement
   - Analyser les variations de sentiment dans le temps
   - Ajuster la stratégie selon les résultats

3. **Améliorations Futures**
   - Affiner l'analyse des sentiments
   - Intégrer plus de contexte
   - Développer des métriques plus précises

### 6. Limitations de l'Étude

Il est important de noter certaines limitations :

1. **Méthodologiques**

   - Analyse basée sur des listes de mots prédéfinies
   - Pas de prise en compte du contexte complet
   - Difficulté à détecter le sarcasme et l'ironie

2. **Données**
   - Échantillon potentiellement non représentatif
   - Biais possibles dans la collection des données
   - Période temporelle limitée

### 7. Conclusion

Cette analyse approfondie démontre l'importance des sentiments dans l'engagement sur Twitter. Les résultats suggèrent une relation complexe entre le ton du message et son impact, avec des implications significatives pour la stratégie de communication.

## 🔍 Méthodologie

1. Prétraitement des tweets (suppression de la ponctuation)
2. Identification des mots positifs et négatifs
3. Calcul des scores de sentiment
4. Analyse de la corrélation avec les métriques d'engagement
5. Visualisation des résultats
