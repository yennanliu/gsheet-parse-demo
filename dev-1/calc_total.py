import csv
import re


def parse_amount(value: str) -> float:
    """Parse currency string like 'NT$342,550' or 'HK$85,000' to float."""
    if not value or not value.strip():
        return 0.0
    # Remove currency symbols and commas
    cleaned = re.sub(r'[NT$HK$,]', '', value.strip())
    try:
        return float(cleaned)
    except ValueError:
        return 0.0


def main():
    file_path = 'data-1.csv'

    total_twd = 0.0
    total_hkd = 0.0

    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Skip summary rows (row 15 in original has different format)
            if not row.get('交易日期'):
                continue

            twd_amount = parse_amount(row.get('台幣金額', ''))
            hkd_amount = parse_amount(row.get('港幣金額', ''))

            total_twd += twd_amount
            total_hkd += hkd_amount

    print(f"Total TWD (台幣): NT${total_twd:,.2f}")
    print(f"Total HKD (港幣): HK${total_hkd:,.2f}")


if __name__ == '__main__':
    main()
