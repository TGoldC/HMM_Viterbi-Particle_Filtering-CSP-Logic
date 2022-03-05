def neg_sym(sym):
    if sym.op == '~':
        return sym.args[0]
    else:
        return ~sym

def cnf_filter_assumption(clauses, pos_asspts, neg_asspts):
    return map(lambda c:
                   frozenset(
                       filter(
                           lambda s:
                               s not in neg_asspts,
                           c
                       )
                   ),
               filter(lambda c:
                          all(map(lambda pa:
                                      pa not in c,
                                  pos_asspts)),
                      clauses))

def fast_dpll(clauses):
    def dpll_with_assumption(clauses, pos_asspts, neg_asspts):
        return fast_dpll(frozenset(cnf_filter_assumption(clauses, pos_asspts, neg_asspts)))

    if frozenset() in clauses:
        return False # not satisfiable
    elif len(clauses) == 0:
        return True # satisfiable

    known_syms = frozenset(map(lambda c: next(iter(c)),
                               filter(lambda c: len(c)==1, clauses)))
    if len(known_syms) > 0:
        neg_known_syms = frozenset(map(neg_sym, known_syms))
        for nks in neg_known_syms:
            if nks in known_syms:
                return False # not satisfiable
        return dpll_with_assumption(clauses, known_syms, neg_known_syms)

    symc_dict = {}
    for clause in clauses:
        for sym in clause:
            symc_dict[sym] = symc_dict.get(sym, 0) + 1

    sym = max(symc_dict.keys(), key = symc_dict.get)
    nsym = neg_sym(sym)
    return dpll_with_assumption(clauses, [sym], [nsym]) or \
           dpll_with_assumption(clauses, [nsym], [sym])
