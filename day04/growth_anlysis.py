import csv
import matplotlib
matplotlib.use('Agg')  # מונע התנגשויות של ממשק גרפי בשרת
import matplotlib.pyplot as plt
import os

def analyze_and_plot(csv_filepath, output_img_path):
    """ calcules the average growth rate and maximum yield from a CSV file containing time and OD600 measurements, and generates a growth curve plot saved as an image.
   
    """
    times = []
    ods = []

    with open(csv_filepath, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            times.append(float(row['time_hours']))
            ods.append(float(row['od600']))

    # calculating average growth rate and maximum yield
    total_time_diff = times[-1] - times[0]
    total_od_diff = ods[-1] - ods[0]
    avg_growth_rate = total_od_diff / total_time_diff
    max_yield = max(ods)

    # creating the plot and saving it as an image
    plt.figure(figsize=(6, 4))
    plt.plot(times, ods, marker='o', color='#3498db', linewidth=2, label='OD600')
    plt.title('Bacterial Growth Curve', fontsize=12)
    plt.xlabel('Time (hours)', fontsize=10)
    plt.ylabel('OD600', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    
    # saving the image to the specified path
    plt.savefig(output_img_path)
    plt.close()

    return avg_growth_rate, max_yield
def smooth_single_dips(ods):
    """מתקנת נפילות רעש נקודתיות: אם מדידה נמוכה גם מהקודמת וגם מהבאה, היא מוחלפת בממוצע שלהן."""
    cleaned = list(ods)
    for i in range(1, len(cleaned) - 1):
        if cleaned[i] < cleaned[i - 1] and cleaned[i] < cleaned[i + 1]:
            cleaned[i] = (cleaned[i - 1] + cleaned[i + 1]) / 2
    return cleaned