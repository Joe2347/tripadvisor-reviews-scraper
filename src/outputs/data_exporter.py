thonimport json
import csv

class DataExporter:
    @staticmethod
    def export_to_json(data, filename='output.json'):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def export_to_csv(data, filename='output.csv'):
        if data:
            keys = data[0].keys()
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=keys)
                writer.writeheader()
                writer.writerows(data)