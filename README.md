# validkit

Eine kleine, eigenständige Python-Bibliothek ohne externe Abhängigkeiten, die neun
unabhängige, reine Prüf- und Normalisierungsfunktionen bereitstellt:

`is_valid_email`, `luhn_check`, `is_valid_iban`, `is_valid_isbn13`,
`normalize_phone`, `strip_accents`, `mask_secret`, `slugify` und `clamp`.

Alle Funktionen sind typannotiert und melden ungültige Eingaben mit
aussagekräftigen Fehlern. Die öffentliche API wird über `validkit/__init__.py`
exportiert.

## Tech-Stack

- **Sprache**: Python
- **Runtime**: Python 3.10+
- **Test-Framework**: pytest
- **Abhängigkeiten**: ausschließlich Python-Standardbibliothek
- **Packaging**: setuptools / `pyproject.toml`

## Installation

```bash
pip install -e .
```

## Tests ausführen

```bash
pytest
```

## Verwendung

```python
import validkit
```

Alle neun Funktionen sind direkt über `validkit.<name>` erreichbar:

### `is_valid_email(text) -> bool`

```python
validkit.is_valid_email("user@example.com")  # True
validkit.is_valid_email("user@example")  # False
```

### `luhn_check(digits) -> bool`

```python
validkit.luhn_check("4532 0148 1655 3921")  # True
validkit.luhn_check("4532 0148 1655 3922")  # False
```

### `is_valid_iban(text) -> bool`

```python
validkit.is_valid_iban("DE89 3704 0044 0532 0130 00")  # True
```

### `is_valid_isbn13(text) -> bool`

```python
validkit.is_valid_isbn13("978-3-16-148410-0")  # True
```

### `normalize_phone(text, country_code) -> str`

```python
validkit.normalize_phone("030 1234567", "DE")  # '+49301234567'
```

### `strip_accents(text) -> str`

```python
validkit.strip_accents("café au lait — déjà")  # 'cafe au lait — deja'
```

### `mask_secret(text, keep=4) -> str`

```python
validkit.mask_secret("geheim123456789", keep=4)  # '*********6789'
```

### `slugify(text) -> str`

```python
validkit.slugify("Héllo Wörld!  Test -- x")  # 'hello-world-test-x'
```

### `clamp(value, low, high) -> float`

```python
validkit.clamp(5, 0, 10)  # 5
validkit.clamp(-5, 0, 10)  # 0
validkit.clamp(15, 0, 10)  # 10
```

## Feature-Liste

- E-Mail-Validierung
- Luhn-Prüfziffer
- IBAN-Validierung
- ISBN-13-Prüfsumme
- Telefonnummer-Normalisierung
- Diakritika-Entfernung
- Geheimnis-Maskierung
- Slug-Erzeugung
- Werte-Clamping
