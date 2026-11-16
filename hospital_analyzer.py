import pandas as pd
import matplotlib.pyplot as plt


def load_data(file_name):
    try:
        return pd.read_csv(file_name)
    except FileNotFoundError:
        print("File not found:", file_name)
        return None


def clean_data(data):
    data = data.copy()

    before = len(data)
    data = data.drop_duplicates(subset="Patient_ID")
    removed = before - len(data)
    if removed > 0:
        print("Duplicates removed:", removed)

    data["Age"] = pd.to_numeric(data["Age"], errors="coerce")
    data.loc[(data["Age"] < 0) | (data["Age"] > 120), "Age"] = None

    data["Admit_Date"] = pd.to_datetime(data["Admit_Date"], errors="coerce")
    data["Discharge_Date"] = pd.to_datetime(data["Discharge_Date"], errors="coerce")
    data = data.dropna(subset=["Admit_Date", "Discharge_Date"])
    data = data[data["Discharge_Date"] >= data["Admit_Date"]]

    data["Department"] = data["Department"].fillna("Unknown")
    data["Gender"] = data["Gender"].fillna("Unknown")

    missing_age = data["Age"].isna().sum()
    if missing_age > 0:
        median_age = data["Age"].median()
        data["Age"] = data["Age"].fillna(median_age)
        print("Missing Age filled with median:", format(median_age, "g"))

    data["Stay_Days"] = (data["Discharge_Date"] - data["Admit_Date"]).dt.days
    return data.reset_index(drop=True)


def show_department_count(data):
    counts = data.groupby("Department")["Patient_ID"].count()
    parts = [name + ": " + str(count) for name, count in counts.items()]
    print(" | ".join(parts))
    print("Total patients:", len(data))


def show_gender_count(data):
    counts = data.groupby("Gender")["Patient_ID"].count()
    parts = [name + ": " + str(count) for name, count in counts.items()]
    print(" | ".join(parts))


def plot_bar_chart(labels, values, title, x_label, y_label):
    plt.figure(figsize=(7, 4))
    plt.bar(labels, values, color="steelblue")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.tight_layout()
    plt.show()


def show_length_of_stay(data):
    for _, row in data.iterrows():
        print(row["Patient_ID"] + ": " + str(row["Stay_Days"]) + " days")
    print("Average stay:", format(data["Stay_Days"].mean(), ".2f"), "days")

    department_stay = data.groupby("Department")["Stay_Days"].mean()
    plot_bar_chart(
        department_stay.index,
        department_stay.values,
        "Average Length of Stay by Department",
        "Department",
        "Days",
    )


def get_age_groups(data):
    groups = pd.cut(
        data["Age"],
        bins=[-1, 40, 60, 200],
        labels=["0-40", "41-60", "61+"],
    )
    return groups.value_counts().reindex(["0-40", "41-60", "61+"])


def show_stay_and_age_groups(data):
    print("Average stay:", format(data["Stay_Days"].mean(), ".2f"), "days")

    age_counts = get_age_groups(data)
    parts = [label + ": " + str(count) for label, count in age_counts.items()]
    print("Age groups:", " | ".join(parts))

    plot_bar_chart(
        age_counts.index,
        age_counts.values,
        "Patients by Age Group",
        "Age Group",
        "Number of Patients",
    )
    print("Bar chart displayed")


def show_menu():
    print()
    print("===== Hospital Patient Data Analyzer =====")
    print("1. Department count")
    print("2. Length of stay")
    print("3. Stay and age groups")
    print("4. Gender count")
    print("5. Exit")


def main():
    file_name = input("Enter CSV file name (press Enter for patients.csv): ").strip()
    if file_name == "":
        file_name = "patients.csv"

    raw_data = load_data(file_name)
    if raw_data is None:
        return

    data = clean_data(raw_data)
    if data.empty:
        print("No valid records found.")
        return

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_department_count(data)
        elif choice == "2":
            show_length_of_stay(data)
        elif choice == "3":
            show_stay_and_age_groups(data)
        elif choice == "4":
            show_gender_count(data)
        elif choice == "5":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()
