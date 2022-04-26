# Yatzy-app

## Dokumentaatio

- [Changelog](./dokumentaatio/changelog.md)
- [Tuntikirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Riippuvuuksien asentamiseen käytä "yatzy-app" repositorion sisällä komentoa: 
```bash
poetry install
```

2. Ohjelman aloittamiseen käytä "yatzy-app" repositorion sisällä komentoa:
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

### Pylint

Tiedoston [.pylintrc](./.pylintrc) tarkastukset tehdään "yatzy-app" repositorion sisällä komennolla:

```bash
poetry run invoke lint
```
