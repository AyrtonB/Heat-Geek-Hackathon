from pydantic import BaseModel


class OpexEstimate(BaseModel):
    annual_heat_pump_elec_cost: float
    annual_gas_boiler_counterfactual_cost: float
    annual_carbon_kg_reduction: float
