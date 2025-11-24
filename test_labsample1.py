import labsample1


def test_get_longest_workout():
    workouts = labsample1.load_csv()
    result=labsample1.get_longest_workout(workouts)
    expected=75.0
    assert(expected==result["duration"])


def test_calc_total_duration():
    workouts = labsample1.load_csv()
    result=labsample1.calc_total_duration(workouts)
    expected=853
    assert(expected==result)


def test_calc_average_duration():
    workouts = labsample1.load_csv()
    result=labsample1.calc_average_duration(workouts)
    expected=42.65
    assert(expected==result)
