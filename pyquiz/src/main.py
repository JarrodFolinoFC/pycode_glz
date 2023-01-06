from repos.assigment import *
from repos.bytes import *
from repos.classes import *
from repos.collections_1 import *
from repos.decorators_1 import *
from repos.dict_1 import *
from repos.dataclasses import *
from repos.dunder_1 import *
from repos.list_comps_1 import *
from repos.list_1 import *
from repos.pattern_matching_1 import *
from repos.repo_1 import *
from repos.set_1 import *
from repos.slicing_1 import *
from repos.unpacking_1 import *
from repos.references import *
from repos.first_class_functions import *
from factories.quiz_engine_factory import QuizEngineFactory
from decorators.quiz_item_registry import QuizItemRegistry

import pprint
pp = pprint.PrettyPrinter(indent=4)

if __name__ == "__main__":
    registry = QuizItemRegistry.registry()
    qe = QuizEngineFactory.build(registry)
    print(qe.stats())
    # qe.run()
    pp.pprint(qe.summary())
