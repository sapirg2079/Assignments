import csv

def calculate_average_growth_rate(csv_filepath):
    """
    Calculates the simple average growth rate between the first and last measurement.
    """
    times = []
    ods = []

    with open(csv_filepath, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            times.append(float(row['time_hours']))
            ods.append(float(row['od600']))

    # Delta OD / Delta Time
    total_time_diff = times[-1] - times[0]
    total_od_diff = ods[-1] - ods[0]
    
    avg_growth_rate = total_od_diff / total_time_diff
    return avg_growth_rate

def main():
    csv_file = r"C:\Users\sapir\Documents\python course\Assignments\day03\data.csv"
    rate = calculate_average_growth_rate(csv_file)
    
    print(f"Average growth rate: {rate:.3f} OD/hour")

if __name__ == "__main__":
    main()