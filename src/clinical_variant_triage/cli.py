import argparse
from clinical_variant_triage.core import build_snapshot


def main() -> None:
    parser = argparse.ArgumentParser(description="Variant triage helpers with review queues, labels, and concise evidence bundles.")
    parser.add_argument("--summary", action="store_true")
    args = parser.parse_args()
    if args.summary:
        print(build_snapshot())


if __name__ == "__main__":
    main()
