from typing import List
import adijif

from fastapi import Header, HTTPException
from pydantic import BaseModel

#from api.core_app import app


class ClockSearch(BaseModel):
    part: str
    vcxo: int
    output_clocks: List[int]


#@app.post("/clock/solve")
def clock_chip_solve(search: ClockSearch, tr=Header(...)):

    if search.part not in adijif.clocks.supported_parts:
        raise HTTPException(
            status_code=404, detail="Part not supported or found: " + search.part
        )

    vcxo = 125000000

    clk = eval("adijif.{}()".format(search.part))

    # clk.n2 = 24
    # output_clocks = [1e9, 500e6, 7.8125e6]
    output_clocks = list(map(int, search.output_clocks))  # force to be ints
    clock_names = ["ADC", "FPGA", "SYSREF"]
    clk.set_requested_clocks(vcxo, search.output_clocks, clock_names)

    try:
        clk.solve()
    except:
        raise HTTPException(status_code=400, detail="No solution found")

    return {"config": clk.get_config()}
