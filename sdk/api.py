def compute_vitality(Q, D, T_norm):
    """
    ORAC-NT Vitality Algorithm Core Logic.
    W(t) = Q(t) * D(t) - T_norm(t)
    """
    return (Q * D) - T_norm