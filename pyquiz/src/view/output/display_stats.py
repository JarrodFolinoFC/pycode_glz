def display_stats(stats):
    print(f'Total: ({stats["total_questions"]})\n')
    print('Questions by Tag:')
    for tag in stats['tags']:
        print(f'* {tag} ({stats["tags"][tag]})')