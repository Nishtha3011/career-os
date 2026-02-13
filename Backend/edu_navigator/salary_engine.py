def estimate_salary(readiness):

    if readiness < 30:
        return "3-5 LPA (Entry Level)"

    elif readiness < 60:
        return "6-9 LPA (Junior Level)"

    elif readiness < 80:
        return "10-14 LPA (Mid Level)"

    else:
        return "15+ LPA (Interview Ready)"