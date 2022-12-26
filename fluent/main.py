from repos.repo_1 import questions
from factories.quiz_engine_factory import QuizEngineFactory

if __name__ == "__main__":
    qe = QuizEngineFactory.build(questions())
    qe.run()
    print(qe.summary())
