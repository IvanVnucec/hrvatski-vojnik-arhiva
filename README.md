# Arhiva časopisa "Hrvatski vojnik"

Repozitorij sadrži arhivu časopisa "Hrvatski vojnik" preuzetih sa službene stranice [hrvatski-vojnik.hr](https://hrvatski-vojnik.hr/).
Preuzete časopise možete pronaći u direktoriju `arhiva` u PDF formatu.
Časopisi se automatski preuzimaju pomoću skripti koje se također nalaze u repozitoriju. Preuzimanje časopisa odvija se jednom dnevno u 03:00h pomoću _GitHub Actions_-a.

## Korištenje

```bash
# Aktivirajte virtualno okruženje
virtualenv .venv
source .venv/bin/activate

# Instalirajte potrebne pakete
pip install -r requirements.txt

# Pokrenite preuzimanje časopisa
python3 main.py
```
