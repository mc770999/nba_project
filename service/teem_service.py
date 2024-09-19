from toolz import pipe,reduce
from toolz.curried import partial

from model.teem_model import Teem


def convert_to_teem(t):
    return  Teem(name=t["name"],position_C=t["c"],position_SF=t["sf"],position_PF=t["pf"],position_SG=t["sg"],position_PG=t["pg"])

