from repos.assigment import assignment_questions
from repos.bytes import byte_questions
from repos.collections_1 import collections_questions
from repos.decorators import deco_questions
from repos.dict_1 import dict_questions
from repos.dataclasses import dataclasses_questions
from repos.dunder_1 import dunder_questions
from repos.list_comps_1 import list_comp_questions
from repos.list_1 import list_questions
from repos.pattern_matching_1 import pm_questions
from repos.repo_1 import questions
from repos.set_1 import set_questions
from repos.slicing_1 import slicing_questions
from repos.unpacking_1 import unpacking_questions
from repos.references import reference_questions
from repos.first_class_functions import first_class_function_questions
from factories.quiz_engine_factory import QuizEngineFactory

if __name__ == "__main__":
    qe = QuizEngineFactory.build(deco_questions())
    qe.run()
    print(qe.summary())
