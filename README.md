# Yatzy-app

## Dokumentaatio

- [Changelog](./dokumentaatio/changelog.md)
- [Tuntikirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)

## Asennus

1. Riippuvuuksien asentamiseen käytä komentoa: 
```bash
poetry install
```

2. Ohjelman aloittamiseen käytä komentoa:
```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Suoritus
```bash
poetry run invoke start
```

### Testaus
```bash
poetry run invoke test
```

### Testikattavuusraportti

```bash
poetry run invoke coverage-report
```

