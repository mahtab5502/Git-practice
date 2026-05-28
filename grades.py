SUBJECTS = ["Math", "English", "Science"]

def get_scores():
    scores = {}

    for subject in SUBJECTS:
        score = float(input(f"{subject} score: "))
        scores[subject] = score

    return scores


def calculate_average(scores):
    return sum(scores.values()) / len(scores)


if __name__ == "__main__":
    scores = get_scores()

    average = calculate_average(scores)

    print("Average:", average)