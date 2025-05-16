import json
import os

learning_path = {
    "Python Programming": [
        "Variables and Data Types",
        "Control Structures (if, for, while)",
        "Functions and Modules",
        "File Handling"
    ],
    "Math & Statistics": [
        "Linear Algebra Basics",
        "Probability & Statistics",
        "Descriptive Statistics",
        "Inferential Statistics"
    ],
    "Data Analysis (Pandas, NumPy)": [
        "Working with arrays",
        "DataFrames and Series",
        "Data Cleaning and Preprocessing",
        "Grouping and Aggregating"
    ],
    "Data Visualization": [
        "Line and Bar Charts",
        "Histograms and Boxplots",
        "Scatter Plots",
        "Correlation and Heatmaps"
    ],
    "Machine Learning": [
        "Supervised vs Unsupervised Learning",
        "Linear Regression",
        "Classification (KNN, SVM)",
        "Model Evaluation (Accuracy, F1 Score)"
    ],
    "Projects & Practice": [
        "Titanic Dataset Analysis",
        "Sales Forecasting Project",
        "Customer Segmentation",
        "Deploying a ML Model"
    ]
}

PROGRESS_FILE = "progress.json"

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return []

def save_progress(progress):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f)

def show_learning_path(progress):
    for i, (module, topics) in enumerate(learning_path.items(), 1):
        print(f"\n{i}. {module}")
        for idx, topic in enumerate(topics, 1):
            print(f"   {idx}. {topic}")

def mark_completed(progress):
    show_learning_path(progress)
    topic = input("\nEnter exact topic name you completed: ").strip()
    if any(topic in topics for topics in learning_path.values()):
        if topic not in progress:
            progress.append(topic)
            save_progress(progress)
            print(f"Marked '{topic}' as completed!")
        else:
            print("Topic already marked completed.")
    else:
        print("Topic not found.")

def view_progress(progress):
    total = sum(len(t) for t in learning_path.values())
    done = len(progress)
    print(f"\nCompleted {done}/{total} topics ({done / total * 100:.2f}%)")

    module_completed = {}
    for topic in progress:
        for module, topics in learning_path.items():
            if topic in topics:
                module_completed.setdefault(module, []).append(topic)
                break

    for module, topics_completed in module_completed.items():
        print(f"{module} :")
        topics_completed_sorted = sorted(topics_completed, key=lambda t: learning_path[module].index(t))
        for topic in topics_completed_sorted:
            idx = learning_path[module].index(topic) + 1
            print(f"   {idx}. {topic}")

def main():
    progress = load_progress()
    while True:
        print("\n1. View Learning Path\n2. Mark Topic Completed\n3. View Progress\n4. Exit")
        choice = input("Choose (1-4): ").strip()
        if choice == '1':
            show_learning_path(progress)
        elif choice == '2':
            mark_completed(progress)
        elif choice == '3':
            view_progress(progress)
        elif choice == '4':
            print("Good luck learning!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
