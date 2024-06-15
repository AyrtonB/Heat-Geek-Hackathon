// This file is used to setup configure the heatpump

import { Card, Form, Slider, SliderSingleProps } from "antd";
import React from "react";
import { useAppDispatch } from "../state/dispatch";
import { propertySlice } from "../state/property";

const MAX_FLOW_TEMPERATURE = 55;
const MIN_FLOW_TEMPERATURE = 35;

const marks: SliderSingleProps["marks"] = {
  35: "35°C",
  40: "40°C",
  45: "45°C",
  50: "50°C",
  55: "55°C",
};
const MaxFlowTemperature: React.FC = () => {
    const dispatch = useAppDispatch()
  return (
    <Form.Item label="Max flow temperature">
    <Slider 
      step={5}
      marks={marks}
      min={MIN_FLOW_TEMPERATURE}
      max={MAX_FLOW_TEMPERATURE}
      defaultValue={MAX_FLOW_TEMPERATURE}
      onChange={(value) => {
        dispatch(propertySlice.actions.setMaxFlowTemperature(value))
      }}
    />
  </Form.Item>
  );
};

const HeatpumpSetup: React.FC = () => {
  return (
    <Card title="Heatpump">
      <MaxFlowTemperature />
    </Card>
  );
};

export default HeatpumpSetup;
