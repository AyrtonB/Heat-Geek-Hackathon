import { PayloadAction, createSlice } from "@reduxjs/toolkit";
import { PropertyInfoResult } from "./property-info-api";

type PropertyState = {
    propertyInfo?: PropertyInfoResult
    maxFlowTemperature: number
    
}

const initialState:PropertyState = {
    maxFlowTemperature: 40

}

export const propertySlice = createSlice({
    name: "property",
    reducers: {
        setPropertyInfo: (state, action: PayloadAction<PropertyInfoResult>) => {
            state.propertyInfo = action.payload
        },
        setMaxFlowTemperature: (state, action: PayloadAction<number>) => {
            state.maxFlowTemperature = action.payload
        }
    },
    initialState
})