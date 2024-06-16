import { PayloadAction, createSlice } from "@reduxjs/toolkit";
import { PropertyInfoResult } from "./api";

type HeatPumpState = {
   scopIndex: number
}

const initialState: HeatPumpState = {
    scopIndex: 0
}

export const heatpumpSlice = createSlice({
    name: "heatpump",
    reducers: {
        setPropertyInfo: (state, action: PayloadAction<PropertyInfoResult>) => {
            state.propertyInfo = action.payload
        },
        setScop: (state, action: PayloadAction<number>) => {
            state.scop = action.payload
        }
    },
    initialState
})