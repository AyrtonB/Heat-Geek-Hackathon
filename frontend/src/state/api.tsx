import { fetchBaseQuery } from '@reduxjs/toolkit/query'
import { createApi } from '@reduxjs/toolkit/query/react'
import { get } from 'http'


const BASE_URL = 'https://hackathonapis-35klfnb33a-ew.a.run.app'

export interface PropertyInfoSearchParams {
    postcode: string
    address: string
}

export type PropertyInfoResult = {
    zor_model: string;
    home: {
      uprn: number;
      address: string;
      address_rm: string;
      longitude: number;
      latitude: number;
      postcode: string;
      country: string;
    };
    home_details: {
      property_type: string;
      property_age: string;
      property_age_int: number;
      urban_rural_classification: string;
      listed_building_grade: string;
      conservation_area: string;
      has_epc: boolean;
      is_on_gas_network: boolean;
      elec_co2_factor: number;
      gas_co2_factor: number;
      elec_unit_cost: number;
      gas_unit_cost: number;
    };
    fabric: Array<{
      type: string;
      floor_area: number;
      wall_type: string;
      wall_insulation: string;
      loft_insulation: number;
      glazing_type: string;
      property_age: string;
      epc_rating: string;
      epc_rating_score: string;
      epc_number: string;
      epc_date: string;
      epc_url: string;
      room_count: number;
      habitable_rooms: number;
      bathrooms: number;
      bedrooms: number;
      energy_demand_est: number;
      heat_loss_kw: number;
      heat_loss_factor: number;
      location_design_temp: number;
      location_degree_days: number;
      annual_heat_requirement_kwh: number;
      annual_heat_requirement_heating_kwh: number;
      annual_heat_requirement_hw_kwh: number;
    }>;
    designs: Array<{
      type: string;
      fabric: string;
      running_cost: number;
      fuel: string;
      boiler_efficiency: number;
      house_radiator_count: number;
      primary_circuit_size: number;
      microbore_risk: string;
      cylinder_present: boolean;
      is_a_hard_stop?: boolean;
      hard_stop_reason?: string;
      parts?: {
        heatpump: {
          id: string;
          model_rated_output: number;
          temp: number;
          flow_temp: number;
          output_thermal: number;
          scop: number;
          model_name: string;
          manufacturer_name: string;
          power_kw: number;
          is_defaultable: boolean;
          model: string;
          scop_hw: number;
          scop_weighted: number;
        };
        hp_count: number;
        meets_heat_loss: boolean;
        hp_flow_temp_scop: Array<{
          flow_temp: number;
          scop: number;
        }>;
        replaced_radiator_count: number;
        controls: string;
        primaries: string;
        cylinder: number;
      };
      energy_demand_annual_energy_demand_kwh?: number;
      energy_demand_fuel?: string;
      design_carbon_emissions?: number;
      carbon_saving_kg?: number;
      is_bus_eligible?: boolean;
      bus_issues?: Array<any>;
      install_costs?: {
        cost_install_total: number;
        cost_breakdown: {
          survey: number;
          parts_total: number;
          parts: {
            heatpump: number;
            cylinder: number;
            radiator_parts: number;
            controller: number;
            sundries: number;
            sundries_breakdown: {
              electrical: number;
              heatpump_base: number;
              flexipipe: number;
              flexi_feet: number;
              filters: number;
              diverter_valves: number;
              valves: number;
              filter_ball_valve: number;
              pipes: number;
            };
          };
          labour_all: number;
          labour_heatpump_cylinder: number;
          labour_hydronics: number;
          labour_commission: number;
          labour_electrician: number;
          install_margin: number;
          install_discount: number;
          installer_dayrate: number;
        };
      };
      install_total_days?: number;
      labour_days_breakdown?: {
        survey: number;
        heatpump_and_cylinder: number;
        hydronics: number;
        electrician: number;
        commission: number;
      };
      running_cost_gas?: number;
      running_cost_elec?: number;
      running_cost_tou?: number;
      savings_fixed_tariff?: number;
      savings_flexible_tariff?: number;
      finance_monthly_repayment?: number;
      monthly_savings_after_finance?: number;
      heatpump_placement?: {
        max_distance_neighbour: number;
        wall_length: number;
        risk_planning_requirement: string;
        risk_low_space: string;
        geojson_features: {
          type: string;
          features: Array<{
            id: string;
            type: string;
            properties: {
              feature_name: string;
              name: string;
            };
            geometry: {
              type: string;
              coordinates: Array<Array<Array<Array<number>>>>;
            };
          }>;
        };
      };
    }>;
    raw: {
      epc_data: {
        LMK_KEY: string;
        ADDRESS1: string;
        ADDRESS2: string;
        ADDRESS3?: string;
        POSTCODE: string;
        BUILDING_REFERENCE_NUMBER: number;
        CURRENT_ENERGY_RATING: string;
        POTENTIAL_ENERGY_RATING: string;
        CURRENT_ENERGY_EFFICIENCY: number;
        POTENTIAL_ENERGY_EFFICIENCY: number;
        PROPERTY_TYPE: string;
        BUILT_FORM: string;
        INSPECTION_DATE: string;
        LOCAL_AUTHORITY: string;
        CONSTITUENCY: string;
        COUNTY: string;
        LODGEMENT_DATE: string;
        TRANSACTION_TYPE: string;
        ENVIRONMENT_IMPACT_CURRENT: number;
        ENVIRONMENT_IMPACT_POTENTIAL: number;
        ENERGY_CONSUMPTION_CURRENT: number;
        ENERGY_CONSUMPTION_POTENTIAL: number;
        CO2_EMISSIONS_CURRENT: number;
        CO2_EMISS_CURR_PER_FLOOR_AREA: number;
        CO2_EMISSIONS_POTENTIAL: number;
        LIGHTING_COST_CURRENT: number;
        LIGHTING_COST_POTENTIAL: number;
        HEATING_COST_CURRENT: number;
        HEATING_COST_POTENTIAL: number;
        HOT_WATER_COST_CURRENT: number;
        HOT_WATER_COST_POTENTIAL: number;
        TOTAL_FLOOR_AREA: number;
        ENERGY_TARIFF: string;
        MAINS_GAS_FLAG: string;
        FLOOR_LEVEL: string;
        FLAT_TOP_STOREY?: string;
        FLAT_STOREY_COUNT?: string;
        MAIN_HEATING_CONTROLS: number;
        MULTI_GLAZE_PROPORTION: number;
        GLAZED_TYPE: string;
        GLAZED_AREA: string;
        EXTENSION_COUNT: number;
        NUMBER_HABITABLE_ROOMS: number;
        NUMBER_HEATED_ROOMS: number;
        LOW_ENERGY_LIGHTING: number;
        NUMBER_OPEN_FIREPLACES: number;
        HOTWATER_DESCRIPTION: string;
        HOT_WATER_ENERGY_EFF: string;
        HOT_WATER_ENV_EFF: string;
        FLOOR_DESCRIPTION: string;
        FLOOR_ENERGY_EFF: string;
        FLOOR_ENV_EFF?: string;
        WINDOWS_DESCRIPTION: string;
        WINDOWS_ENERGY_EFF: string;
        WINDOWS_ENV_EFF: string;
        WALLS_DESCRIPTION: string;
        WALLS_ENERGY_EFF: string;
        WALLS_ENV_EFF: string;
        SECONDHEAT_DESCRIPTION: string;
        SHEATING_ENERGY_EFF?: string;
        SHEATING_ENV_EFF?: string;
        ROOF_DESCRIPTION: string;
        ROOF_ENERGY_EFF: string;
        ROOF_ENV_EFF: string;
        MAINHEAT_DESCRIPTION: string;
        MAINHEAT_ENERGY_EFF: string;
        MAINHEAT_ENV_EFF: string;
      }
    }
}

export interface AnnualSavingsParameters {
  scop: number[]
  heat_loss_kw?: number;
  location_design_temp?: number;
}

type AnnualSavingsResponse = {
  key: string;
  value: number;
}[][]

  
export const apiSlice = createApi({
    reducerPath: 'api',
    baseQuery: fetchBaseQuery({ baseUrl: BASE_URL }),
    endpoints: builder => ({
        getPropertyInfo: builder.query<PropertyInfoResult, PropertyInfoSearchParams>({
            query: ({ postcode, address }) => `property_info/${address}/${postcode}`
        }),
        getAnnualSavings: builder.query<AnnualSavingsResponse, AnnualSavingsParameters>({
            query: (p) => `annual_savings/?scop=${p.scop}`
        })
    })
})

export const { useLazyGetPropertyInfoQuery, useGetAnnualSavingsQuery } = apiSlice