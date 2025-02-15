#!/usr/bin/env python3

import argparse
import csv
import sys

import dawa_api as dawa
from dawa_api.adgangsadresse import AdresseQuery


def from_csv(filename: str) -> list[dict]:
    rows = []
    with open(filename, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            rows.append(row)
    return rows


def to_csv(filename: str, geocoded: list[dawa.AdgangsadresseMini]) -> None:
    with open(filename, mode="w", encoding="utf-8") as f:
        fields = ("vejnavn", "husnr", "postnr", "postnrnavn", "x", "y")
        f.write(";".join(fields) + "\n")
        for row in geocoded:
            f.write(";".join([str(getattr(row, x)) for x in fields]) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="geocode_from_csv.py",
        description="Geocode Danish postal adresses from a CSV file",
    )
    parser.add_argument(
        "-i", "--in-file", help="input file", metavar="FILENAME", required=True
    )
    parser.add_argument(
        "-o", "--out-file", help="output file", metavar="FILENAME", required=True
    )
    args = parser.parse_args()
    geocoder(in_filename=args.in_file, out_filename=args.out_file)


def geocoder(in_filename: str, out_filename: str) -> None:
    geocoded = []
    addresses = from_csv(in_filename)
    client = dawa.Client()
    for addr in addresses:
        try:
            result = client.adgangsadresser_mini(AdresseQuery(**addr))
            if result:
                r = result[0]
                geocoded.append(r)
                print(
                    f"OK:  {r.vejnavn} {r.husnr}, {r.postnr} {r.postnrnavn} ({r.x},{r.y})"
                )
            else:
                print(
                    f"ERR: {addr.get("vejnavn")} {addr.get("husnr")}, {addr.get("postnr")} | No result"
                )
        except dawa.ApiErrorConnection as error:
            print(f"Error: {error}")
            sys.exit(1)
        except dawa.ApiErrorNotFound as error:
            print(f"Error: {error}")
            sys.exit(1)
        except dawa.ApiError as error:
            print(
                f"ERR: {addr.get("vejnavn")} {addr.get("husnr")}, {addr.get("postnr")} | Error: {error}"
            )
    to_csv(out_filename, geocoded=geocoded)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Unexpected error: {error}")
        sys.exit(1)
