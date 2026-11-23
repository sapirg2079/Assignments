import pytest
from growth_anlysis import analyze_and_plot, smooth_single_dips


def test_analyze_and_plot_normal_growth(tmp_path):
    """בדיקת חישוב תקין של קצב גידול, תפוקה מקסימלית ויצירת קובץ גרף."""
    # יצירת קובץ CSV זמני עם נתוני מדידה
    csv_file = tmp_path / "sample_growth.csv"
    csv_file.write_text(
        "time_hours,od600\n"
        "0,0.1\n"
        "2,0.5\n"
        "4,0.9\n",
        encoding="utf-8"
    )
    output_img = tmp_path / "growth_curve.png"

    rate, max_yield = analyze_and_plot(str(csv_file), str(output_img))

    # חישוב צפוי: (0.9 - 0.1) / (4 - 0) = 0.2
    assert rate == pytest.approx(0.2)
    assert max_yield == pytest.approx(0.9)
    # וידוא שקובץ התמונה נוצר ואינו ריק
    assert output_img.exists()
    assert output_img.stat().st_size > 0


def test_max_yield_in_middle_of_experiment(tmp_path):
    """וידוא ש-max_yield מחזיר את הערך הגבוה ביותר גם אם בסוף הניסוי יש ירידה (שלב התמותה)."""
    csv_file = tmp_path / "decline_growth.csv"
    csv_file.write_text(
        "time_hours,od600\n"
        "0,0.2\n"
        "5,1.8\n"
        "10,1.2\n",
        encoding="utf-8"
    )
    output_img = tmp_path / "decline_curve.png"

    rate, max_yield = analyze_and_plot(str(csv_file), str(output_img))

    # קצב ממוצע בין ההתחלה לסוף: (1.2 - 0.2) / 10 = 0.1
    assert rate == pytest.approx(0.1)
    # השיא היה באמצע הניסוי (1.8), לא בסוף
    assert max_yield == pytest.approx(1.8)


def test_empty_csv_raises_error(tmp_path):
    """בדיקת מקרה קצה: קובץ CSV עם כותרות בלבד וללא שורות נתונים."""
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("time_hours,od600\n", encoding="utf-8")
    output_img = tmp_path / "empty.png"

    with pytest.raises(IndexError):
        analyze_and_plot(str(csv_file), str(output_img))


def test_zero_time_difference_raises_error(tmp_path):
    """בדיקת מקרה קצה: הפרש זמנים אפס שגורם לחלוקה באפס."""
    csv_file = tmp_path / "zero_time.csv"
    csv_file.write_text(
        "time_hours,od600\n"
        "2,0.1\n"
        "2,0.5\n",
        encoding="utf-8"
    )
    output_img = tmp_path / "zero_time.png"

    with pytest.raises(ZeroDivisionError):
        analyze_and_plot(str(csv_file), str(output_img))


def test_missing_columns_raises_error(tmp_path):
    """בדיקת מקרה קצה: קובץ CSV עם שמות עמודות שגויים."""
    csv_file = tmp_path / "bad_headers.csv"
    csv_file.write_text(
        "time,od\n"
        "0,0.1\n"
        "2,0.5\n",
        encoding="utf-8"
    )
    output_img = tmp_path / "bad_headers.png"

    with pytest.raises(KeyError):
        analyze_and_plot(str(csv_file), str(output_img))

    from growth_anlysis import smooth_single_dips

def test_smooth_single_dips_fixes_noise():
    # נתונים עם נפילת רעש בשעה השלישית (0.2 במקום ~0.5)
    raw_ods = [0.1, 0.4, 0.2, 0.6, 0.9]
    
    cleaned_ods = smooth_single_dips(raw_ods)
    
    # הערך 0.2 אמור להתחלף בממוצע של 0.4 ו-0.6 (שהוא 0.5)
    assert cleaned_ods == [0.1, 0.4, 0.5, 0.6, 0.9]