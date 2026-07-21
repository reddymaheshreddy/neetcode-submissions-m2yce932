from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    student = scores[0][0]
    high_score = scores[0][1]
    for st,score in scores[1:]:
        if score > high_score:
            student,high_score = st,score
    return student


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
