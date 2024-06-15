// This file is used to setup configure the heatpump

import { Card, Form, Slider } from "antd";
import React from "react";
import { useAppDispatch } from "../state/dispatch";
import { propertySlice } from "../state/property";
import { useSelector } from "react-redux";
import { RootState } from "../state";

const MIN_SCOP = 1;
const MCS_STANDARD = 2.8;
const MAX_SCOP = 5;

const MaxFlowTemperature: React.FC = () => {
  const dispatch = useAppDispatch();
  const value = useSelector(
    (state: RootState) => state.property.maxFlowTemperature
  );
  return (
    <Form.Item label={`SCoP ${value}`}>
      <Slider
        min={MIN_SCOP}
        max={MAX_SCOP}
        step={0.1}
        value={value}
        defaultValue={MCS_STANDARD}
        onChange={(value) => {
          dispatch(propertySlice.actions.setMaxFlowTemperature(value));
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
