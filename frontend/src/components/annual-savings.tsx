import { Card, Form, List, Slider, Space, Spin } from "antd";
import React from "react";
import { AnnualSavingsParameters, useGetOpexEstimateQuery } from "../state/api";
import { useSelector } from "react-redux";
import { RootState } from "../state";
import {
  MAX_SCOP,
  MAX_SCOP_INDEX,
  MIN_SCOP,
  SCOP_INTERVAL,
  SCOP_VALUES,
} from "../constants";
import { useAppDispatch } from "../state/dispatch";
import { heatpumpSlice } from "../state/heatpump";

const useAnnualHeatKwhConsumption = () =>
  useSelector((state: RootState) => {
    const propertyInfo = state.property;
    if (!propertyInfo.addressLookup) return undefined;
    if (!propertyInfo.addressLookup.fabric) return undefined;
    if (propertyInfo.addressLookup.fabric.length === 0) return undefined;
    let total = 0;
    for (let fabric of propertyInfo.addressLookup.fabric) {
      total += fabric.annual_heat_requirement_heating_kwh;
    }
    return total;
  });

const roundScop = (scop: number) => Math.round(scop * 100) / 100;

const useQueryParams = (): AnnualSavingsParameters => {
  const annual_heat_kwh_consumption = useAnnualHeatKwhConsumption();
  const scops = SCOP_VALUES.map(roundScop);
  return { annual_heat_kwh_consumption, scops };
};

const ScopSlider: React.FC = () => {
  const scopIndex = useScopIndex();
  const dispatch = useAppDispatch();

  return (
    <Form.Item label="SCOP">
      <Slider
        min={0}
        max={MAX_SCOP_INDEX}
        style={{ width: "100%" }}
        value={scopIndex}
        tooltip={{
          formatter: (value) => SCOP_VALUES[scopIndex].toFixed(2),
        }}
        step={1}
        // marks={{ [MIN_SCOP]: MIN_SCOP, [MAX_SCOP]: MAX_SCOP }}
        onChange={(value) => {
          dispatch(heatpumpSlice.actions.setScopIndex(value));
        }}
      />
    </Form.Item>
  );
};

const useScopIndex = () =>
  useSelector((state: RootState) => state.property.scopIndex);

const OpexEstimateResultsList: React.FC = () => {
  const params = useQueryParams();
  const scopIndex = useScopIndex();
  const { data, error, isLoading } = useGetOpexEstimateQuery(params);
  return (
    <>
      {isLoading && <Spin />}
      {data && (
        <List
          dataSource={data?.[scopIndex]?.annual}
          renderItem={(item) => (
            <List.Item>
              <List.Item.Meta title={item.key} description={item.value} />
            </List.Item>
          )}
        />
      )}
    </>
  );
};

const AnnualSavingsCard: React.FC = () => {
  const hasAddressLookup = useSelector(
    (state: RootState) => !!state.property.addressLookup
  );
  if(!hasAddressLookup) return null;
  return (
    <Card title="Annual Savings">
      <Space direction="vertical" style={{ width: "100%" }}>
        <ScopSlider />
        <OpexEstimateResultsList />
      </Space>
    </Card>
  );
};

export default AnnualSavingsCard;
