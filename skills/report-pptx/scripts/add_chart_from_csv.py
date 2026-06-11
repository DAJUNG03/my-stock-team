# -*- coding: utf-8 -*-
"""기술적 분석 CSV의 날짜·종가를 payload JSON의 price.chart에 주입한다.

사용법: python add_chart_from_csv.py <payload.json> <ohlcv.csv> [차트제목]
CSV는 Date, Close 컬럼을 포함해야 한다. 250포인트 초과 시 균등 다운샘플.
"""
import csv
import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def main():
    payload_path, csv_path = sys.argv[1], sys.argv[2]
    title = sys.argv[3] if len(sys.argv) > 3 else "종가 추이 (원)"
    dates, values = [], []
    with open(csv_path, encoding="utf-8-sig") as f:
        for row in csv.DictReader(f):
            d, c = row.get("Date"), row.get("Close")
            if d and c:
                dates.append(d[5:] if len(d) == 10 else d)  # MM-DD로 축약
                values.append(float(c))
    if not values:
        print("[경고] CSV에서 Date/Close를 찾지 못함 — 차트 생략")
        return
    with open(payload_path, encoding="utf-8") as f:
        payload = json.load(f)
    payload.setdefault("price", {})["chart"] = {
        "dates": dates, "values": values, "title": title}
    with open(payload_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
    print(f"OK: 차트 {len(values)}포인트 주입 ({dates[0]} ~ {dates[-1]})")


if __name__ == "__main__":
    main()
