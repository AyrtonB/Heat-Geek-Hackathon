import { Card, List, Slider, Space } from 'antd'
import React from 'react'
import { AnnualSavingsParameters, useGetAnnualSavingsQuery } from '../state/api'
import { useSelector } from 'react-redux'
import { RootState } from '../state'
import { MAX_SCOP, MIN_SCOP, SCOP_INTERVAL, SCOP_VALUES } from '../constants'

const useHeatLossKw = () => useSelector((state: RootState) => {
    const propertyInfo = state.property.propertyInfo
    if(!propertyInfo) return undefined
    if(!propertyInfo.fabric) return undefined
    if(propertyInfo.fabric.length === 0) return undefined
    return state.property.propertyInfo?.fabric.map(f => f.heat_loss_kw).reduce((a, b) => a + b, 0)
})

const useLocationDesignTemp = () => useSelector((state: RootState) =>{
    const propertyInfo = state.property.propertyInfo
    if(!propertyInfo) return undefined
    if(!propertyInfo.fabric) return undefined
    const temps =  state.property.propertyInfo?.fabric.map(f => f.location_design_temp)
    if(!temps || temps.length === 0) return undefined
    return temps.reduce((a, b) => a + b, 0) / temps.length
})

const useQueryParams = (): AnnualSavingsParameters => {
    const heat_loss_kw = useHeatLossKw()
    const location_design_temp = useLocationDesignTemp()
    let params: AnnualSavingsParameters = {scop: SCOP_VALUES}
    if(heat_loss_kw) params['heat_loss_kw'] = heat_loss_kw
    if(location_design_temp) params['location_design_temp'] = location_design_temp
    return params
}

const ScopSlider: React.FC = () => {
    return (
        <Slider
            min={MIN_SCOP}
            max={MAX_SCOP}
            step={SCOP_INTERVAL}
            marks={{[MIN_SCOP]: MIN_SCOP, [MAX_SCOP]: MAX_SCOP}}
        />
    )
}

const AnnualSavings: React.FC = () => {
    const params = useQueryParams()
    const [scopIndex, setScopIndex] = React.useState(0)
    const { data, error, isLoading } = useGetAnnualSavingsQuery(params)
    return (
        <Card title="Annual Savings" loading={isLoading}>
            <Slider
                min={MIN_SCOP}
                max={MAX_SCOP}
                value={scopIndex}
                onChange={setScopIndex}
                step={SCOP_INTERVAL}
            />
            <Space direction='vertical'>
                {data && <List
                    dataSource={data[scopIndex]}
                    renderItem={item => (
                        <List.Item>
                            <List.Item.Meta title={item.key} description={item.value} />
                        </List.Item>
                    )}
                />}

            </Space>
        </Card>
    )
}

export default AnnualSavings