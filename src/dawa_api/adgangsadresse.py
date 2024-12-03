from dataclasses import asdict, dataclass
from typing import Optional

from dataclasses_json import Undefined, dataclass_json


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class AdgangsadresseMini:
    """
    Data class containing the informations returned from the 'adgangsadresse'
    endpoint when requested with the 'struktur' parameter equals 'mini'.
    Reference:
    https://dawadocs.dataforsyningen.dk/dok/api/adgangsadresse#databeskrivelse
    """

    id: Optional[str] = None
    status: Optional[int] = None
    darstatus: Optional[int] = None
    vejkode: Optional[str] = None
    vejnavn: Optional[str] = None
    adresseringsvejnavn: Optional[str] = None
    husnr: Optional[str] = None
    supplerendebynavn: Optional[str] = None
    postnr: Optional[str] = None
    postnrnavn: Optional[str] = None
    stormodtagerpostnr: Optional[str] = None
    stormodtagerpostnrnavn: Optional[str] = None
    kommunekode: Optional[str] = None
    x: Optional[float] = None
    y: Optional[float] = None
    href: Optional[str] = None
    betegnelse: Optional[str] = None


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class AdgangsadresseFlad:
    """
    Data class containing the informations returned from the 'adgangsadresse'
    endpoint when requested with the 'struktur' parameter equals 'flad'.
    Reference:
    https://dawadocs.dataforsyningen.dk/dok/api/adgangsadresse#databeskrivelse
    """

    id: Optional[str] = None
    status: Optional[int] = None
    darstatus: Optional[int] = None
    oprettet: Optional[str] = None
    ændret: Optional[str] = None
    vejkode: Optional[str] = None
    vejnavn: Optional[str] = None
    adresseringsvejnavn: Optional[str] = None
    husnr: Optional[str] = None
    supplerendebynavn: Optional[str] = None
    postnr: Optional[str] = None
    postnrnavn: Optional[str] = None
    stormodtagerpostnr: Optional[str] = None
    stormodtagerpostnrnavn: Optional[str] = None
    kommunekode: Optional[str] = None
    kommunenavn: Optional[str] = None
    ejerlavkode: Optional[int] = None
    ejerlavnavn: Optional[str] = None
    matrikelnr: Optional[str] = None
    esrejendomsnr: Optional[str] = None
    etrs89koordinat_øst: Optional[float] = None
    etrs89koordinat_nord: Optional[float] = None
    wgs84koordinat_bredde: Optional[float] = None
    wgs84koordinat_længde: Optional[float] = None
    nøjagtighed: Optional[str] = None
    kilde: Optional[int] = None
    tekniskstandard: Optional[str] = None
    tekstretning: Optional[int] = None
    adressepunktændringsdato: Optional[str] = None
    ddkn_m100: Optional[str] = None
    ddkn_km1: Optional[str] = None
    ddkn_km10: Optional[str] = None
    regionskode: Optional[str] = None
    regionsnavn: Optional[str] = None
    jordstykke_ejerlavkode: Optional[int] = None
    jordstykke_matrikelnr: Optional[str] = None
    jordstykke_esrejendomsnr: Optional[str] = None
    jordstykke_ejerlavnavn: Optional[str] = None
    højde: Optional[float] = None
    adgangspunktid: Optional[str] = None
    vejpunkt_id: Optional[str] = None
    vejpunkt_kilde: Optional[str] = None
    vejpunkt_nøjagtighed: Optional[str] = None
    vejpunkt_tekniskstandard: Optional[str] = None
    vejpunkt_x: Optional[float] = None
    vejpunkt_y: Optional[float] = None
    sognekode: Optional[str] = None
    sognenavn: Optional[str] = None
    politikredskode: Optional[str] = None
    politikredsnavn: Optional[str] = None
    retskredskode: Optional[str] = None
    retskredsnavn: Optional[str] = None
    opstillingskredskode: Optional[str] = None
    opstillingskredsnavn: Optional[str] = None
    menighedsrådsafstemningsområdenummer: Optional[int] = None
    menighedsrådsafstemningsområdenavn: Optional[str] = None
    zone: Optional[str] = None
    afstemningsområdenummer: Optional[str] = None
    afstemningsområdenavn: Optional[str] = None
    brofast: Optional[bool] = None
    supplerendebynavn_dagi_id: Optional[str] = None
    navngivenvej_id: Optional[str] = None
    vejpunkt_ændret: Optional[str] = None
    ikrafttrædelse: Optional[str] = None
    nedlagt: Optional[str] = None
    storkredsnummer: Optional[str] = None
    storkredsnavn: Optional[str] = None
    valglandsdelsbogstav: Optional[str] = None
    valglandsdelsnavn: Optional[str] = None
    landsdelsnuts3: Optional[str] = None
    landsdelsnavn: Optional[str] = None
    betegnelse: Optional[str] = None
    kvh: Optional[str] = None


@dataclass
class AdresseQuery:
    """Class for constructing adgangsadresse queries.
    Reference:
    https://dawadocs.dataforsyningen.dk/dok/api/adgangsadresse
    """

    q: Optional[str] = None
    autocomplete: Optional[str] = None
    fuzzy: Optional[str] = None
    kvh: Optional[str] = None
    id: Optional[str] = None
    status: Optional[int] = None
    vejkode: Optional[int] = None
    vejnavn: Optional[str] = None
    husnr: Optional[str] = None
    husnrfra: Optional[str] = None
    husnrtil: Optional[str] = None
    supplerendebynavn: Optional[str] = None
    postnr: Optional[str] = None
    kommunekode: Optional[int] = None
    ejerlavkode: Optional[str] = None
    matrikelnr: Optional[str] = None
    srid: Optional[int] = None
    polygon: Optional[str] = None
    cirkel: Optional[str] = None
    nøjagtighed: Optional[str] = None
    regionskode: Optional[str] = None
    landsdelsnuts3: Optional[str] = None
    sognekode: Optional[str] = None
    afstemningsområdenummer: Optional[str] = None
    opstillingskredsnummer: Optional[str] = None
    storkredsnummer: Optional[str] = None
    valglandsdelsbogstav: Optional[str] = None
    retskredskode: Optional[str] = None
    politikredskode: Optional[str] = None
    stednavnid: Optional[str] = None
    stedid: Optional[str] = None
    stednavnafstand: Optional[str] = None
    stedaftand: Optional[str] = None
    bebyggelsesid: Optional[str] = None
    bebyggelsestype: Optional[str] = None
    adgangspunktid: Optional[str] = None
    vejpunkt_id: Optional[str] = None
    navngivenvej_id: Optional[str] = None
    geometri: Optional[str] = None
    callback: Optional[str] = None
    format: Optional[str] = None
    noformat: Optional[str] = None
    ndjson: Optional[str] = None
    side: Optional[int] = None
    per_side: Optional[int] = None
    struktur: Optional[str] = "mini"
    medtagugyldige: Optional[str] = None
    medtagnedlagte: Optional[str] = None

    def as_params(self):
        """Return Query instance as dictionary"""
        return asdict(
            self, dict_factory=lambda x: {k: v for (k, v) in x if v is not None}
        )
