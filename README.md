# 📄 DocExtract API

API REST qui extrait automatiquement des données structurées (JSON) depuis n'importe quel document (PDF, image), via l'IA générative (Google Gemini). Aucune règle d'extraction codée en dur par type de document : le modèle détecte et structure lui-même le contenu.

**🔗 Démo en ligne :** https://docextract-api-yzhl.onrender.com/docs

## 🚀 Points forts

- Extraction générique : factures, attestations, tickets de caisse, cartes d'identité, etc.
- Détection automatique du type de document
- Gestion d'erreurs robuste : un échec d'extraction (IA indisponible) est capturé proprement, jamais de crash
- API sécurisée par clé API (`X-API-Key`)
- Testé automatiquement, conteneurisé, déployé en production

## 🛠️ Stack

FastAPI · PostgreSQL · SQLAlchemy · Pydantic · Google Gemini API · Pytest · Docker · Render

## 📡 Endpoints

| Méthode | Endpoint | Description |
|---|---|---|
| GET | `/health` | Statut de l'API |
| POST | `/extractions` | Upload un document, lance l'extraction |
| GET | `/extractions` | Liste paginée des extractions |
| GET | `/extractions/{id}` | Détail d'une extraction |
| DELETE | `/extractions/{id}` | Supprime une extraction |

```bash
curl -X POST "https://docextract-api-yzhl.onrender.com/extractions" \
  -H "x-api-key: VOTRE_CLE_API" \
  -F "file=@document.pdf;type=application/pdf"
```

```json
{
  "status": "completed",
  "extracted_data": {
    "document_type": "receipt",
    "merchant_name": "LIDL",
    "total_amount": 8.11
  }
}
```

## ⚙️ Démarrage rapide

```bash
git clone https://github.com/mohyieddine-kamal/docextract-api.git
cd docextract-api
pip install -r requirements.txt
# .env : DATABASE_URL, API_KEY, GEMINI_API_KEY
uvicorn main:app --reload
```

Ou avec Docker, sans rien installer :
```bash
docker compose up --build
```

## ✅ Tests

```bash
python3 -m pytest
```

## ⚠️ Limites & 🔮 Améliorations futures

L'extraction reste soumise aux limites d'un LLM (hallucination possible) ; une vérification humaine est recommandée pour un usage critique. Pistes futures : clés API multi-utilisateurs, interface web, traitement asynchrone en file d'attente.
