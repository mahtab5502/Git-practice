SUBJECTS = ["국어", "영어", "수학", "과탐"]

def get_scores():
    scores = {}

    for subject in SUBJECTS:
        score = float(input(f"{subject} 점수: "))
        scores[subject] = score

    return scores

if __name__ == "__main__":
    scores = get_scores()
    print(scores)