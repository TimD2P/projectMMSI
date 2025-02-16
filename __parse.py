import csv
from datetime import datetime

file_path = "AIS_2024_09_10.csv"
output_path = f"done_{file_path}"

def filter_ais_messages(file_path, output_path):
    records = {}

    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Читаем заголовки отдельно

        for row in reader:
            mmsi, timestamp = row[0], row[1]
            dt = datetime.fromisoformat(timestamp)
            hour_key = (mmsi, dt.replace(minute=0, second=0, microsecond=0))
            if hour_key not in records or dt < records[hour_key]["timestamp"]:
                records[hour_key] = {"timestamp": dt, "row": row}

    with open(output_path, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)  # Записываем заголовки в новый файл
        for record in records.values():
            record["row"][1] = record["timestamp"].isoformat()  # Приводим время к ISO 8601
            writer.writerow(record["row"])

filter_ais_messages(file_path, output_path)
