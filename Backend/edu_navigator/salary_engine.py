def estimate_salary(readiness):
    if readiness < 40:
        return "₹3–5 LPA (Fresher)"
    elif readiness < 70:
        return "₹6–10 LPA (Junior Level)"
    else:
        return "₹12+ LPA (Interview Ready)"