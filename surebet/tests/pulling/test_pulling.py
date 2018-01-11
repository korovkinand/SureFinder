from os import path
import pickle
import json

from surebet import *
from surebet.pulling.pull_surebets import pull
from surebet.tests.pulling import *


def test_known_result():
    filename = path.join(package_dir, "knownResult.json")
    with open(filename) as file:
        known_res = json.load(file)

    filename = path.join(package_dir, "knownResult.pkl")
    with open(filename, "rb") as file:
        known_res_sample = pickle.load(file)

    surebets = pull(known_res_sample)

    assert obj_to_json(surebets) == json_dumps(known_res)

    logging.info("PASS: known result")


def test_sample():
    filename = path.join(package_dir, "sample.pkl")
    with open(filename, "rb") as file:
        sample = pickle.load(file)

    sample[0].sort(key=lambda o: o["sport"])
    sample[1].sort(key=lambda o: o["sport"])
    for i in range(min(len(sample[0]), len(sample[1]))):
        part1, part2 = sample[0][i], sample[1][i]
        wagers_bets = [part1["part_bets"], part2["part_bets"]]
        if part1["sport"] == "tennis" or part1["sport"] == "volley":
            pull(wagers_bets, with_draw=False)
        else:
            pull(wagers_bets)

    logging.info("PASS: sample")
