from prop_fc import prop_fc
from dpll import fast_dpll
from logic import conjuncts, to_cnf, disjuncts

class FCPropKB:
    def __init__(self):
        self.clauses = set()
    def tell(self, clause):
        self.clauses.add(clause)
    def has_contradicting_knowledge(self):
        dpll_kb = DpllPropKB()
        for prop in self.clauses:
            dpll_kb.tell(prop)
        return dpll_kb.has_contradicting_knowledge()
    def ask(self, clause):
        return prop_fc(self, clause)

class DpllPropKB:
    def __init__(self):
        self.clauses = set() #知识库用集合表示，重复的元素会被自动合并
    def tell(self, sentence):
        self.clauses.update(map(frozenset,
                                map(set,
                                    map(disjuncts,
                                        conjuncts(to_cnf(sentence))))))
    def has_contradicting_knowledge(self):
        return not fast_dpll(self.clauses)
    def ask(self, prop):
        to_prove = frozenset(map(frozenset,
                                 map(set,
                                     map(disjuncts,
                                         conjuncts(to_cnf(~prop)))))) \
                    | self.clauses #把要证明的结论先否定再整理成CNF的形式，再和原来KB中的子句们并一下

        if fast_dpll(to_prove):
            return False #是否有contradiction,若没有（fast_dpll()为True）
        else:
            self.tell(prop) #如果结论成立(有contradiction)，那么就把新的推论给到KB
            return True
