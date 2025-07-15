import logging

import dawa_api as dawa


dawa_logger = logging.getLogger("dawa_api")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh = logging.FileHandler("dawa_debug.log")
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
dawa_logger.addHandler(fh)
dawa_logger.setLevel(logging.DEBUG)


def main():
    dawa_logger.info("Starting.")
    client = dawa.Client()

    q = dawa.AdresseQuery(vejnavn="Christiansborg Ridebane", husnr="5", postnr="1218")
    results = client.adgangsadresser_mini(adresse_query=q)

    for res in results:
        print(res)


if __name__ == "__main__":
    main()
