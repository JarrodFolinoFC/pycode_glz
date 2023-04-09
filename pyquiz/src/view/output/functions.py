import pprint
pp = pprint.PrettyPrinter(indent=4)


def display_stats(stats):
    print(f'Total: ({stats["total_questions"]})\n')
    print('Questions by Tag:')
    for tag in stats['tags']:
        print(f'* {tag} ({stats["tags"][tag]})')


def display_summary(summary):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(summary)
