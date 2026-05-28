SUBJECTS = ["국어", "영어", "수학", "과탐"]

def get_scores():
    scores = {}

    for subject in SUBJECTS:
        score = float(input(f"{subject} 점수: "))
        scores[subject] = score

    return scores

def calculate_average(scores):
    return sum(scores.values()) / len(scores)

if __name__ == "__main__":
    scores = get_scores()

    average = calculate_average(scores)

    print(scores)
    print("평균:", average)