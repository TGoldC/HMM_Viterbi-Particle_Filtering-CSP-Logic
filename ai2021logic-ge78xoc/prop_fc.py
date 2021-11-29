from logic import conjuncts

def prop_fc(kb, alpha):
    old_clauses_len = 0
    while old_clauses_len != len(kb.clauses):
        old_clauses_len = len(kb.clauses)
        for clause in set(kb.clauses):
            if clause.op in ("==>", "<=>"):
                if all(map(lambda c: c in kb.clauses, conjuncts(clause.args[0]))):
                    kb.clauses.update(conjuncts(clause.args[1]))
            if clause.op in ("<==", "<=>"):
                if all(map(lambda c: c in kb.clauses, conjuncts(clause.args[1]))):
                    kb.clauses.update(conjuncts(clause.args[0]))
            if alpha in kb.clauses:
                return True
    return False
