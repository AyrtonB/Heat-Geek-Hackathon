from pydantic import BaseModel


class AnnualCostEstimate(BaseModel):
    annual_heat_pump_elec_cost: float
    annual_gas_boiler_counterfactual_cost: float
    annual_carbon_kg_reduction: float





class OpexEstimate(BaseModel):
    annual: AnnualCostEstimate
