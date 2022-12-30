from repos.repo_1 import questions
from repos.dict_1 import dict_questions
from repos.dunder_1 import dunder_questions
from repos.collections_1 import collections_questions
from repos.set_1 import set_questions
from repos.list_comps_1 import list_comp_questions
from repos.pattern_matching_1 import pm_questions
from repos.bytes import byte_questions
from factories.quiz_engine_factory import QuizEngineFactory

if __name__ == "__main__":
    qe = QuizEngineFactory.build(list_comp_questions())
    qe.run()
    print(qe.summary())
