import json
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

class ExtractionError(Exception):
    pass

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def extract(file_bytes: bytes, content_type: str) -> dict:
    prompt = """Tu es un système d'extraction de données de documents.

Analyse le document fourni et extrais UNIQUEMENT les informations qui sont réellement présentes dans le document.

Règles strictes :
- Ne jamais inventer une information absente du document. Si un champ n'existe pas dans le document, mets sa valeur à null.
- Réponds UNIQUEMENT avec un objet JSON valide, sans texte avant ou après, sans balises markdown (pas de ```json).
- Identifie d'abord le type de document (facture, carte d'identité, attestation, etc.) dans un champ "document_type".
- Structure les autres champs selon les informations réellement trouvées (par exemple : nom, date, montant, numéro de référence, etc.), en gardant des noms de champs clairs en anglais (snake_case).
"""

    fichier_pour_gemini = types.Part.from_bytes(data=file_bytes, mime_type=content_type)
    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=[prompt, fichier_pour_gemini],
            config={"response_mime_type": "application/json"},
        )

        donnees_extraites = json.loads(response.text)
    except Exception as erreur:
        raise ExtractionError(f"L'extraction a échoué : {erreur}")


    return donnees_extraites
import json
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def extract(file_bytes: bytes, content_type: str) -> dict:
    prompt = """Tu es un système d'extraction de données de documents.

Analyse le document fourni et extrais UNIQUEMENT les informations qui sont réellement présentes dans le document.

Règles strictes :
- Ne jamais inventer une information absente du document. Si un champ n'existe pas dans le document, mets sa valeur à null.
- Réponds UNIQUEMENT avec un objet JSON valide, sans texte avant ou après, sans balises markdown (pas de ```json).
- Identifie d'abord le type de document (facture, carte d'identité, attestation, etc.) dans un champ "document_type".
- Structure les autres champs selon les informations réellement trouvées (par exemple : nom, date, montant, numéro de référence, etc.), en gardant des noms de champs clairs en anglais (snake_case).
"""

    fichier_pour_gemini = types.Part.from_bytes(data=file_bytes, mime_type=content_type)
    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=[prompt, fichier_pour_gemini],
            config={"response_mime_type": "application/json"},
        )

        donnees_extraites = json.loads(response.text)
    except Exception as erreur:
        raise ExtractionError(f"L'extraction a échoué : {erreur}")


    return donnees_extraites