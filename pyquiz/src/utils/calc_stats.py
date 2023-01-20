from collections import Counter


def calc_stats(questions):
    return {
        'total_questions': len(questions),
        'tags_summary': uniq_tags(questions),
        'tags': tag_count(questions),
    }

def tag_count(questions):
    counter = Counter()
    for q in questions:
        counter.update(q.tags)

    return counter


def uniq_tags(questions):
    tag_set = set()
    [[tag_set.add(tag) for tag in q.tags] for q in questions]
    return list(tag_set)
