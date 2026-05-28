SUBJECTS = ["국어", "영어", "수학", "과탐"]


def get_scores():
    scores = {}

    for subject in SUBJECTS:
        score = float(input(f"{subject} 점수: "))
        scores[subject] = score

    return scores


def calculate_average(scores):
    return sum(scores.values()) / len(scores)


def print_results(scores, average):
    print("점수 결과")

    for subject, score in scores.items():
        print(f"{subject}: {score}")

    print("평균:", average)


if __name__ == "__main__":
    scores = get_scores()

    average = calculate_average(scores)

    print_results(scores, average)